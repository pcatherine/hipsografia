import mechanize 
from bs4 import BeautifulSoup
import json
from instapush import Instapush, App
from time import sleep
from hipsografia.controller.Status import *
from hipsografia.controller.Environment import *
   
def toAscii(text):
  ls = text.split(' ')
  print ls
  for i in range(len(ls)):
    print 'paolla', i
    ls[i] = unidecode.unidecode(ls[i])
    print ls[i]

  return ''.join(ls)

def geocoding(address, city, state, country):
  try:
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:43.0) Gecko/20100101 Debian 3.2.73-2+deb7u1 Firefox/43.0')]
    htmltext = browser.open(('http://maps.googleapis.com/maps/api/geocode/json?address=%s,%s,%s,%s') % (addressToRequest(address), city, state, country))
    soup = BeautifulSoup(htmltext, "html.parser")
    results = json.loads(str(soup))
    sleep(0.5)
    return results['results'][0]['geometry']['location']['lat'], results['results'][0]['geometry']['location']['lng']

  except Exception as e:
    if results['status'] == 'ZERO_RESULTS':
      sendNotificationDeveloper(Status.IPUSH_EVENT_EXCEPTION, (('%s, %s - %s, %s -> %s') % (address, city, state, country, Status.GMAPS_ZERO_RESULTS)))
    elif results['status'] == 'OVER_QUERY_LIMIT':
      sendNotificationDeveloper(Status.IPUSH_EVENT_EXCEPTION, (('%s, %s - %s, %s -> %s') % (address, city, state, country, Status.GMAPS_OVER_QUERY_LIMIT)))
      raise Exception(Status.GMAPS_OVER_QUERY_LIMIT)
    elif results['status'] == 'REQUEST_DENIED':
      sendNotificationDeveloper(Status.IPUSH_EVENT_EXCEPTION, (('%s, %s - %s, %s -> %s') % (address, city, state, country, Status.GMAPS_REQUEST_DENIED)))
    elif results['status'] == 'INVALID_REQUEST':
      sendNotificationDeveloper(Status.IPUSH_EVENT_EXCEPTION, (('%s, %s - %s, %s -> %s') % (address, city, state, country, Status.GMAPS_INVALID_REQUEST)))
    elif results['status'] == 'UNKNOWN_ERROR':
      sendNotificationDeveloper(Status.IPUSH_EVENT_EXCEPTION, (('%s, %s - %s, %s -> %s') % (address, city, state, country, Status.GMAPS_UNKNOWN_ERROR)))
    print e
    return 'a','b'


def addressToRequest(address):
  street, number = address.split(',')
  return number.strip()+'+'+'+'.join(street.split(' '))


def sendNotificationDeveloper(eventName, message):
  insta = Instapush(user_token=Environment.INSTAPUSH_USER_TOKEN)
  app = App(appid=Environment.INSTAPUSH_APPID, secret=Environment.INSTAPUSH_SECRET)
  # app.notify(event_name=eventName, trackers={'message': message})
  print 'Hipsografia Except:'+message