from django.db import models
from django.contrib.auth.models import User #utilizando o modelo User do django.models

STATUS = ( 
  (0, 'Draft'),
  (1, 'Publish')
)

#usar models.Model para herdar automaticamente da biblioteca django.models
#abstração de um post do blog:
class Post(models.Model):
  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True) #identificação do post
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
  updated_on = models.DateTimeField(auto_now_add=True)
  content = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  status = models.IntegerField(choices=STATUS, default=0)
  
  class Meta:
    ordering = ['-created_on'] #define a ordem de acordo com o created_on 
    
  def __str__(self):
    return self.title