from rest_framework.generics import ListCreateAPIView, GenericAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.request import Request
from rest_framework import mixins, generics
from .models import Blog, BlogComment
from .serializers import BlogSerializer, CommentsSerializer, SpecificBlogCommentsListSerializer
from .permissions import IsAuthorOrReadOnly


class BlogPagination(PageNumberPagination):
    page_size = 3


class BlogListCreateApiView(ListCreateAPIView):
    queryset = Blog.objects.order_by("-release_date").filter(is_active=True)
    serializer_class = BlogSerializer
    pagination_class = BlogPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
        


class BlogDetailsApiView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):
    queryset = Blog.objects.order_by("-release_date").all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]
    lookup_field = 'pk'
    
    def get(self,request:Request, pk):
        return self.retrieve(request,pk)
    
    def put(self,request:Request, pk):
        return self.update(request,pk)
    
    def delete(self,request:Request, pk):
        return self.destroy(request,pk)
    

class CreateCommentApiView(CreateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
    
class UpdateDeleteCommentApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]
    lookup_field = 'pk'
    
class SpecificBlogCommentsApiView(generics.ListAPIView):
    serializer_class = SpecificBlogCommentsListSerializer
    
    def get_queryset(self):
        blog_id = self.kwargs['blog_id']
        queryset = BlogComment.objects.filter(blog_id=blog_id).all()
        return queryset