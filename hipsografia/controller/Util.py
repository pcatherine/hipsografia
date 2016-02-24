import mechanize 
from bs4 import BeautifulSoup
import json
from instapush import Instapush, App

def geocoding(address, city, state, country):
   
   try:

     browser = mechanize.Browser()
     browser.set_handle_robots(False)
     browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:43.0) Gecko/20100101 Debian 3.2.73-2+deb7u1 Firefox/43.0')]
     htmltext = browser.open(('http://maps.googleapis.com/maps/api/geocode/json?address=%s,%s,%s,%s&key=AIzaSyAjmai5mxOgNeKim8mRd0mCkT_BBJfftaA') % (addressToRequest(address), city, state, country))
     
     soup = BeautifulSoup(htmltext, "html.parser")

     results = json.loads(str(soup))
     # time.sleep(0.5)
     return results['results'][0]['geometry']['location']['lat'], results['results'][0]['geometry']['location']['lng']

   except Exception, e:
      results['results']
     
     print e
     if results['status'] = 'ZERO_RESULTS':

     Util.sendNotificationDeveloper('Exception', 'Não pôde localizar o endereço');
     return 'a','b'
   #   ZERO_RESULTS" indicates that the geocode was successful but returned no results. This may occur if the geocoder was passed a non-existent address.
   # "OVER_QUERY_LIMIT" indicates that you are over your quota.
   # "REQUEST_DENIED" indicates that your request was denied.
   # "INVALID_REQUEST" generally indicates that the query (address, components or latlng) is missing.
   # "UNKNOWN_ERROR" indicates that the request could not be processed due to a server error. The request may succeed if you try again.


def addressToRequest(address):
   street, number = address.split(',')
   print number.strip()+'+'+'+'.join(street.split(' '))
   return number.strip()+'+'+'+'.join(street.split(' '))


def sendNotificationDeveloper(eventName, message):
   insta = Instapush(user_token='56bdf6045659e3895741cd2e')
   app = App(appid='56cdc55b5659e3f31ac56c64', secret='97d6095f608ae4caa8be2f3f7712daf4')
   app.notify(event_name=eventName, trackers={'message': message})