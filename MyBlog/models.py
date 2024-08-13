from django.db import models
from django.utils.text import slugify
# from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    img = models.URLField(null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(unique=True)


    def save (self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title

class about(models.Model):
    content = models.TextField()
    
# class User(models.User):
#     pass
class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comment")
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"comment from {self.name} on {self.post}"
