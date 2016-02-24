#-*- coding: utf-8 -*-
# encoding: utf-8
import csv
import time

import Util
import Status


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

  #alterar
  def readCSV(self, path):
    reader = csv.reader(path, delimiter=';')
    schoolList = []
    columns = 0
    try: 
      for row in reader:
        columns = len(row)
        if columns > 0 and columns < 12:
          if row[0].isdigit():
            # lat, lng = [(float(row[9]), float(row[10])) , (Util.geocoding(row[2], row[3], row[4], row[5]))] [ columns > 9 ]
            lat, lng = [(float(row[9]), float(row[10])),(0.0,0.0)] [ columns > 9 ]
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
        else
          return [], Status.FILE_FORMAT
    except Exception, e:
      print e
      Util.sendNotificationDeveloper('Exception', 'Não pôde ler no arquivo CSV');
    
    if columns <= 9:
      writeCSV(schoolList)
    return schoolList


def writeCSV(schoolList):
  count = 1
  try:
    with open("paolla.csv", "w+") as output_file:
      csv_out = csv.writer(output_file, delimiter=';', lineterminator='\n')
       csv_out.writerow(['ID','NOME', 'ENDERECO', 
          'CIDADE', 'ESTADO', 'PAIS', 'ZONA', 
          'SESSAO', 'VOTO', 'LATITUDE', 'LONGITUDE'])
      for school in schoolList:
        csv_out.writerow([count, school.name.encode("utf-8"), school.address.encode("utf-8"), 
          school.city, school.state, school.country, school.zone, 
          school.session, school.vote, school.latitude, school.longitude])
        count += 1
  except Exception, e:
    print e
    # Util.sendNotificationDeveloper('Exception', 'Não pôde escrever no arquivo CSV');