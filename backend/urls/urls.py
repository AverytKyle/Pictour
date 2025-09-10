from django.urls import path, include
from ..views.user_views import *
from ..views.album_views import *
from ..views.image_views import *
from ..views.comment_views import *

urlpatterns = [
    path('users/', include('backend.urls.user_urls')),
    path('albums/', include('backend.urls.album_urls')),
    path('images/', include('backend.urls.image_urls')),
    path('comments/', include('backend.urls.comment_urls')),
]