from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.post.models import post
from apps.post.api.serializers import PostSerializer


class PostViewSet(ViewSet):
    def list(self, request): 
        #Post = [Posts.title for Posts in post.objects.all()]
        serializer = PostSerializer(post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def retrieve(self, request, pk=int):
        serializer = PostSerializer(post.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def create(self, request):
        #post.objects.create(title=request.data['title'], description=request.data['description'], order=request.data['order'])
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return self.get(request)
