import json
import uuid

from django.db import models

from django.forms.models import model_to_dict
from django.utils.encoding import smart_str
from rest_framework import permissions, filters
from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework_jwt import authentication
from rest_framework import permissions


def setup_eager_loading(get_queryset):
    def decorator(self):
        queryset = get_queryset(self)
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset

    return decorator


class UserPermission(permissions.BasePermission):
    """
    Permissão global, checa se o usuário tem acesso ao uma view específica
    """
    message = "Você não tem permissão para executar essa ação"

    def has_permission(self, request, view):
        permission = False

        if hasattr(view, "admin_actions") and request.user:
            # Verifica se o usuário é ADM e tem permisão para realizar uma ação
            # Caso a ação for diferente da bloqueada, permite o acesso
            if (view.action in view.admin_actions and request.user.is_staff) or (
                view.action not in view.admin_actions
            ):
                permission = True

        # Verifica se a view somente permite ser admin
        elif hasattr(view, "is_admin") and request.user and request.user.is_staff:
            permission = True
        # Verifica se a view permite acesso a alguns perfis específicos
        elif hasattr(view,
                     "profile_permission") and request.user and request.user.profile_id in view.profile_permission:
            permission = True
        # Caso não tiver nenhum dos atributos
        elif not hasattr(view, "is_admin") and not hasattr(view, "profile_permission"):
            permission = True

        return permission


class DefaultMixin(object):
    """Configuração default para autenticação, permissões e filtragem"""

    authentication_classes = (
        authentication.JSONWebTokenAuthentication,
    )

    permission_classes = (
        permissions.IsAuthenticated, UserPermission
    )

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
