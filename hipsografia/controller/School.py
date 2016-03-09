#-*- coding: utf-8 -*-
# encoding: utf-8
import csv

import util
from unicodedata import normalize
from hipsografia.controller.Status import *


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


  def readCSV(self, path):
    reader = csv.reader(path, delimiter=';')
    schoolList = []
    columns = 0
    try: 
      for row in reader:
        columns = len(row)
        if columns > 0 and columns < 12:
          if row[0].isdigit():
            if columns <= 9:
              lat, lng = util.geocoding(row[2], row[3], row[4], row[5])
              #lat, lng = 0.0 , 0.0
              print lat, lng
            else:
              lat, lng = float(row[9]), float(row[10])
            if isinstance(lat, float) and isinstance(lng, float): 
              school = School(normalize('NFKD', str(row[1]).decode('utf-8')).encode('ASCII', 'ignore').decode('ASCII'), 
                normalize('NFKD', str(row[2]).decode('utf-8')).encode('ASCII', 'ignore').decode('ASCII'), 
                normalize('NFKD', str(row[3]).decode('utf-8')).encode('ASCII', 'ignore').decode('ASCII'), 
                normalize('NFKD', str(row[4]).decode('utf-8')).encode('ASCII', 'ignore').decode('ASCII'),
                normalize('NFKD', str(row[5]).decode('utf-8')).encode('ASCII', 'ignore').decode('ASCII'),
                lat, lng, 
                int(row[6]), 
                normalize('NFKD', str(row[7]).decode('utf-8')).encode('ASCII', 'ignore').decode('ASCII'), 
                int(row[8]))#int(row[6]))
              schoolList.append(school)
        else:
          return schoolList, Status.FILE_FORMAT
    except Exception as e:
      util.sendNotificationDeveloper(Status.IPUSH_EVENT_EXCEPTION, Status.READ_FILE);
      raise Exception(Status.READ_FILE)
    
    if columns <= 9:
      try: 
        writeCSV(schoolList)
      except Exception as e:
        raise Exception(e)
    return schoolList, Status.OK


def writeCSV(schoolList):
  count = 1
  try:
    with open("paolla.csv", "wb") as output_file:
      csv_out = csv.writer(output_file, delimiter=';')
      csv_out.writerow(['ID','NAME', 'ADDRESS', 'CITY', 'STATE', 'COUNTRY', 'ZONE', 'SESSION', 'VOTE', 'LATITUDE', 'LONGITUDE'])
      for school in schoolList:
        try:
          csv_out.writerow([ count, school.name, school.address, school.city, school.state, school.country, school.zone, 
            school.session, school.vote, school.latitude, school.longitude])
        except Exception as e:
          util.sendNotificationDeveloper(Status.IPUSH_EVENT_EXCEPTION, Status.WRITE_FILE)
        count += 1
  except Exception as e:
    util.sendNotificationDeveloper(Status.IPUSH_EVENT_EXCEPTION, Status.WRITE_FILE)
    raise Exception(Status.WRITE_FILE)