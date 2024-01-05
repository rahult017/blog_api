from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from blog.models import Blog
from blog.serializers import BlogSerializer, UserSerializer



class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, *args, **kwargs):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
