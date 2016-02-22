import mechanize 
from bs4 import BeautifulSoup
import json


def geocoding(address, city, state, country):
   try:
     browser = mechanize.Browser()
     browser.set_handle_robots(False)
     browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:43.0) Gecko/20100101 Debian 3.2.73-2+deb7u1 Firefox/43.0')]
     htmltext = browser.open(('http://maps.googleapis.com/maps/api/geocode/json?address=%s,%s,%s,%s&key=AIzaSyAjmai5mxOgNeKim8mRd0mCkT_BBJfftaA') % (addressToRequest(address), city, state, country))
     soup = BeautifulSoup(htmltext, "html.parser")

     results = json.loads(str(soup))
     return results['results'][0]['geometry']['location']['lat'], results['results'][0]['geometry']['location']['lng']

   except Exception, e:
     print results['status']
     return 'a','b'


def addressToRequest(address):
   street, number = address.split(',')
   print number.strip()+'+'+'+'.join(street.split(' '))
   return number.strip()+'+'+'+'.join(street.split(' '))


def teste(address):
   with open('test1.csv', 'wb') as testfile:
      csv_writer = csv.writer(testfile)
      for y in range(length):
         csv_writer.writerow([x[y] for x in hello])



