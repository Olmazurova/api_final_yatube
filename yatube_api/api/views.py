from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Comment, Group, Follow
from .serializers import (CommentSerializer, PostSerializer,
                          GroupSerializer, FollowSerializer)


class PostViewSet(ModelViewSet):
    """Представление API для модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination


class CommentViewSet(ModelViewSet):
    """Представление API для модели Comment."""

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs.get('post_id'))


class GroupViewSet(ReadOnlyModelViewSet):
    """Представление API для модели Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(ModelViewSet):
    """Представление API для модели Follow."""

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
