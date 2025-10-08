from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', views.homepage_view, name="home"),
    path('post/<slug:slug>/', views.post_view, name="post_detail"),
    path('category/<str:category_name>/', views.category_view, name="category"),
    path('', include(router.urls)),
]