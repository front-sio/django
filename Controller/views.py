from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from PIL import Image 
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import (PackageForm, 
                    ParcelForm, 
                    ParcelUpdateForm, 
                    PackageUpdateForm,
                    createUserForm,
                    createExtraParcelForm
                    )
from CourierController.models import Package, Parcel, ExtraPackageInfo



from django.http import JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from PIL import Image
from datetime import date
from datetime import datetime, timedelta, time
import random
# Create your views here.

current_path = os.path.dirname(__file__)

# @method_decorator(login_required, name='dispatch')



# class CourierCreateView(CreateView):
#     model = Package
#     template_name = 'Controller/Courier/create.html'
#     fields = '__all__'
#     success_url = reverse_lazy('courier_list')

# class ParcelCreateView(CreateView):
#     model = Parcel
#     template_name = 'Controller/Parcel/create.html'
#     fields = '__all__'
#     success_url = reverse_lazy('courier_list')



@login_required
def CourierCreateView(request):
        form = PackageForm()
        context = {
            'form': form
        }
        if request.POST:
            sender_name = request.POST['sender_name']
            tracking_key = request.POST['tracking_key']
            order_number = request.POST['order_number']
            number_of_parcel = request.POST['number_of_parcel']
            kgs = request.POST['kgs']
            sender_phone = request.POST['sender_phone']
            sender_address = request.POST['sender_address']
            reciever_phone = request.POST['reciever_phone']
            reciever_name = request.POST['reciever_name']
            currency = request.POST['currency']
            terms = request.POST['terms']
            reciever_address = request.POST['reciever_address']
            place_from = request.POST['place_from']
            destination = request.POST['destination']
            date_recieved = request.POST['date_recieved']
            chargable_weight = request.POST['chargable_weight']
            custom_value = request.POST['custom_value']
            chg_code = request.POST['chg_code']
            desc = request.POST['desc']
            insurance = request.POST['insurance']
            expected_arrival_date = request.POST['expected_arrival_date']
            percel_type = request.POST['percel_type']
        
            user = request.user
           

            package = Package.objects.create(
                
                insurance=insurance,
                 
                number_of_parcel=number_of_parcel,
                kgs=kgs,
                custom_value=custom_value,
         
                date_recieved=date_recieved,
                expected_arrival_date=expected_arrival_date,
                chargable_weight=chargable_weight,
                chg_code=chg_code,
                currency=currency,
                sender_address=sender_address,
                sender_name=sender_name,
                sender_phone=sender_phone,
                terms=terms,
                desc=desc,
                percel_type = percel_type,
                user = user,
                tracking_key=tracking_key,
                order_number=order_number,
                place_from=place_from, destination=destination,
                )
            package.save()
            return redirect('courier_list')
        return render(request, 'Controller/Courier/create.html', context)




@login_required
def ParcelCreateView(request, pk):
    package = Package.objects.get(id = pk)
    form = ParcelForm()
    
    
    context = {
        'form': form,
        'package': package
        }
    if request.POST:
        mtk = package.tracking_key
        master_kgs = package.kgs
        master_package = package
        user = request.user
        kgs = request.POST['kgs']
        # status = request.POST['status']
        place_from = request.POST['place_from']
        number_of_parcel = request.POST['number_of_parcel']
        destination = request.POST['destination']
        tracking_key = request.POST['tracking_key']
      

        parcel = Parcel.objects.create(mtk=mtk, number_of_parcel=number_of_parcel, user=user,place_from=place_from, destination=destination, tracking_key=tracking_key, master_package=master_package, master_kgs=master_kgs, kgs=kgs)

        parcel.save()   
        # return redirect('courier_list')
        return redirect('view_package', package.id)
        

    return render(request, 'Controller/Parcel/create.html', context)

@login_required
def PackageUpdateView(request, pk):
    package = Package.objects.get(id = pk)
    form = PackageUpdateForm(instance=package)
    
    if request.method == 'POST':
        form = PackageUpdateForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('Admin')
    context = {
        'form': form,
        'package': package
        }
    return render(request, 'Controller/Courier/update.html', context)


@login_required
def ParcelUpdateView(request, pk):
    parcel = Parcel.objects.get(id = pk)
    form = ParcelUpdateForm(instance=parcel)
    context = {
        'form': form,
        'parcel': parcel
        }
    if request.method == 'POST':
        form = ParcelUpdateForm(request.POST, instance=parcel)
        if form.is_valid():
            form.save()
            return redirect('courier_list')

    return render(request, 'Controller/Parcel/update.html', context)


    




