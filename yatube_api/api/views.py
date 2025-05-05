from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from posts.models import Comment, Follow, Group, Post
from .mixins import PermissionMixin
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(PermissionMixin, ModelViewSet):
    """Представление API для модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class CommentViewSet(PermissionMixin, ModelViewSet):
    """Представление API для модели Comment."""

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return serializer.save(author=self.request.user, post=post)


class GroupViewSet(ReadOnlyModelViewSet):
    """Представление API для модели Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(ModelViewSet):
    """Представление API для модели Follow."""

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [filters.SearchFilter, ]
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        following = [
            follow.following
            for follow
            in Follow.objects.filter(user=self.request.user)
        ]
        if serializer.validated_data['following'] in following:
            raise ValidationError(
                'Вы уже подписаны на этого пользователя.'
            )
        if serializer.validated_data['following'] == self.request.user:
            raise ValidationError(
                'Пользователь не может быть подписан сам на себя.'
            )
        return serializer.save(user=self.request.user)
