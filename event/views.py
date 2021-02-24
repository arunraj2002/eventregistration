from django.shortcuts import render
from .models import participant
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    context = {}
    return render(request, 'event/home.html', context)  

def register(request):
    context = {}

    if request.method == 'POST':
        p1=participant()
        p1.username = request.POST.get('username','-')
        p1.email = request.POST.get('email','-')
        p1.phone = request.POST.get('phone','000')
        p1.institution = request.POST.get('institution','-')

        if len(participant.objects.all()) > 5:
            return render (request, 'event/failed.html',context)

        else:
            p1.save()
            return render (request, 'event/success.html',context)

    if request.method =='GET':
        context['username'] = '-'
        context['email'] = '-'
        context['phone'] = '00'
        context['institution'] = '-'

    return render(request, 'event/register.html', context)

def listofparticipants(request):
    context = {}

    context['participant'] = participant.objects.all()

    return render(request, 'event/participant.html', context)

def success(request):
    context = {}
    return render(request, 'event/success.html', context)

def failed(request):
    context = {}
    return render(request, 'event/failed.html', context)
