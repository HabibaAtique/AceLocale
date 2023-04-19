
from django.shortcuts import render, redirect,get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

"""
def main(request):
    return render(request, 'main.html')
"""


def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')
from .forms import BlogPostForm





def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_post_list')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})

def blog_post_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_post_list.html', {'blog_posts': blog_posts})

def blog_post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_post_detail.html', {'post': post})

def blog_post_main(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_post_main.html', {'post': post})

class PostUpdateView(UpdateView):
    model = BlogPost
    fields = ['category', 'title', 'body', 'photo']
    template_name = 'post_edit.html'
    success_url = reverse_lazy('blog_post_list')




def post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.delete()
    return redirect('blog_post_list')
