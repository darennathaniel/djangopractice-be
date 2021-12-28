from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes, name="routes"),
    path('posts/',views.getPosts, name="posts"),
    path('posts/create/',views.postPost, name="create"),
    path('posts/comments/',views.commentPost, name="comment"),
    path('posts/delete/<str:idx>/', views.deletePost, name="delete"),
    path('posts/<str:idx>/',views.getPost, name="post"),
]