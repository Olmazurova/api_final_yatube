from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)
from rest_framework.exceptions import ValidationError

from posts.models import Post, Comment, Group, Follow
from .serializers import (CommentSerializer, PostSerializer,
                          GroupSerializer, FollowSerializer)
from .permissions import AuthorOrReadOnly


class PostViewSet(ModelViewSet):
    """Представление API для модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly, AuthorOrReadOnly,]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    """Представление API для модели Comment."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, AuthorOrReadOnly,]

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        post = get_object_or_404(Post,id=self.kwargs.get('post_id'))
        return serializer.save(author=self.request.user, post=post)


class GroupViewSet(ReadOnlyModelViewSet):
    """Представление API для модели Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]


class FollowViewSet(ModelViewSet):
    """Представление API для модели Follow."""

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [filters.SearchFilter,]
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
