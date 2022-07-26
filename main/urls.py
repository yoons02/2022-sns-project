from django.urls import path
from .views import *
from . import views

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('', showcontact, name="showcontact"),
    path('<int:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('list/', list, name="list"),
    path('create/', create, name="create"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('<str:post_id>/create_comment', create_comment, name="create_comment"),
    path('<str:comment_id>/edit_comment',edit_comment,name='edit_comment'),
    path('<str:comment_id>/update_comment',update_comment,name='update_comment'),
    path('<str:comment_id>/delete_comment',delete_comment,name='delete_comment'),
    # 1. like_toggle url 연결하기
    path('like_toggle/<int:post_id>/', views.like_toggle, name="like_toggle"),
    # 1-1. my_like url 연결하기
    path('my_like/<int:user_id>', views.my_like, name='my_like'),
    # 2. dislike_toggle url 연결하기
    path('dislike_toggle/<int:post_id>/', views.dislike_toggle, name="dislike_toggle"),
    # 2-1. my_dislike url 연결하기
    path('my_dislike/<int:user_id>', views.my_dislike, name='my_dislike'),
]