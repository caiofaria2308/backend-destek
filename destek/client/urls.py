from django.urls.conf import path
from .views import (
    ClientList,
    ClientViewSet,
    EquipmentList,
    EquipmentViewSet,
    TelephoneList,
    TelephoneViewSet,
    AddressList,
    AddressViewSet,
    ObservationList,
    ObservationViewSet
)

urlpatterns = [
    path('client/<str:id>', ClientViewSet.as_view()),
    path('client/equipment/<str:id>', EquipmentViewSet.as_view()),
    path('client/telephone/<str:id>', TelephoneViewSet.as_view()),
    path('client/address/<str:id>', AddressViewSet.as_view()),
    path('client/observation/<str:id>', ObservationViewSet.as_view())
]
