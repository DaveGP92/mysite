from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post, Comment
from . forms import EmailPostForm, CommentForm
from django.core.mail import send_mail

from django.views.decorators.http import require_POST


# def posts_list(request): # --> Function-based view
#     posts_list = Post.published.all()
#     paginator = Paginator(posts_list, 3)
#     page_number = request.GET.get('page', 1)
    
#     try:
#         posts = paginator.page(page_number)

#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)

#     except PageNotAnInteger:
#         posts = paginator.page(1)

#     return render(request, 'blog/post/list.html', {
#         'posts': posts
#     })


class PostListView(ListView): # --> Class-based view
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_share(resquest, post_id):
    post = get_object_or_404(Post, id = post_id, status = Post.Status.PUBLISHED)
    sent = False

    if resquest.method == 'POST':
        form = EmailPostForm(resquest.POST)
    
        if form.is_valid():
            cd = form.cleaned_data
            post_url = resquest.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                        f"{cd['name']}\'s cooments : {cd['comments']}"
            send_mail(subject, message, 'gonzalezdave611@gmail.com', [cd['to']])
            sent = True
        
    else:
         form = EmailPostForm()
        
    return render(resquest, 'blog/post/share.html', {
        'post' : post, 
        'form': form,
        'sent': sent
        })

 
def post_detail(request, year, month, day, post):

    post = get_object_or_404(Post, status= Post.Status.PUBLISHED,
                             slug= post,
                             publish__year= year,
                             publish__month= month,
                             publish__day= day)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    
    return render(request, 'blog/post/detail.html', context)


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    
    context = {'post': post,
               'form': form,
               'comment': comment}
    
    return render(request, 'blog/post/comment.html', context)

