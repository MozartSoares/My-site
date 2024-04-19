from django.views import generic

from blog.models import Post

#herdando de uma classe pré pronta no django para dar overwrite e modificar um método, nesse caso o get
class PostView(generic.ListView):
  #criando a lista e passando ela para o template index.html onde temos o laço for nos posts
  queryset = Post.objects.filter(status=1).order_by('-created_on')
  template_name= 'index.html'

class PostDetail(generic.DetailView):
  #passando o post para o post_detail para exibir atributos dele
  model = Post
  template_name = 'post_detail.html'