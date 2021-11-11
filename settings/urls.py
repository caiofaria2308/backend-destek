from django.urls.conf import path
from .views import (
    SettingList,
    SettingViewSet,
    EquipmentList,
    EquipmentViewSet,
    EquipmentTypeList,
    EquipmentTypeViewSet,
    UserList,
    UserViewSet
)


urlpatterns = [
    path("", SettingList.as_view()),
    path('<str:id>', SettingViewSet.as_view()),

    path('equipment/', EquipmentList.as_view()),
    path('quipment/<str:id>', EquipmentViewSet.as_view()),

    path('equipment-type/', EquipmentTypeList.as_view()),
    path('equipment-type/<str:id>', EquipmentTypeViewSet.as_view()),

    path('user/', UserList.as_view()),
    path('user/<int:id>', UserViewSet.as_view()),
]