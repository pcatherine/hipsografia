#-*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render, redirect, render_to_response
from django.template import loader, Context, Template, RequestContext

from hipsografia.controller.School import *

def index(request):
  csvFile = request.FILES.get('csvfile', '')
  if csvFile != '':
    school = School()
    schoolList = school.readCSV(csvFile)
    return render_to_response('map.html',  
      {'schoolList': schoolList}, context_instance=RequestContext(request))

  return render(request, 'index.html')