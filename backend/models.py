from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name='albums', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {
            "id": self.id,
            "user_id": self.user_id.id,
            "title": self.title,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {
            "id": self.id,
            "user_id": self.user_id.id,
            "image_url": self.image_url,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    image_id = models.ForeignKey(Image, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {
            "id": self.id,
            "user_id": self.user_id.id,
            "image_id": self.image_id.id,
            "content": self.content,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    
class AlbumImage(models.Model):
    id = models.AutoField(primary_key=True)
    album_id = models.ForeignKey(Album, related_name='album_images', on_delete=models.CASCADE)
    image_id = models.ForeignKey(Image, related_name='album_images', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {
            "id": self.id,
            "album_id": self.album_id.id,
            "image_id": self.image_id.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }