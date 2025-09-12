from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Foreign Key: many posts can belong to a User(auther) and on_delete: If the user is deleted, their post is deleted
    title = models.CharField(max_length=100) 
    slug = models.SlugField(unique=True) # made from the title, all lowercase with hyphens instead of spaces
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    cover_image = models.ImageField(upload_to='post_images/', blank=True, null=True) # blank and null means it's optional to have a cover image
    published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True) # auto_add_now is when the object is first created
    updated_at = models.DateTimeField(auto_now=True) # auto_now updates the field every time you save the object

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.CharField(max_length=100)
    content = models.TextField()
    approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user}"