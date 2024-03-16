from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def delete(self, ratus=status.HTTP_204_NO_CONTENT):
        queryset = BlogPost.objects.all()
        serializer_class = BlogPostSerializer
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'
    
    
class BlogPostList(APIView):
    def get(self, request, format=None):
        # get title from the query parameters (if none, default to empty string)
        title = request.query_params.get('title', '')
        
        if title:
            #filter the queryset base on the title
            blog_post = BlogPost.objects.filter(title__icontains=title)
        else:
          #if no title provied, return all blog posts
          blog_post = BlogPost.objects.all() 
        serializer = BlogPostSerializer(blog_post, many=True)
        return Response(serializer.data, status.HTTP_200_OK) 
        
        