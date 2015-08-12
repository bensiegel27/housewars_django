from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import StationStatus
from forms import StationForm

def station_selection(request, station_number):
    if request.method == 'POST':
        form = StationForm(request.post)
        if form.is_valid():
            picked = form.cleaned_data.get('picked')
    else:
        form = StationForm
    station_status = StationStatus.objects.get(station_number=int(station_number))

    return HttpResponse(StationForm.get_choices)
    #return HttpResponse("This is the station selection page for station %s" % station_status)
