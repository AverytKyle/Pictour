from django.urls import path
from .views.user_views import *

urlpatterns = [
    path('users/create/', create_user, name='create_user'),
    path('users/', get_users, name='get_users'),
    path('user/<int:user_id>/', get_user, name='get_user'),
    path('user/<int:user_id>/update/', update_user, name='update_user'),
]