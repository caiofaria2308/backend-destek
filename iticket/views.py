from django.db import transaction
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from defaults import DefaultMixin
from rest_framework.generics import ListAPIView, get_object_or_404
from .models import (
    Priority,
    Ticket,
    TicketEquipment,
    TicketTracking,
    TicketTrackingFile
)
from .serializers import (
    PrioritySerializer,
    TicketSerializer,
    TicketEquipmentSerializer,
    TicketTrackingSerializer,
    TicketTrackingFileSerializer
)

from log.serializers import LogSerializer
from destek.settings import SECRET_KEY
import jwt


class PriorityList(DefaultMixin, ListAPIView):
    queryset = Priority.objects.all().order_by('name')
    serializer_class = PrioritySerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        '$name',
        '$color'
    ]


    def post(self, request: Request, *args, **kwargs):
        try:
            with transaction.atomic():
                if request.data:
                    serializer = PrioritySerializer(data=dict(request.data))
                    if serializer.is_valid():
                        serializer.save()
                        user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                        log = LogSerializer(data = {
                            'user_id': user.get('user_id'),
                            'table': 'iticket_priority',
                            'primary_key': kwargs.get('id'),
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


class PriorityViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_object_or_404(
                Priority,
                pk=kwargs.get('id')
            )
            serializer = PrioritySerializer(obj)
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
                    Priority,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.save()
                serializer = PrioritySerializer(obj)
                serializer.update(obj, data)
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'iticket_priority',
                    'primary_key': kwargs.get('id'),
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
                    Priority,
                    pk=kwargs.get('id')
                )
                obj.delete()
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'iticket_priority',
                    'primary_key': kwargs.get('id'),
                    'data': {},
                    'type': 2
                })
                log.save() if log.is_valid() else None
                return Response(
                    {
                        'detail': f'Priority deleted'
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TicketList(DefaultMixin, ListAPIView):
    queryset = Ticket.objects.all().order_by('created_at').reverse()
    serializer_class = TicketSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        '$title'
    ]
    filterset_fields = [
        'status',
        'user_id',
        'unique_code'
    ]


    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                if request.data:
                    serializer = TicketSerializer(data=dict(request.data))
                    if serializer.is_valid():
                        serializer.save()
                        user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                        log = LogSerializer(data = {
                            'user_id': user.get('user_id'),
                            'table': 'iticket_ticket',
                            'primary_key': kwargs.get('id'),
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


class TicketViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_object_or_404(
                Ticket,
                pk=kwargs.get('id')
            )
            serializer = TicketSerializer(obj)
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
                    Ticket,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.save()
                serializer = TicketSerializer(obj)
                serializer.update(obj, data)
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'iticket_ticket',
                    'primary_key': kwargs.get('id'),
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
                    Ticket,
                    pk=kwargs.get('id')
                )
                obj.delete()
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'iticket_ticket',
                    'primary_key': kwargs.get('id'),
                    'data': {},
                    'type': 2
                })
                log.save() if log.is_valid() else None
                return Response(
                    {
                        'detail': f'Ticket deleted'
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TicketEquipmentList(DefaultMixin, ListAPIView):
    queryset = TicketEquipment.objects.all().order_by('updated_at')
    serializer_class = TicketEquipmentSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = [
        'equipment',
        'ticket'
    ]


    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                if request.data:
                    serializer = TicketEquipmentSerializer(data=dict(request.data))
                    if serializer.is_valid():
                        serializer.save()
                        user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                        log = LogSerializer(data = {
                            'user_id': user.get('user_id'),
                            'table': 'iticket_ticketequipment',
                            'primary_key': kwargs.get('id'),
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


class TicketEquipmentViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_object_or_404(
                TicketEquipment,
                pk=kwargs.get('id')
            )
            serializer = TicketEquipmentSerializer(obj)
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
                    TicketEquipment,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.save()
                serializer = TicketEquipmentSerializer(obj)
                serializer.update(obj, data)
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'iticket_ticketequipment',
                    'primary_key': kwargs.get('id'),
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
                    TicketEquipment,
                    pk=kwargs.get('id')
                )
                obj.delete()
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'iticket_ticketequipment',
                    'primary_key': kwargs.get('id'),
                    'data': {},
                    'type': 2
                })
                log.save() if log.is_valid() else None
                return Response(
                    {
                        'detail': f'TicketEquipment deleted'
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TicketTrackingList(DefaultMixin, ListAPIView):
    queryset = TicketTracking.objects.all().order_by('updated_at')
    serializer_class = TicketTrackingSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = [
        'ticket',
        'user_id',
        'status'
    ]


    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                if request.data:
                    serializer = TicketTrackingSerializer(data=dict(request.data))
                    if serializer.is_valid():
                        serializer.save()
                        user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                        log = LogSerializer(data = {
                            'user_id': user.get('user_id'),
                            'table': 'iticket_tickettracking',
                            'primary_key': kwargs.get('id'),
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


class TicketTrackingViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_object_or_404(
                TicketTracking,
                pk=kwargs.get('id')
            )
            serializer = TicketTrackingSerializer(obj)
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
                    TicketTracking,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.save()
                serializer = TicketTrackingSerializer(obj)
                serializer.update(obj, data)
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'iticket_tickettracking',
                    'primary_key': kwargs.get('id'),
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
                    TicketTracking,
                    pk=kwargs.get('id')
                )
                obj.delete()
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'iticket_tickettracking',
                    'primary_key': kwargs.get('id'),
                    'data': {},
                    'type': 2
                })
                log.save() if log.is_valid() else None
                return Response(
                    {
                        'detail': f'Ticket Tracking deleted'
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TicketTrackingFileList(DefaultMixin, ListAPIView):
    queryset = TicketTrackingFile.objects.all().order_by('updated_at')
    serializer_class = TicketTrackingFileSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = [
        'ticket_tracking'
    ]


    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                if request.data:
                    serializer = TicketTrackingFileSerializer(data=dict(request.data))
                    if serializer.is_valid():
                        serializer.save()
                        user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                        log = LogSerializer(data = {
                            'user_id': user.get('user_id'),
                            'table': 'iticket_tickettrackingfile',
                            'primary_key': kwargs.get('id'),
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


class TicketTrackingFileViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_object_or_404(
                TicketTrackingFile,
                pk=kwargs.get('id')
            )
            serializer = TicketTrackingFileSerializer(obj)
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
                    TicketTrackingFile,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.save()
                serializer = TicketTrackingFileSerializer(obj)
                serializer.update(obj, data)
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'iticket_tickettrackingfile',
                    'primary_key': kwargs.get('id'),
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
                    TicketTrackingFile,
                    pk=kwargs.get('id')
                )
                obj.delete()
                user = jwt.decode(
                            request.auth,
                            SECRET_KEY
                        )
                log = LogSerializer(data = {
                    'user_id': user.get('user_id'),
                    'table': 'iticket_tickettrackingfile',
                    'primary_key': kwargs.get('id'),
                    'data': {},
                    'type': 1
                })
                log.save() if log.is_valid() else None
                return Response(
                    {
                        'detail': f'Ticket Tracking File deleted'
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
