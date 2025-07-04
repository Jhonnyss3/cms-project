from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'image', 'link', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']