@login_required
def dashboard(request):
    # initiate total/sum of kgs
    tpkweek = 0
    tpkyesterday = 0
    tpktoday = 0

    data_today = Package.objects.all()
    data_yesterday = Package.objects.all()
    data_week = Package.objects.all()

    for pack in data_today:
        tpktoday += int(pack.kgs)


    for pack in data_yesterday:
        tpkyesterday += int(pack.kgs)

    
    
    for pack in data_week:
        tpkweek += int(pack.kgs)
      
    # calculate parcel sum of

    trlkweek = 0
    trlkyesterday = 0
    trlktoday = 0

    prl_today = Parcel.objects.all()
    prl_yesterday = Parcel.objects.all()
    prl_week = Parcel.objects.all()

    for pack in prl_today:
        trlktoday += int(pack.kgs)


    for pack in prl_yesterday:
        trlkyesterday += int(pack.kgs)

    
    
    for pack in prl_week:
        trlkweek += int(pack.kgs)
      


    # calculate tottal/sum parcel and package 
    today = 0
    yesterday = 0
    week = 0
    today = 0
    if trlktoday > 0:

        today = tpktoday+trlktoday
    else:
        today = tpktoday

    if trlkyesterday > 0:

        yesterday = tpktoday+trlkyesterday
    else:
        yesterday = tpkyesterday


    if trlkweek > 0:

        week = tpktoday+trlkweek
    else:
        week = tpkweek





    # fetch packages from database
    packages = Package.objects.all()

    # fetch parcel from database
    parcel = Parcel.objects.all()

  
    print(today)

    context ={

        # display total/sum of kg
        'today': today,
        'yesterday': yesterday,
        'week': week,

        # display list of packages
        'packages': packages,
        'parcel': parcel,
    }
    return render(request, 'Controller/dashboard/index.html', context)


@login_required
def courier_list_view(request):
    packages = Package.objects.all().order_by('-created_at')[:10]
    context = {
        'packages': packages
        }
    return render(request, 'Controller/Courier/index.html', context)
@login_required
def parcel_lits_view(request, pk):
    package = Package.objects.get(id=pk)
    parcel = package.parcels.all().order_by('-created_at')[:10]
    context = {
        'package': package,
        'parcel': parcel
    }
    return render(request, 'Controller/Parcel/parcel_list.html', context)
@login_required
def shengzen_view(request):
    shengzen_goods = Package.objects.filter(percel_type='shengzen goods').order_by('-created_at')[:6]
    context = {
        'shengzen_goods': shengzen_goods,
    }
    return render(request, 'Controller/Courier/shengzen_goods.html', context)



@login_required
def express_view(request):
    express_goods = Package.objects.filter(percel_type='express goods').order_by('-created_at')[:6]
    context = {
        'packages': express_goods,
    }
    return render(request, 'Controller/Courier/express_goods.html', context)


@login_required
def normal_view(request):
    normal_goods = Package.objects.filter(percel_type='normal goods').order_by('-created_at')[:6]
    context = {
        'packages': normal_goods,
    }
    return render(request, 'Controller/Courier/normal_goods.html', context)
@login_required
def arrival_view(request):
    arrival = Package.objects.filter(status='ARRIVED').order_by('-created_at')[:6]
    context = {
        'packages': arrival,
    }
    return render(request, 'Controller/Courier/arrival_goods.html', context)
@login_required
def received_view(request):
    recieved = Package.objects.filter(status='RCS - recieved from shipper').order_by('-created_at')[:6]
    context = {
        'packages': arrived,
    }
    return render(request, 'Controller/Courier/received_goods.html', context)


@login_required
def delivered_view(request):
    delivered_goods = Package.objects.filter(status='delivered').order_by('-created_at')[:6]
    context = {
        'packages': delivered_goods,
    }
    return render(request, 'Controller/Courier/delivered_goods.html', context)







# @login_required
# def createInvoice(request, pk):
#     package_id = Package.objects.get(id = pk)
#     parcle_id = Parcel.objects.get(id = pk)

#     customer_name = package_id.customer_name
#     #create a blank invoice ....
#     number = 'INV-'+customer_name+str(uuid4()).split('-')[1]
#     newInvoice = Invoice.objects.create(number=number)
#     newInvoice.save()

#     inv = Invoice.objects.get(number=number)
#     return redirect('create-build-invoice', slug=inv.slug)



# @login_required
# def createBuildInvoice(request, slug):
#     #fetch that invoice
#     try:
#         invoice = Invoice.objects.get(slug=slug)
#         pass
#     except:
#         messages.error(request, 'Something went wrong')
#         return redirect('invoices')

#     #fetch all the products - related to this invoice
#     products = Product.objects.filter(invoice=invoice)


#     context = {}
#     context['invoice'] = invoice
#     context['products'] = products

#     if request.method == 'GET':
#         prod_form  = ProductForm()
#         inv_form = InvoiceForm(instance=invoice)
#         client_form = ClientSelectForm(initial_client=invoice.client)
#         context['prod_form'] = prod_form
#         context['inv_form'] = inv_form
#         context['client_form'] = client_form
#         return render(request, 'invoice/create-invoice.html', context)

