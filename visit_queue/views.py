from django.db import transaction
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from rest_framework import filters
from defaults import DefaultMixin
from rest_framework.generics import ListAPIView, get_object_or_404

from iticket.serializers import TicketSerializer
from .models import (
    Vacation,
    Type,
    VisitQueue
)
from .serializers import (
    VacationSerializer,
    TypeSerializer,
    VisitQueueSerializer
)
from log.serializers import LogSerializer
from destek.settings import SECRET_KEY
import jwt


class VacationList(DefaultMixin, ListAPIView):
    queryset = Vacation.objects.all().order_by('final_date').reverse()
    serializer_class = VacationSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = [
        'user'
    ]
    
    
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                if request.data:
                    serializer = VacationSerializer(data=dict(request.data))
                    if serializer.is_valid():
                        serializer.save()
                        user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                        log = LogSerializer(data = {
                            'user_id': user.get('user_id'),
                            'table': 'visit_queue_vacation',
                            'primary_key': serializer.data.get('id'),
                            'data': serializer.data,
                            'type': 0
                        })
                        log.save() if log.is_valid() else None
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class VacationViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_object_or_404(
                VisitQueue,
                pk=kwargs.get('id')
            )
            serializer = VacationSerializer(obj)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def put(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Vacation,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.save()
                serializer = VacationSerializer(obj)
                serializer.update(obj, data)
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'visit_queue_vacation',
                    'primary_key': serializer.data.get('id'),
                    'data': serializer.data,
                    'type': 1
                })
                log.save() if log.is_valid() else None
                return Response(
                        serializer.data,
                        status=status.HTTP_200_OK
                    )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        
    def delete(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Vacation,
                    pk=kwargs.get('id')
                )
                obj.delete()
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'visit_queue_vacation',
                    'primary_key': kwargs.get('id'),
                    'data': {},
                    'type': 1
                })
                log.save() if log.is_valid() else None
                return Response(
                    {
                        'detail': f'Vacation deleted'
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
class TypeList(DefaultMixin, ListAPIView):
    queryset = Type.objects.all().order_by('name')
    serializer_class = TypeSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        '$name'
    ]


    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                if request.data:
                    serializer = TypeSerializer(data=dict(request.data))
                    if serializer.is_valid():
                        serializer.save()
                        user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                        log = LogSerializer(data = {
                            'user_id': user.get('user_id'),
                            'table': 'visit_queue_type',
                            'primary_key': serializer.data.get('id'),
                            'data': serializer.data,
                            'type': 0
                        })
                        log.save() if log.is_valid() else None
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TypeViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_object_or_404(
                Type,
                pk=kwargs.get('id')
            )
            serializer = TypeSerializer(obj)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def put(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Type,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.save()
                serializer = TypeSerializer(obj)
                serializer.update(obj, data)
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'visit_queue_type',
                    'primary_key': serializer.data.get('id'),
                    'data': serializer.data,
                    'type': 1
                })
                log.save() if log.is_valid() else None
                return Response(
                        serializer.data,
                        status=status.HTTP_200_OK
                    )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        
    def delete(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Type,
                    pk=kwargs.get('id')
                )
                obj.delete()
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'visit_queue_type',
                    'primary_key': kwargs.get('id'),
                    'data': {},
                    'type': 1
                })
                log.save() if log.is_valid() else None
                return Response(
                    {
                        'detail': f'Type File deleted'
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
class VisitQueueList(DefaultMixin, ListAPIView):
    queryset = VisitQueue.objects.all().order_by('visit_date').reverse()
    serializer_class = VisitQueueSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = [
        'user',
        'client',
        'type'
    ]


    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                if request.data:
                    serializer = VisitQueueSerializer(data=dict(request.data))
                    if serializer.is_valid():
                        serializer.save()
                        user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                        log = LogSerializer(data = {
                            'user_id': user.get('user_id'),
                            'table': 'visit_queue_visitqueue',
                            'primary_key': serializer.data.get('id'),
                            'data': serializer.data,
                            'type': 0
                        })
                        log.save() if log.is_valid() else None
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class VisitQueueViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_object_or_404(
                VisitQueue,
                pk=kwargs.get('id')
            )
            serializer = VisitQueueSerializer(obj)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def put(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    VisitQueue,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.save()
                serializer = VisitQueueSerializer(obj)
                serializer.update(obj, data)
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'visit_queue_visitqueue',
                    'primary_key': serializer.data.get('id'),
                    'data': serializer.data,
                    'type': 1
                })
                log.save() if log.is_valid() else None
                return Response(
                        serializer.data,
                        status=status.HTTP_200_OK
                    )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        
    def delete(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    VisitQueue,
                    pk=kwargs.get('id')
                )
                obj.delete()
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'visit_queue_visitqueue',
                    'primary_key': kwargs.get('id'),
                    'data': {},
                    'type': 1
                })
                log.save() if log.is_valid() else None
                return Response(
                    {
                        'detail': f'Visit queue deleted'
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
