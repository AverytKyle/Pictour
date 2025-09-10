from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import AlbumImage
from ..serializer import AlbumImageSerializer

@api_view(['GET'])
def get_album_images(request):
    if request.method == 'GET':
        album_images = AlbumImage.objects.all()
        serializer = AlbumImageSerializer(album_images, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_album_image(request, album_image_id):
    try:
        album_image = AlbumImage.objects.get(id=album_image_id)
    except AlbumImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlbumImageSerializer(album_image)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_album_images_by_album(request, album_id):
    if request.method == 'GET':
        album_images = AlbumImage.objects.filter(album_id=album_id)
        serializer = AlbumImageSerializer(album_images, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_album_image(request):
    if request.method == 'POST':
        serializer = AlbumImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'PATCH'])
def update_album_image(request, album_image_id):
    try:
        album_image = AlbumImage.objects.get(id=album_image_id)
    except AlbumImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method in ['PUT', 'PATCH']:
        serializer = AlbumImageSerializer(album_image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_album_image(request, album_image_id):
    try:
        album_image = AlbumImage.objects.get(id=album_image_id)
    except AlbumImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        album_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)