#     if request.method == 'POST':
#         prod_form  = ProductForm(request.POST)
#         inv_form = InvoiceForm(request.POST, instance=invoice)
#         client_form = ClientSelectForm(request.POST, initial_client=invoice.client, instance=invoice)

#         if prod_form.is_valid():
#             obj = prod_form.save(commit=False)
#             obj.invoice = invoice
#             obj.save()

#             messages.success(request, "Invoice product added succesfully")
#             return redirect('create-build-invoice', slug=slug)
#         elif inv_form.is_valid and 'paymentTerms' in request.POST:
#             inv_form.save()

#             messages.success(request, "Invoice updated succesfully")
#             return redirect('create-build-invoice', slug=slug)
#         elif client_form.is_valid() and 'client' in request.POST:

#             client_form.save()
#             messages.success(request, "Client added to invoice succesfully")
#             return redirect('create-build-invoice', slug=slug)
#         else:
#             context['prod_form'] = prod_form
#             context['inv_form'] = inv_form
#             context['client_form'] = client_form
#             messages.error(request,"Problem processing your request")
#             return render(request, 'invoice/create-invoice.html', context)


#     return render(request, 'invoice/create-invoice.html', context)


@login_required
def addExtraParcelInfo(request, parcel_id):
    package = Parcel.objects.get(pk = parcel_id)
    form = createExtraParcelForm()
    if request.method == "POST":
        package = Package.objects.get(pk = parcel_id)
        print(package)
        status = request.POST['status']
        terminal = request.POST['terminal']
        note = request.POST['terminal']
        extras = ExtraPackageInfo(package=package, status=status, terminal=terminal, note=note)
        extras.save()
        return redirect('Admin')
    context = {
        'package':package,
        'form': form
    }
    return render(request, 'Controller/Courier/extra_package_info.html', context)



@login_required
def addExtraPackageInfo(request, package_id):
    package = Package.objects.get(pk = package_id)
    form = createExtraParcelForm()
    if request.method == "POST":
        package = Package.objects.get(pk = package_id)
        print(package)
        status = request.POST['status']
        terminal = request.POST['terminal']
        note = request.POST['terminal']
        extras = ExtraPackageInfo(package=package, status=status, terminal=terminal, note=note)
        extras.save()
        return redirect('Admin')
    context = {
        'package':package,
        'form': form
    }
    return render(request, 'Controller/Courier/extra_package_info.html', context)











@login_required
def prinArea(request, pk):
    package = Package.objects.get(id = pk)
    
    context = {
        'package': package,
    }
    return render(request, 'Controller/label/label.html', context)



@login_required
def userCreation(request):
    form = createUserForm()
    if request.method == "POST":
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save(commit=False)

    context = {'form': form}
    return render(request, 'Controller/accounts/register.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_staff and request.user.is_active:
                return redirect('Admin')
            elif request.user.is_superuser and request.user.is_active:
                messages.success(request, 'welcome back '+username)
                return redirect('Admin')
        else:
            messages.error(request, 'invalid credidentials or your not authorized')
            return redirect('login')
    
    context = {}
    return render(request, 'Controller/accounts/login.html', context)
    
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def users(request):
    form = createUserForm()
    if request.method == "POST":
        form = createUserForm(request.POST)
        if form.is_ajax():
            form.save()
    context = {'form': form}
    return render(request, 'Controller/accounts/users.html', context)





def search_result(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        shipping = request.POST.get('shipping')
            
        if Package.objects.filter(tracking_key=shipping).exists():
            ship = Package.objects.filter(tracking_key=shipping)
            if len(shipping) > 0 and len(ship) > 0:
                for pos in ship:
                    data = []
                    item = {
                        'pk': pos.pk,
                        'sender_name': pos.sender_name,
                        'reciever_name': pos.reciever_name,
                        'kg': pos.kgs,
                        'place_from': pos.place_from,
                        'destination': pos.destination,
                        'number_of_parcel': pos.number_of_parcel,
                        'chargable_weight': pos.chargable_weight,
                        'tracking_key': pos.tracking_key,
                        }
                    data.append(item)
                    res = data
            else:
                res = 'No data match'
            return JsonResponse({'package_data': res})
        if Parcel.objects.filter(tracking_key=shipping).exists():
            ship = Parcel.objects.filter(tracking_key=shipping)
            if len(shipping) > 0 and len(ship) > 0:
                for pos in ship:
                    data = []
                    item = {
                        'pk': pos.pks,
                        'sender_name': pos.sender_name,
                        'reciever_name': pos.reciever_name,
                        'number_of_parcel': pos.number_of_parcel,
                        'master_kg': pos.master_kg,
                        'kg': pos.kg,
                        'place_from': pos.place_from,
                        'destination': pos.destination,
                        'mtk': pos.mtk,
                        'tracking_key': pos.tracking_key,
                    }
                    data.append(item)
                    res = data
            else:
                res = 'No data match'
            return JsonResponse({'parcel_data': res})
    return JsonResponse({'no_data_matching': 'No data match'})



