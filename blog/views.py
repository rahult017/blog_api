from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated


class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]


class BlogRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
