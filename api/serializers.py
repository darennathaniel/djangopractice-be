from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer
from .models import BlogPost, User, Comments 

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'

class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class CommentsSerializer(ModelSerializer):
    user = UserSerializer()
    blogpost = BlogPostSerializer()

    class Meta:
        model = Comments
        fields = '__all__'