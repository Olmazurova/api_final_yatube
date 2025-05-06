from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

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
    user = serializers.SlugRelatedField(
        slug_field='username',
        default=CurrentUserDefault(),
        read_only=True
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(), fields=['user', 'following']
            )
        ]

    def validate_following(self, value):
        if value == self.context.get('request').user:
            raise serializers.ValidationError(
                'Пользователь не может быть подписан сам на себя.'
            )
        return value
