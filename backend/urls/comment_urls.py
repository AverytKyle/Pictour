from django.urls import path
from ..views.comment_views import *

urlpatterns = [
    path('', get_comments, name='get_comments'),
    path('user/<int:user_id>/', get_user_comments, name='get_user_comments'),
    path('image/<int:image_id>/', get_image_comments, name='get_image_comments'),
    path('create/', create_comment, name='create_comment'),
    path('<int:comment_id>/', get_comment, name='get_comment'),
    path('<int:comment_id>/update/', update_comment, name='update_comment'),
    path('<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]