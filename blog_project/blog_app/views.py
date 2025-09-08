from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post, Comment

# Create your views here.

def homepage_view(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog_app/home.html', {'posts':posts})

def category_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(category=category, published=True).order_by('-created_at')
    return render(request, 'blog_app/category.html', {'category':category, 'posts':posts})

def post_view(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    comments = post.comments.filter(approved=True)
    return render(request, 'blog_app/post_detail.html', {'post':post, 'comments':comments})

def comment_view(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    if request.method == "POST":
        user = request.POST.get("user")
        content = request.POST.get("content")
        Comment.objects.create(post=post, user=user, content=content, approved=False)
        return redirect('post_detail', slug=post.slug)
    return redirect('post_detail', slug=post.slug)
