from django.db import models
from users.models import User

class Blog(models.Model):
    title = models.CharField(max_length= 200, db_index=True)
    text = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'blogs')
    is_active = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'blogs'
        
    def __str__(self):
        return f'{self.title} / is published: {self.is_active}'
    
class BlogComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comments')
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'blog_comments'
        
    def __str__(self):
        return f'{self.author} / {self.blog}'