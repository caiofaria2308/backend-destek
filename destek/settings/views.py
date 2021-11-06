import json
from typing import List
from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework import serializers
from rest_framework import response
import rest_framework
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from defaults import DefaultMixin
from rest_framework.generics import get_object_or_404

from .serializers import SettingSerializer
from .models import Setting


class SettingList(DefaultMixin, ListAPIView, APIView):
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
