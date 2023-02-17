from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils import timezone
from datetime import timedelta
from django.db import models
from .models import Package
# Create your views here.


class courier_track_view(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Hello async world!")





def display_report(request):
    now = timezone.now()
    dataset = Package.objects.aggregate(
        total=models.Count('id'),
        today=models.Count('id', filter=models.Q(created_at__date=now.date())),
        yesterday=models.Count('id', filter=models.Q(created_at__date__gte=(now - timedelta(hours=24)).date())),
        last_7_day=models.Count('id', filter=models.Q(created_at__date__gte=(now - timedelta(days=7)).date())),
    )

    context = {
        'data': dataset
    }
    return render(request, 'Controller/dashboard/index.html', context)