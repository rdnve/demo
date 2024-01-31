from django.urls import path

from .views import get_weekday

urlpatterns = [path("<str:weekday>/", get_weekday)]
