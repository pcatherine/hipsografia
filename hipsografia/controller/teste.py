#!-*- conding: utf-8 -*-
# encoding: utf-8
import re
from htmlentitydefs import name2codepoint
import os
import sys

# print sys.getdefaultencoding()
from geopy.geocoders import Nominatim

geolocator = Nominatim()
location = geolocator.geocode('Rua Comandante Ataliba Euclides Vieira, 1030, Campinas - SP')
print(location.latitude, location.longitude) 
# location = geolocator.geocode('AV JÚLIO DE MESQUITA, 840, Campinas - SP')
# print(location.latitude, location.longitude)
# location = geolocator.geocode('Rua Visconde de Taunay, 250, Campinas - SP')
# # # # print(location.address)
# print(location.latitude, location.longitude)
# print(location.raw)
# ola = 'COLÉGIO DE APLICAÇÃO PIO XII'
# print ola

# print re.sub('&(%s);' % '|'.join(name2codepoint),lambda m: unichr(name2codepoint[m.group(1)]), ola)

# (-22.9052241, -47.0503148)
# (-22.9080033, -47.060002)
# o = 'a test of \xc3\xa9 char'
# print o.decode('latin-1').encode("utf-8")
# 'a test of \xc3\xa9 char'