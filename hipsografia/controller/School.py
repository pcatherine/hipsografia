#-*- coding: utf-8 -*-
import csv
import re
from htmlentitydefs import name2codepoint

from geopy.geocoders import Nominatim

class School(object):
  def __init__(self, name='', address='', latitude=0, longitude=0, zone=0, session='', vote=0):
    self.name = name
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
      print row[1]
      # school = School(htmlentitydecode(row[1]), htmlentitydecode(row[2]), float(row[3]), float(row[4]), int(row[5]), htmlentitydecode(row[6]), (int(row[7])/10) )
      geolocator = Nominatim()
      location = geolocator.geocode(row[2])
      # print(location.address)
      print(location.latitude, location.longitude)
      print(location.raw)
      school = School(htmlentitydecode(row[1]), htmlentitydecode(row[2]), location.latitude, location.longitude, int(row[3]), htmlentitydecode(row[4]), (int(row[5])/10) )
      schoolList.append(school)
    return schoolList

def htmlentitydecode(s):
  return re.sub('&(%s);' % '|'.join(name2codepoint),lambda m: unichr(name2codepoint[m.group(1)]), s)