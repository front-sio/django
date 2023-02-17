from django.shortcuts import render
from .forms import QuoteForm
from django.views import View
from .models import Contact
from CourierController.models import Package, Parcel

from .models import Quote, Team, Contact, About, SocialMedia, Service
import datetime



class Home(View):
    def get(self, request, *arggs, **kwargs):
        teams = Team.objects.all()
        # services = Service.objects.all()
        # contacts = Contact.objects.all()

        

    

        form = QuoteForm()
        context = {
            'teams': teams,
            'form': form,
            # 'services': services,
            # 'address': contacts,
        }
        return render(request, 'HomeController/index.html', context)
    
    def post(self, request, *args, **kwargs):
        form = QuoteForm()
        if request.POST:
            name = request.POST['name']
            email = request.POST['email']
            service = request.POST['service']

            quote = Quote(name=name, email=email, service=service)
            quote.save()
        context = {
            'form': form
        }
        return render(request, 'HomeController/index.html', context)




def About_us_view(request):
    abouts = About.objects.all()
    teams = Team.objects.all()
    contacts = Contact.objects.all()
    socials = SocialMedia.objects.all()
    context = {
        'abouts': abouts,
        'teams': teams,
        'address': contacts,
        'socials': socials,
    }
    return render(request, 'HomeController/about_us.html', context)



def Our_Services(request):
    services= Service.objects.all()
    contacts = Contact.objects.all()

    form = QuoteForm()
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        service = request.POST['service']

        quote = Quote(name=name, email=email, service=service)
        quote.save()
       
    context = {
        'services': services,
        'address': contacts,
        'form': form,
    }
    return render(request, 'HomeController/services.html', context)


def Contact_Us(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts,
        'address': contacts,
    }
    return render(request, 'HomeController/contact_us.html', context)






def Index(request):
    contacts = Contact.objects.all()
    context = {
        'address': contacts,
    }
    if request.method == 'POST':
        tracking_id = request.POST.get('tracking_key')
       
        courier_packages = Package.objects.filter(tracking_key=tracking_id)
        courier_parcel = Parcel.objects.filter(tracking_key=tracking_id)
        # print(couriers)
        if courier_packages:
            return render(request, 'HomeController/couriers.html', locals())
        if courier_parcel:
            return render(request, 'HomeController/couriers.html', locals())
        else:
            context["errors"] = "Sorry Your tracking id is invalid"
            return render(request, 'HomeController/couriers.html', context)
    else:
        return render(request, 'HomeController/couriers.html')


def CourierInfo(request, pk):
    
    contacts = Contact.objects.all()
    courier = Package.objects.get(id = pk)
    courier_details = courier.extraPackInfo.all().order_by('-time')

   
    context = {
        'courier_details': courier_details,
        'courier':courier,
        'address': contacts,
    }
    return render(request, 'HomeController/courierInfo.html', context)

                
                
                
