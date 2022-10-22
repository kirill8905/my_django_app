from django.shortcuts import render
from django.http import HttpResponse
#from .models import Objects_KA, System_KA, Signaling, Cctv, Accesscontrol

#def mitservice(request):

#    objects = Objects_KA.objects.all()
#    systems = System_KA.objects.all()
#    return render(request, 'service/service.html')

#def sys(request):

#    systems = System.objects.all()
#    return render(request, 'service/service.html', {'system_type':systems})

def mitservice(request):
    return HttpResponse('<h2>connection completed</h2>')