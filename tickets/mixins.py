"""Модуль вьюсетов для билетов и регистрации."""

from rest_framework import viewsets, mixins


class RetrieveDestroyViewSet(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Вьюсет на чтение, удаление."""
    pass
