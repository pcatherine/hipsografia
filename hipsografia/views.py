#-*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render, redirect, render_to_response
from django.template import loader, Context, Template, RequestContext

from hipsografia.controller.School import *
from hipsografia.controller.Status import *


def index(request, alert='', description=''):
  csvFile = request.FILES.get('csvfile', '')
  if csvFile != '' and alert == '' and description == '':
    school = School()
    try:
      schoolList, status = school.readCSV(csvFile)
      if status == Status.OK:
        return render_to_response('map.html',  
          {'schoolList': schoolList}, context_instance=RequestContext(request))
      else:
        return index(request, 'danger', status)
    except Exception as e:
      return index(request, 'danger', e)

  return render_to_response('index.html',  
    {'alert': alert,
    'description': description}, context_instance=RequestContext(request))