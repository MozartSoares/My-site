from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'created_on', 'slug', 'status')# exibe lista com todos os posts criados
  list_filter = ('status',)  # filtra os posts por status 
  search_fields = ['title', 'content']# campos de busca
  prepopulated_fields = {"slug":('title',)}# campos que são prepopulados
  
  
admin.site.register(Post, PostAdmin)