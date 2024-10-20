from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author'] # Agrega un panel de filtros en la barra lateral derecha de la interfaz del listado de posts. 
    search_fields = ['title', 'body'] # Agrega una barra de búsqueda para que los administradores puedan buscar posts.
    prepopulated_fields = {'slug': ('title',)} # El campo slug se autocompletará automáticamente basándose en el campo title.
    raw_id_fields = ['author'] # Convierte el campo author en un campo de búsqueda con un selector desplegable en la interfaz de administración.
    date_hierarchy = 'publish' # Agrega un filtro jerárquico por fecha en la parte superior de la página de listado de posts.
    ordering = ['status', 'publish'] # Define el orden predeterminado de los posts en la página de listado.
