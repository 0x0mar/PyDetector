from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
import pydetector


def welcome(request):
    #return render_to_response(request,'pyd/.html')
    return  render(request, 'index.html')
def logs(request):
    return render(request,'logs.html')