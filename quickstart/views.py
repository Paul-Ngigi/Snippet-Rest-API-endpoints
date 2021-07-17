from django.shortcuts import render
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.

class AllPosts(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
# class AllPosts(APIView):
#     """
#     GET, POST, PUT, DELETE, PATCH
#     """
#     def get(self, request):
#         queryset = Snippet.objects.all()
#         serializer = SnippetSerializer(queryset, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializers = SnippetSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
#
class SinglePost(APIView):
    def post(self, pk):
        singlePost = Snippet.objects.get(pk=pk)
        return singlePost

    def get(self, request, pk):
        post = self.post(pk)
        serializer = SnippetSerializer(post, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.post(pk)
        serializer = SnippetSerializer(post, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.post(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
