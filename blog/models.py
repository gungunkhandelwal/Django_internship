from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    

class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="blog_posts",blank=True,null=True)
    title=models.CharField(max_length=200,blank=True)
    image=models.ImageField(upload_to='blog_images/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='blog_posts')
    summary=models.TextField(max_length=300)
    content=models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Dr. {self.author} posted - {self.title} Blog'

