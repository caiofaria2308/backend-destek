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
    path('settings/<str:id>', SettingViewSet.as_view()),
    path('settings/equipment/<str:id>', EquipmentViewSet.as_view()),
    path('settings/equipment/type/<str:id>', EquipmentTypeViewSet.as_view()),
]