from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name="home"),
    path('post/<slug:slug>/', views.post_view, name="post_detail"),
    path('category/<str:category_name>/', views.category_view, name="category"),
    path('post/<slug:slug>/comment/', views.comment_view, name="comment"),
]