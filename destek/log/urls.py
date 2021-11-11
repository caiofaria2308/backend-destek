from django.conf.urls import url
from django.urls.conf import path
from .views import (
    LogList,
    LogViewSet
)

urlpatterns = [
    path('', LogList.as_view()),
    path('<str:id>', LogViewSet.as_view())
]
