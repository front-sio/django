from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
import barcode
from decimal import *
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File


COURIER_STATUS_CHOICES = (
    ("MANIFATED", "manifested"),
    ("RCS - recieved from shipper", "RCS recieved from shipper"),
    ("OFFLOADED", "offloaded"),
    ("DEPARTED", "departed"),
    ("ON TRANSIT", "on transit"),
    ("ARRIVED", "arrived"),
    ("UNDER CLEARANCE", "under clearance"),
    ("DELIVERED", "derivered"),
)

Type_CHOICES = (
    ("normal goods", "Normal goods"),
    ("express goods", "Express goods"),
    ("shengzen goods", "Shengzen goods"),
)

STATION_CHOICES = (
    ('CAN - Guanzhou', 'CAN - Guanzhou'),
    ('HKG - HongKong', 'HKG - HongKong'),
    ('DAR - Dar es salaam', 'DAR - Dar es salaam'),
    ('DXB - Dubai', 'DXB - Dubai'),
    ('NBO - Nairobi', 'NBO - Nairobi'),
    ('SHJ - Sharjah', 'SHJ - Sharjah'),
    ('JNB - Johanesburg', 'JNB - Johanesburg'),
    ('MCT - Muscat', 'MCT - Muscat'),
    ('BOM - Mumbai', 'BOM - Mumbai'),
    ('ADD - Addis Ababa', 'ADD - Addis Ababa'),
)


class Package(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name="package_creator")
    tracking_key = models.CharField(max_length=18, null=True)
    barcode = models.ImageField(upload_to="couriers/barcode/image/", null=True, blank=True)
    order_number = models.CharField(max_length=8, null=True)
    reciever_name = models.CharField(max_length=100, null=True)
    sender_name = models.CharField(max_length=100, null=True)
    place_from = models.CharField(max_length=100, null=True, choices=STATION_CHOICES)
    destination = models.CharField(max_length=100, null=True, choices=STATION_CHOICES)
    number_of_parcel = models.CharField(max_length=100, null=True)
    kgs = models.CharField(max_length=100, null=True)
    chargable_weight = models.CharField(max_length=100, null=True, blank=True)
    custom_value = models.CharField(max_length=100, null=True, blank=True)
    currency = models.CharField(max_length=100, null=True, blank=True)
    terms = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField( null=True, blank=True)
    insurance = models.CharField(max_length=100, null=True, blank=True)
    chg_code = models.CharField(max_length=100, null=True, blank=True)
    sender_phone = models.CharField(max_length=100, null=True, blank=True)
    sender_address = models.CharField(max_length=100, null=True, blank=True)
    number_of = models.CharField(max_length=100, null=True, blank=True)


    total_amount = models.DecimalField(max_digits=12,null=True, decimal_places=2, blank=True, verbose_name="amount")
    reciever_phone = models.CharField(_("Reciever phone"), max_length=13, null=True)
    
    reciever_address = models.CharField(_("Reciever address"),max_length=100, null=True,)
    date_recieved = models.DateField(_("Date recieved"), null=True, blank=True)
    time_recieved = models.TimeField(_("Date recieved"), null=True, blank=True)
    date_of_stoking_out = models.DateField(_("Date of stocking out"), null=True, blank=True)
    time_of_stoking_out = models.TimeField(_("Date of stocking out"), null=True, blank=True)
    expected_arrival_date = models.DateField(_("Expected arrival date"), null=True, blank=True)
    percel_type = models.CharField(max_length=100, null=True,choices=Type_CHOICES, verbose_name="parcel type")
    has_dimentions = models.BooleanField(null=True, blank=True)
    height = models.IntegerField( null=True, blank=True)
    length = models.IntegerField( null=True, blank=True)
    width = models.IntegerField( null=True, blank=True)
    # status = models.CharField(verbose_name="Courier status",null=True, choices=COURIER_STATUS_CHOICES, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.reciever_name)


    def save(self, *args, **kwargs):
        CODE = barcode.get_barcode_class('code128')
        tracking_key = str(self.tracking_key)
        code = CODE(tracking_key, writer=ImageWriter())
        buffer = BytesIO()
        code.write(buffer)
        File_name = str(self.reciever_name)
        self.barcode.save(File_name+'.jpg', File(buffer), save=False)
        return super().save(*args, **kwargs)



class Parcel(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name="parcel_insertor")
    master_package = models.ForeignKey(Package, null=True, on_delete=models.DO_NOTHING, related_name="parcels")
    tracking_key = models.CharField(max_length=15, null=True)
    mtk = models.CharField(max_length=15, null=True)
    barcode = models.ImageField(upload_to="parcel/barcode/image/", null=True, blank=True)
    master_barcode = models.ImageField(upload_to="parcel/master/barcode/image/", null=True, blank=True)
    place_from = models.CharField(max_length=100, null=True, choices=STATION_CHOICES,)
    destination = models.CharField(max_length=100, null=True, choices=STATION_CHOICES,)
    master_kgs = models.CharField(max_length=15, null=True)
    number_of_parcel = models.CharField(max_length=15, null=True)
    kgs = models.CharField(max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    has_dimentions = models.BooleanField(null=True, blank=True)
    height = models.IntegerField( null=True, blank=True)
    width = models.IntegerField( null=True, blank=True)
    length = models.IntegerField( null=True, blank=True)
    chargable_weight = models.IntegerField( null=True, blank=True)
    number_of = models.CharField(max_length=100, null=True, blank=True)
    # dimensions = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.tracking_key)
    

    def save(self, *args, **kwargs):
        CODE = barcode.get_barcode_class('code128')
        tracking_key = str(self.tracking_key)
        maseter_tracking_key = str(self.mtk)
        code = CODE(tracking_key, writer=ImageWriter())
        mastercode = CODE(maseter_tracking_key, writer=ImageWriter())
        buffer = BytesIO()
        code.write(buffer)
        mastercode.write(buffer)
        File_name = str('parcel_barcode')
        self.barcode.save(File_name+'.jpg', File(buffer), save=False)
        self.master_barcode.save(File_name+'.jpg', File(buffer), save=False)
        return super().save(*args, **kwargs)


class ExtraPackageInfo(models.Model):
    package = models.ForeignKey(Package, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="extraPackInfo")
    status = models.CharField(verbose_name="Courier status", null=True, choices=COURIER_STATUS_CHOICES, max_length=50)
    date = models.DateField(_("Date"), auto_now_add=True, null=True, blank=True)
    time = models.TimeField(_("Time"),auto_now=True, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    terminal = models.CharField(max_length=100, null=True, choices=STATION_CHOICES)

    def __str__(self):
        return str(self.terminal)


class ExtraParcelInfo(models.Model):
    package  = models.ForeignKey(Parcel, null=True, blank=True, on_delete=models.DO_NOTHING)
    status = models.CharField(verbose_name="Courier status", null=True, choices=COURIER_STATUS_CHOICES, max_length=50)
    date = models.DateField(_("Date recieved"), null=True, blank=True)
    time = models.TimeField(_("Date recieved"), null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    terminal = models.CharField(max_length=100, null=True, choices=STATION_CHOICES)


    def __str__(self):
        return str(self.terminal)
    

