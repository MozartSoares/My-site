from django.http import HttpResponse
from django.views import generic

#herdando de uma classe pré pronta no django para dar overwrite e modificar um método, nesse caso o get
class PostView(generic.View):
  def get(self, request, *args, **kwargs):
    return HttpResponse('hello world !')