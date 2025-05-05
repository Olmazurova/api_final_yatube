from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post
from .mixins import AuthorFieldMixin

User = get_user_model()


class PostSerializer(AuthorFieldMixin, serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(AuthorFieldMixin, serializers.ModelSerializer):

    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
