from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name="home"),
    path('category/', views.category_view, name="category"),
    path('post/', views.post_view, name="post"),
    path('comment/', views.comment_view, name="comment"),
]