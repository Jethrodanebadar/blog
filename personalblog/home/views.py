from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import  DeleteView
from .models import blog_data
from django.core.exceptions import ViewDoesNotExist
from django.http.response import HttpResponse
from .forms import Blogform


def Homeview(request):
    list_posts = blog_data.objects.all()
    return render(request, "home/home.html", {
        "blogs": list_posts
    })


def Detaildisplay(request, pk):
    try:
        list_posts = blog_data.objects.get(pk=pk)
    except ViewDoesNotExist:
        return HttpResponse(404, "Page not Found")
        
    
    return render(request, "home/post-page.html", {
        "post": list_posts
    })
    

class Createblog(CreateView):
    model = blog_data
    form_class = Blogform
    template_name = "home/create.html"
    success_url = '/home/'
    
class Updateblog(UpdateView):
    model = blog_data
    form_class = Blogform
    template_name = "home/create.html"
    success_url = '/home/'
    
class Deleteblog(DeleteView):
    model = blog_data
    success_url = '/home/'
    template_name = 'home/delete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context