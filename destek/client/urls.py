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
    path('', ClientList.as_view()),
    path('<str:id>', ClientViewSet.as_view()),

    path('equipment/', EquipmentList.as_view()),
    path('equipment/<str:id>', EquipmentViewSet.as_view()),

    path('telephone/', TelephoneList.as_view()),
    path('telephone/<str:id>', TelephoneViewSet.as_view()),

    path('address/', AddressList.as_view()),
    path('address/<str:id>', AddressViewSet.as_view()),
    
    path('observation/', ObservationList.as_view()),
    path('observation/<str:id>', ObservationViewSet.as_view())
]
