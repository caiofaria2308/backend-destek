from typing import List
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView
from defaults import DefaultMixin
from log.models import Log
from log.serializers import LogSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework.request import Request


class LogList(DefaultMixin, ListAPIView):
    queryset = Log.objects.all().order_by('created_at').reverse()
    serializer_class = LogSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = [
        'user',
        'type',
        'primary_key'
    ]


class LogViewSet(DefaultMixin, ListAPIView):
    queryset = Log.objects.all().order_by('created_at').reverse()
    serializers_class = LogSerializer
    
    
    def get(self, request: Request, *args, **kwargs):
       try:
            obj = get_object_or_404(
                Log,
                pk=kwargs.get('id', 0)
            )
            serializer = LogSerializer(obj, many=True)
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
            
    
    def put(self, request: Request, *args, **kwargs):
        try:
            with transaction.atomic():
                obj = get_object_or_404(
                    Log,
                    pk=kwargs.get('id')
                )
                data = dict(request.data)
                for key, value in data.items():
                    setattr(obj, key, value)
                obj.save()
                serializer = LogSerializer(obj)
                serializer.update(obj, data)
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
    