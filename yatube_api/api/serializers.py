from rest_framework import serializers
from posts.models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'group', 'author', 'image', 'pub_date',)
        read_only_fields = ('author', 'pub_date', 'id',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description',)


class CommentSerializer(serializers.ModelSerializer):
    class Merta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created',)
        read_only_field = ('id', 'author', 'created',)