import mechanize 
from bs4 import BeautifulSoup
import json


def geocoding(address):
   number, address, city, state, country = addressToRequest(address)
   try:
     browser = mechanize.Browser()
     browser.set_handle_robots(False)
     browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:43.0) Gecko/20100101 Debian 3.2.73-2+deb7u1 Firefox/43.0')]
     htmltext = browser.open('http://maps.google.com.br/maps/api/geocode/json?address=250+neuza+goulart+brizola,campinas,sp,brasil&sensor=false')
     soup = BeautifulSoup(htmltext, "html.parser")

     results = json.loads(str(soup))
     return results['results'][0]['geometry']['location']['lat'], results['results'][0]['geometry']['location']['lng']

   except Exception, e:
     print address


def addressToRequest(address):
   pass