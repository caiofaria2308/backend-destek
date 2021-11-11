from django.urls.conf import path
from .views import (
    PriorityList,
    PriorityViewSet,
    TicketList,
    TicketViewSet,
    TicketTrackingList,
    TicketTrackingViewSet,
    TicketEquipmentList,
    TicketEquipmentViewSet,
    TicketTrackingFileList,
    TicketTrackingFileViewSet
)


urlpatterns = [
    path('priority/', PriorityList.as_view()),
    path('priority/<str:id>', PriorityViewSet.as_view()),

    path('ticket/', TicketList.as_view()),
    path('ticket/<str:id>', TicketViewSet.as_view()),

    path('ticket-tracking/', TicketTrackingList().as_view()),
    path('ticket-tracking/<str:id>', TicketTrackingViewSet.as_view()),

    path('ticket-equipment/', TicketEquipmentList.as_view()),
    path('ticket-equipment/<str:id>', TicketEquipmentViewSet.as_view()),

    path('ticket-tracking-file/', TicketTrackingFileList.as_view()),
    path('ticket-tracking-file/<str:id>', TicketTrackingFileViewSet.as_view())
]