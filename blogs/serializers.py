from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Blog, BlogComment

class BlogSerializer(ModelSerializer):
    author = serializers.CharField(source= 'author.username', read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
        

class CommentsSerializer(ModelSerializer):
    author = serializers.CharField(source= 'author.username', read_only=True)
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.filter(is_active=True), write_only=True)
    blog_title = serializers.CharField(source= 'blog.title', read_only=True)
    
    class Meta:
        model = BlogComment
        fields = '__all__'
        
class SpecificBlogCommentsListSerializer(ModelSerializer):
    blog = BlogSerializer(read_only=True)
    class Meta:
        model = BlogComment
        fields= '__all__'