from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from defaults import DefaultMixin
from rest_framework.generics import get_object_or_404

from .serializers import (
    SettingSerializer,
    EquipmentSerializer,
    EquipmentTypeSerializer
)
from .models import (
    Setting,
    Equipment,
    EquipmentType
)


class SettingList(DefaultMixin, ListAPIView):
    filterset_fields = ['label']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer


    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                if request.data:
                    serializer = SettingSerializer(data=dict(request.data))
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class SettingViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_object_or_404(Setting, pk=kwargs.get('id'))
            serializer = SettingSerializer(obj, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def put(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(Setting, pk=kwargs.get('id'))
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.save()
                serializer = SettingSerializer(obj)
                serializer.update(obj, data)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def delete(self, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(Setting, pk=kwargs.get('id'))
                obj.delete()
                return Response(
                    {
                        'detail': f'Setting deleted'
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class EquipmentList(DefaultMixin, ListAPIView):
    search_fields = ['$brand', '$model']
    filterset_fields = ['type']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                if request.data:
                    serializer = EquipmentSerializer(data=dict(request.data))
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class EquipmentViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_object_or_404(Equipment, pk=kwargs.get('id'))
            serializer = EquipmentSerializer(obj, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def put(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(Equipment, pk=kwargs.get('id'))
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.save()
                serializer = EquipmentSerializer(obj)
                serializer.update(obj, data)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def delete(self, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(Equipment, pk=kwargs.get('id'))
                obj.delete()
                return Response(
                    {
                        'detail': f'Equipment deleted'
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class EquipmentTypeList(DefaultMixin, ListAPIView):
    search_fields = ['$type']
    filter_backends = (filters.SearchFilter,)
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer


    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                if request.data:
                    serializer = EquipmentTypeSerializer(data=dict(request.data))
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class EquipmentTypeViewSet(DefaultMixin, APIView):
    def get(self, request, *args, **kwargs):
        try:
            obj = get_object_or_404(EquipmentType, pk=kwargs.get('id'))
            serializer = EquipmentTypeSerializer(obj, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def put(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(EquipmentType, pk=kwargs.get('id'))
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.save()
                serializer = EquipmentTypeSerializer(obj)
                serializer.update(obj, data)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def delete(self, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(EquipmentType, pk=kwargs.get('id'))
                obj.delete()
                return Response(
                    {
                        'detail': f'EquipmentType deleted'
                    },
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
