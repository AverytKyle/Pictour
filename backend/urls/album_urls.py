from django.urls import path
from ..views.album_views import *

urlpatterns = [
    path('create/', create_album, name='create_album'),
    path('', get_albums, name='get_albums'),
    path('<int:album_id>/', get_album, name='get_album'),
    path('<int:album_id>/update/', update_album, name='update_album'),
    path('<int:album_id>/delete/', delete_album, name='delete_album'),
    path('user/<int:user_id>/albums/', get_user_albums, name='get_user_albums'),
]