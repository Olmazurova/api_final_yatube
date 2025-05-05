from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import AuthorOrReadOnly


class AuthorFieldMixin(serializers.ModelSerializer):
    """Миксин настраивает поле автора."""

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )


class PermissionMixin:
    """Миксин добавляет permission_classes во вьюсет."""

    permission_classes = [IsAuthenticatedOrReadOnly, AuthorOrReadOnly,]