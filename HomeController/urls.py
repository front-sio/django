from django.urls import path 
from django.http import HttpResponse
from django.views import View

from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),

    # tracking views here
    path('courier/', Index, name="courier"),
    path('courier/<str:pk>/courier_detail', CourierInfo, name="courier_detail"),
    # services views here
    path('about/us/', About_us_view, name="about"),
    path('contact/us/', Contact_Us, name="contact"),
    path('services/', Our_Services, name="services"),
]