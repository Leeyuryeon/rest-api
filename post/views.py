from django.shortcuts import render

from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

# Create your views here.
