from django.db import models

# Create your models here.
class User(models.Model):
    name=models.TextField()
    email=models.EmailField(null=True, blank=True)
    created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name[:50]

class BlogPost(models.Model):
    body = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:50]

class Comments(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.TextField(null=True,blank=True)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment[:50]