from django.urls import path 
from .views import *

urlpatterns = [
    path('', dashboard, name="Admin"),

    
    path('courier/shengzen_goods/', shengzen_view, name="shengzen_goods"),
    path('courier/express_goods/', express_view, name="express_goods"),
    path('courier/normal_goods/', normal_view, name="normal_goods"),
    path('courier/received/', received_view, name="received"),
    path('courier/delivered/', delivered_view, name="delivered"),
    path('courier/arival/', arrival_view, name="arrival"),



    path('couriers/', courier_list_view, name="courier_list"),
    path('couriers/parcel/list/<str:pk>/', parcel_lits_view, name="view_package"),
    # path('courier/<str:pk>/detail/', courierDetailView, name="courier_detail"),
    path('courier/create/', CourierCreateView, name="courier_create"),
    path('courier/<str:pk>/update/', PackageUpdateView, name="courier_update"),
    # path('courier/<str:pk>/update/', CourierUpdateView, name="courier_update"),
    # path('courier/<str:pk>/delete/', CourierDeleteView, name="courier_delete"),


    # parcel 
    path('parcel/<str:pk>/create/', ParcelCreateView, name="parcel_create"),
    path('parcel/<str:pk>/update/', ParcelUpdateView, name="parcel_update"),
   
    path('parcel/<str:parcel_id>/', addExtraParcelInfo, name="extra_parcel_detail"),
    path('package/<str:package_id>/', addExtraPackageInfo, name="extra_pack_detail"),



    path('search_result/', search_result, name="search_result"),
   






    # printing url 
    path('package/<str:pk>/print/', prinArea, name="package_print"),

   

    # users url pages
    path('accounts/create/', userCreation, name="create_user"),
   

   
    path('accounts/users/', users, name="users"),
    

]