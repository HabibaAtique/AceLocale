from django.shortcuts import render
from personal_app.views import BlogPost
from django.views.generic import TemplateView
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    
    template_name = 'main.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_posts = BlogPost.objects.all()
        context['blog_posts'] = blog_posts
        return context