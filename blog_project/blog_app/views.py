from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Post, Comment
from .serializers import CategorySerializer, PostSerializer, CommentSerializer
from rest_framework import viewsets
# Create your views here.

def homepage_view(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'blog_app/home.html', {'posts':posts, 'categories':categories})

def category_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(category=category, published=True).order_by('-created_at')
    return render(request, 'blog_app/category.html', {'category':category, 'posts':posts})

def post_view(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    comments = post.comments.filter(approved=True)
    if request.method == "POST":
        user = request.POST.get("user")
        content = request.POST.get("content")
        if user and content:
            Comment.objects.create(post=post, user=user, content=content, approved=True)
            return redirect('post_detail', slug=post.slug)
    return render(request, 'blog_app/post_detail.html', {'post':post, 'comments':comments})

# def comment_view(request, slug):
#     post = get_object_or_404(Post, slug=slug, published=True)
#     if request.method == "POST":
#         user = request.POST.get("user")
#         content = request.POST.get("content")
#         Comment.objects.create(post=post, user=user, content=content, approved=False)
#         return redirect('post_detail', slug=post.slug)
#     return redirect('post_detail', slug=post.slug)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer