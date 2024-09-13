from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.post.models import post

class PostView(APIView):
    def get(self, request):
        Post = [Posts.title for Posts in post.objects.all()]
        return Response(status=status.HTTP_200_OK, data=Post)