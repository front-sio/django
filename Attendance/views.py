from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class attendance_list(View):
    def get(self, *args, **kwargs):
        # return render(request, 'Attendance/attendance_list.html')
        return HttpResponse("Hello async world!")

    def post(self, *args, **kwargs):
        pass
