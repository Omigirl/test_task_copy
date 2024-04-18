from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author_name', 'comment_text', 'created_date']
        extra_kwargs = {'post': {'write_only': True, 'required': False}}

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  
    published_date = serializers.DateTimeField(read_only=True)  

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'published_date', 'comments']  

