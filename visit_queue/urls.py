from django.urls.conf import path
from .views import (
    VacationList,
    VacationViewSet,
    TypeList,
    TypeViewSet,
    VisitQueueViewSet,
    VisitQueueList
)


urlpatterns = [
    path('vacation/', VacationList.as_view()),
    path('vacation/<str:id>', VacationViewSet.as_view()),
    
    path('type/', TypeList.as_view()),
    path('type/<str:id>', TypeViewSet.as_view()),
    
    path('visit-queue/', VisitQueueList.as_view()),
    path('visit-queue/<str:id>', VisitQueueViewSet.as_view())
]
