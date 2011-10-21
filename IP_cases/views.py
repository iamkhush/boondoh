# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from IP_cases.models import *
from IP_cases.forms import LocationForm, NoaForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from IP_cases.models import notice_of_appearence as notice, location

def dbcall():
    data_list = notice.objects.all()
    for data in data_list:
        try:
            a_loc=location.objects.create(state=data.state,office=data.office)
            data.location = a_loc
        except:
            l=location.objects.get(state = data.state, office = data.office)
            data.location = l
            data.save()

def index(request):
    if request.method == 'GET':
        form = LocationForm()
        return render_to_response('index.html', locals(), context_instance=RequestContext(request))

@csrf_exempt     
def get_notice(request):
    if request.method == 'GET':
        locid = request.GET.get('locid',None)
        notice_list = notice.objects.filter(location=int(locid))
        return render_to_response('notice.html', locals(), context_instance=RequestContext(request))
        
        