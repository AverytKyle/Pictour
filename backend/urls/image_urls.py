from django.urls import path
from ..views.image_views import *
from ..views.album_image_views import *

urlpatterns = [
    path('create/', create_image, name='create_image'),
    path('', get_images, name='get_images'),
    path('user/<int:user_id>/', get_user_images, name='get_user_images'),
    path('album/<int:album_id>/', get_album_images_by_album, name='get_album_images_by_album'),
    path('<int:image_id>/', get_image, name='get_image'),
    path('<int:image_id>/update/', update_image, name='update_image'),
    path('<int:image_id>/delete/', delete_image, name='delete_image'),
]