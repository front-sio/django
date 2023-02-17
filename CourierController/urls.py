from django.urls import path 
from .views import *

urlpatterns = [
    path('', courier_track_view.as_view(), name="courier_track")

]