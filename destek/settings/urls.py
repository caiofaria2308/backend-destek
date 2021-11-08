from django.urls.conf import path
from .views import (
    SettingList,
    SettingViewSet,
    EquipmentList,
    EquipmentViewSet,
    EquipmentTypeList,
    EquipmentTypeViewSet
)


urlpatterns = [
    path("settings/", SettingList.as_view()),
    path('settings/<str:id>', SettingViewSet.as_view()),

    path('settings-equipment/', EquipmentList.as_view()),
    path('settings-equipment/<str:id>', EquipmentViewSet.as_view()),

    path('settings-equipment-type/', EquipmentTypeList.as_view()),
    path('settings-equipment-type/<str:id>', EquipmentTypeViewSet.as_view()),
]