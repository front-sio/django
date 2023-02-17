from django import forms
from django.forms import ModelForm
from django.forms.utils import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from CourierController.models import Package, Parcel
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

from django.forms import widgets
from .models import *
from CourierController.models import *
from CourierController.models import ExtraPackageInfo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class PackageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PackageForm, self).__init__(*args, **kwargs)
        self.fields['tracking_key'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Press load key button to load tracking key'
        }
        self.fields['order_number'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Press load key button to load key'
        }
        self.fields['place_from'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'From'
        }
        self.fields['destination'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Destination'
        }
        self.fields['sender_name'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Sender name'
        }
        self.fields['sender_phone'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Sender phone'
        }
        self.fields['sender_address'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Sender address'
        }

        self.fields['reciever_name'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Reciever name'
        }
        self.fields['reciever_address'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter reciever address'
        }
        self.fields['reciever_phone'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter reciever phone'
        }
        self.fields['number_of_parcel'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'N.O.P'
        }
        self.fields['kgs'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Actual weight'
        }
        self.fields['custom_value'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Custom value (OPTIONAL)'
        }
        self.fields['terms'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter terms (OPTIONAL)'
        }
        self.fields['desc'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter desc (OPTIONAL)'
        }
        self.fields['currency'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter currency (e.g USD)'
        }
        self.fields['chg_code'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter C.H.G code (OPTIONAL)'
        }
        self.fields['chargable_weight'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter C.W'
        }
        self.fields['insurance'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter insurance'
        }
        self.fields['date_recieved'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter date recieved'
        }
        self.fields['percel_type'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter parcel type'
        }
        self.fields['expected_arrival_date'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter expected arrival date'
        }
    class Meta:
        model = Package
        fields = [
            'tracking_key',
            'order_number',
            'place_from',
            'destination',
            'sender_name', 
            'sender_phone',
            'sender_address',
            'reciever_name',
            'reciever_address',
            'insurance',
            'reciever_phone',
            'number_of_parcel',
            'kgs',
            'custom_value',
            'terms',
            'desc',
            'currency',
            'chg_code',
            'chargable_weight',
            'date_recieved',
            'percel_type',
            'expected_arrival_date',
            ]
        exclude = ['user', 'date_of_stoking_out', 'total_amount']

        widgets = {
            'date_recieved' :  DatePickerInput(),
            'expected_arrival_date' :  DatePickerInput(),
            
        }

# package update
class PackageUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PackageUpdateForm, self).__init__(*args, **kwargs)
        self.fields['tracking_key'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Press load key button to load tracking key'
        }
        self.fields['order_number'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Press load key button to load key'
        }
        self.fields['place_from'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'From'
        }
        self.fields['destination'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Destination'
        }
        self.fields['sender_name'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Sender name'
        }
        self.fields['sender_phone'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Sender phone'
        }
        self.fields['sender_address'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Sender address'
        }

        self.fields['reciever_name'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Reciever name'
        }
        self.fields['reciever_address'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter reciever address'
        }
        self.fields['reciever_phone'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter reciever phone'
        }
        self.fields['number_of_parcel'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'N.O.P'
        }
        self.fields['kgs'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Actual weight'
        }
        self.fields['custom_value'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Custom value (OPTIONAL)'
        }
        self.fields['terms'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter terms (OPTIONAL)'
        }
        self.fields['desc'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter desc (OPTIONAL)'
        }
        self.fields['currency'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter currency (e.g USD)'
        }
        self.fields['chg_code'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter C.H.G code (OPTIONAL)'
        }
        self.fields['chargable_weight'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter C.W'
        }
        self.fields['insurance'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter Insurance (OPTIONAL)'
        }
        self.fields['date_recieved'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter date recieved'
        }
        self.fields['percel_type'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter parcel type'
        }
        self.fields['expected_arrival_date'].widget.attrs = {
            'class': 'form-control col-md-6',
            'placeholder': 'Enter expected arrival date'
        }
    class Meta:
        model = Package
        fields = [
            'tracking_key',
            'order_number',
            'place_from',
            'destination',
            'sender_name', 
            'sender_phone',
            'sender_address',
            'reciever_name',
            'reciever_address',
            'reciever_phone',
            'number_of_parcel',
            'kgs',
            'custom_value',
            'terms',
            'desc',
            'currency',
            'insurance',
            'chg_code',
            'chargable_weight',
            'date_recieved',
            'percel_type',
            'expected_arrival_date',
        ]



# parcel form
class ParcelForm(ModelForm):
    class Meta:
        model = Parcel
        fields = '__all__'
        exclude = ['mtk', 'master_kgs', 'has_dimentions', 'master_package', 'user', 'height', 'width', 'length']



# parcel Update
class ParcelUpdateForm(ModelForm):
    class Meta:
        model = Parcel
        fields = '__all__'






#Form Layout from Crispy Forms



# class DateInput(forms.DateInput):
#     input_type = 'date'

# class InvoiceForm(forms.ModelForm):
#     THE_OPTIONS = [
#     ('14 days', '14 days'),
#     ('30 days', '30 days'),
#     ('60 days', '60 days'),
#     ]
#     STATUS_OPTIONS = [
#     ('CURRENT', 'CURRENT'),
#     ('OVERDUE', 'OVERDUE'),
#     ('PAID', 'PAID'),
#     ]

#     title = forms.CharField(
#                     required = True,
#                     label='Invoice Name or Title',
#                     widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Invoice Title'}),)
#     paymentTerms = forms.ChoiceField(
#                     choices = THE_OPTIONS,
#                     required = True,
#                     label='Select Payment Terms',
#                     widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
#     status = forms.ChoiceField(
#                     choices = STATUS_OPTIONS,
#                     required = True,
#                     label='Change Invoice Status',
#                     widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
#     notes = forms.CharField(
#                     required = True,
#                     label='Enter any notes for the client',
#                     widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))

#     dueDate = forms.DateField(
#                         required = True,
#                         label='Invoice Due',
#                         widget=DateInput(attrs={'class': 'form-control mb-3'}),)


#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Row(
#                 Column('title', css_class='form-group col-md-6'),
#                 Column('dueDate', css_class='form-group col-md-6'),
#                 css_class='form-row'),
#             Row(
#                 Column('paymentTerms', css_class='form-group col-md-6'),
#                 Column('status', css_class='form-group col-md-6'),
#                 css_class='form-row'),
#             'notes',

#             Submit('submit', ' EDIT INVOICE '))

#     class Meta:
#         model = Invoice
#         fields = ['title', 'dueDate', 'paymentTerms', 'status', 'notes']



class createExtraPackageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(createExtraPackageForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['terminal'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['note'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        
    class Meta:
        model = ExtraPackageInfo
        fields = ['status', 'terminal', 'note']

class createExtraParcelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(createExtraParcelForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['terminal'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['note'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        
    class Meta:
        model = ExtraParcelInfo
        fields = ['status', 'terminal', 'note']

class createUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(createUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['first_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['last_name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['password1'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['password2'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'password1', 'password2']
