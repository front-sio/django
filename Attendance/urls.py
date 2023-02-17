from django.urls import path
from .views import *
urlpatterns = [
    path('', attendance_list.as_view(), name="attendance_list")
]