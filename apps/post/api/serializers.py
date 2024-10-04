from rest_framework.serializers import ModelSerializer
from apps.post.models import post

class PostSerializer(ModelSerializer):
    class Meta: 
        model = post
        #fields = "__all__"
        fields = ['id','title','description','order','updated_at']