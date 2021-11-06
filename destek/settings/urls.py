from django.urls.conf import path
from .views import SettingList, SettingViewSet


urlpatterns = [
    path('settings/', SettingList.as_view()),
    path('settings/<str:id>', SettingViewSet.as_view())
]