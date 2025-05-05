from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)

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


class GroupViewSet(ReadOnlyModelViewSet):
    """Представление API для модели Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]


class FollowViewSet(ModelViewSet):
    """Представление API для модели Follow."""

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated,]
