from django import forms

from . models import Comment

#Con Form creamos un formulario desde cero
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget= forms.Textarea)


#Con ModelForm creamos un formulario desde un modelo
class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['name', 'email', 'body']