#-*- coding: utf-8 -*-
# encoding: utf-8
import csv
import Util


class School(object):
  def __init__(self, name='', address='', city = '', state = '', country = '', latitude=0, longitude=0, zone=0, session='', vote=0):
    self.name = name
    self.address = address
    self.city = city
    self.state = state
    self.country = country
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

  #alterar
  def readCSV(self, path):
    reader = csv.reader(path, delimiter=';')
    schoolList = []
    try: 
      for row in reader:
        if len(row) > 0:
          if row[0].isdigit():
            lat, lng = Util.geocoding(row[2], row[3], row[4], row[5])
            if isinstance(lat, float) and isinstance(lng, float): 
              school = School(str(row[1]).decode('latin-1').encode("utf-8"), 
                str(row[2]).decode('latin-1').encode("utf-8"), 
                str(row[3]).decode('latin-1').encode("utf-8"), 
                str(row[4]).decode('latin-1').encode("utf-8"),
                str(row[5]).decode('latin-1').encode("utf-8"),
                lat, lng, 
                int(row[6]), 
                str(row[7]).decode('latin-1').encode("utf-8"), 
                int(row[8]))#int(row[6]))
              schoolList.append(school)
    except:
      print 'deu ruim'
    return schoolList


  def writeCSV(self, schoolList):
    with open('test1.csv', 'wb') as testfile:
        csv_writer = csv.writer(testfile, delimiter=';')
        for y in xrange(11):
            csv_writer.writerow([x[y] for x in schoolList])
