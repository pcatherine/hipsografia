#-*- coding: utf-8 -*-
# encoding: utf-8
import csv
import re
from htmlentitydefs import name2codepoint

from geopy.geocoders import Nominatim

class School(object):
  def __init__(self, name='', addressMap='', address='', latitude=0, longitude=0, zone=0, session='', vote=0):
    self.name = name
    self.addressMap = addressMap
    self.address = address
    self.latitude = latitude
    self.longitude = longitude
    self.zone = zone
    self.session = session
    self.vote = vote

  # def __str__(self):
  #   return 'Colegio Eleitoral: ' + self._colegio + '/n/r'
  #   + 'Endereco: ' + self._endereco + '/n/r'
  #   + 'Latitude e Longitude: ' + self._lat + '/n/r'
  #   + 'Zona: ' + self._zona + '/n/r'
  #   + 'Sessao: ' + self._sessao + '/n/r'


  def readCSV(self, path):
    reader = csv.reader(path, delimiter=';')
    schoolList = []
    for row in reader:
      geolocator = Nominatim()
      # win
      # location = geolocator.geocode( str(row[2]).decode('latin-1').encode("utf-8") , timeout=10)
      # ubuntu
      print row[2]
      location = geolocator.geocode( str(row[2]), timeout=10) 

      school = School(str(row[1]).decode('latin-1').encode("utf-8"), str(row[2]).decode('latin-1').encode("utf-8"), str(row[3]).decode('latin-1').encode("utf-8"), location.latitude, location.longitude, int(row[4]), str(row[5]).decode('latin-1').encode("utf-8"), (int(row[6])/10))
      schoolList.append(school)
    return schoolList