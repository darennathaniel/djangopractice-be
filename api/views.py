from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(req):
    routes=[
        {
            'Endpoint': '/blogpost/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of blogpost'
        },
        {
            'Endpoint': '/blogpost/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single blogpost object'
        },
        {
            'Endpoint': '/blogpost/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new blogpost with data sent in post request'
        },
        {
            'Endpoint': '/blogpost/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing blogpost with data sent in post request'
        },
        {
            'Endpoint': '/blogpost/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting blogpost'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getPosts(req):
    posts = BlogPost.objects.all()
    serializer = BlogPostSerializer(posts,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPost(req,idx):
    post = BlogPost.objects.get(id=idx)
    serializer = BlogPostSerializer(post,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postPost(req):
    data = req.data
    post = BlogPost.objects.create(title=data['title'],body=data['body'])
    serializer = BlogPostSerializer(post, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def commentPost(req):
    data = req.data
    post = BlogPost.objects.get(id=data['idx'])
    post.comments['all'].append(data['comment'])
    post.save()
    serializer = BlogPostSerializer(post, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deletePost(req,idx):
    post = BlogPost.objects.get(id=idx)
    post.delete()
    posts = BlogPost.objects.all()
    serializer = BlogPostSerializer(posts, many=True)
    return Response(serializer.data)