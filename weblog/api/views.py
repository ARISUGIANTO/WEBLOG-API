from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from api.models import Post, Comment, Category
from api.serializers import UserSerializer, PostSerializer, CommentSerializer, CategorySerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, pk=None, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request, pk=None, format=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, pk=None, format=None):
        if request.method == 'POST':
            return self.create(request, pk=pk, format=format)

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request, pk=None, format=None):
        if request.method == 'PUT':
            return self.update(request, pk=pk, format=format)
        elif request.method == 'PATCH':
            return self.partial_update(request, pk=pk, format=format)

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, pk=None, format=None):
        if request.method == 'POST':
            return self.create(request, pk=pk, format=format)

class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request, pk=None, format=None):
        if request.method == 'PUT':
            return self.update(request, pk=pk, format=format)
        elif request.method == 'PATCH':
            return self.partial_update(request, pk=pk, format=format)

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, pk=None, format=None):
        if request.method == 'POST':
            return self.create(request, pk=pk, format=format)

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request, pk=None, format=None):
        if request.method == 'PUT':
            return self.update(request, pk=pk, format=format)
        elif request.method == 'PATCH':
            return self.partial_update(request, pk=pk, format=format)
