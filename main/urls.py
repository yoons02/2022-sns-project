from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('', showcontact, name="showcontact"),
    path('<int:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('<str:post_id>/create_comment', create_comment, name="create_comment"),
    # path('<int:post_id>/comments/<int:comment_id>/delete/', views.comment_delete, name="delete_comment"),
]