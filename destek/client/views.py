from django.db import transaction
from django.shortcuts import render
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import filters
from defaults import DefaultMixin
from rest_framework.generics import ListAPIView, get_object_or_404

from .models import (
    Client,
    Telephone,
    Address,
    Observation,
    Equipment
)

from .serializers import (
    ClientSerializer,
    TelephoneSerializer,
    AddressSerializer,
    ObservationSerializer,
    EquipmentSerializer
)


class ClientList(DefaultMixin, ListAPIView, viewsets.ModelViewSet, APIView):
    queryset = Client.objects.all().order_by('is_active')
    serializer_class = ClientSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = [
        '$corporate_name',
        '$fantasy_name',
        '^main_document',
        '^secondary_document',
        '^reference_code'
    ]


class ClientViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_object_or_404(
                Client,
                pk=kwargs.get('id')
            )
            serializer = ClientSerializer(obj)
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
                    Client,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.save()
                serializer = ClientSerializer(obj)
                serializer.update(obj, data)
                return Response(
                        serializer.data,
                        status=status.HTTP_200_OK
                    )
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        
    def delete(self, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Client,
                    pk=kwargs.get('id')
                )
                obj.delete()
                return Response(
                    {
                        'detail': f'Client deleted'
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TelephoneList(DefaultMixin, ListAPIView, viewsets.ModelViewSet):
    queryset = Telephone.objects.all().order_by('is_active')
    serializer_class = TelephoneSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = [
        'client'
    ]
    search_fields = [
        '$telephone'
    ]
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)


class TelephoneViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_object_or_404(
                Telephone,
                pk=kwargs.get('id')
            )
            serializer = TelephoneSerializer(obj)
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
                    Telephone,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                serializer = TelephoneSerializer(obj)
                serializer.update(obj, data)
                obj.save()
                return Response(
                        serializer.data,
                        status=status.HTTP_200_OK
                    )
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        
    def delete(self, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Telephone,
                    pk=kwargs.get('id')
                )
                obj.delete()
                return Response(
                    {
                        'detail': f'Telephone deleted'
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AddressList(DefaultMixin, ListAPIView, viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('zip_code')
    serializer_class = AddressSerializer
    filterset_fields = [
        'client'
    ]
    search_fields = [
        '^zip_code',
        '$address',
        '=city'
    ]


class AddressViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Address,
                    pk=kwargs.get('id')
                )
                serializer = AddressSerializer(obj)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def put(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Address,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                serializer = AddressSerializer(obj)
                serializer.update(obj, data)
                obj.save()
                return Response(
                        serializer.data,
                        status=status.HTTP_200_OK
                    )
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def delete(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Address,
                    pk=kwargs.get('id')
                )
                obj.delete()
                return Response(
                    {"detail": "Deleted with successful"},
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ObservationList(DefaultMixin, ListAPIView, viewsets.ModelViewSet):
    queryset = Observation.objects.all().order_by('title')
    serializer_class = ObservationSerializer
    filterset_fields = [
        'client'
    ]
    search_fields = [
        '$title',
        '$information'
    ]


class ObservationViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Observation,
                    pk=kwargs.get('id')
                )
                serializer = ObservationSerializer(obj)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def put(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Observation,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                serializer = ObservationSerializer(obj)
                serializer.update(obj, data)
                obj.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def delete(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Observation,
                    pk=kwargs.get('id')
                )
                obj.delete()
                return Response(
                    {"detail": "Deleted with successful"},
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class EquipmentList(DefaultMixin, ListAPIView, viewsets.ModelViewSet):
    queryset = Equipment.objects.all().order_by('created_at')
    serializer_class = EquipmentSerializer
    filterset_fields = [
        'client',
        'equipment'
    ]
    search_fields = [
        
    ]


class EquipmentViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Equipment,
                    pk=kwargs.get('id')
                )
                serializer = EquipmentSerializer(obj)
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def put(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Equipment,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                serializer = EquipmentSerializer(obj)
                serializer.update(obj, data)
                obj.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def delete(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Equipment,
                    pk=kwargs.get('id')
                )
                obj.delete()
                return Response(
                    {"detail": "Deleted with successful"},
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
