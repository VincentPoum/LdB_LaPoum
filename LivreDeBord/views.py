from django.shortcuts import render
from django.http import HttpResponse
from .models import Evenement, Histoire

def index(request):
#    event_liste = Evenement.objects.order_by('-date_event')[:5]
#    context = {'event_liste': event_liste}
    histoires = Histoire.objects.all()
    context = {'histoires': histoires}
    return render(request, 'LivreDeBord/coucou.html', context)
