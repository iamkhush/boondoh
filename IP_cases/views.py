# Create your views here.
from IP_cases.models import *
from IP_cases.forms import indexform
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    form = indexform()
    context = { 'form' : form }
    template = 'index.html'
    return render_to_response(template,context,context_instance=RequestContext(request))