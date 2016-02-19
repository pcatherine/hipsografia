#!-*- conding: utf-8 -*-
# encoding: utf-8
# import re
# from htmlentitydefs import name2codepoint
# import os
# import sys

# print sys.getdefaultencoding()
# from geopy.geocoders import Nominatim

# geolocator = Nominatim()
# location = geolocator.geocode('Núcleo Residencial Jardim Fernanda, Campinas - SP', timeout = 10) 
# print(location.latitude, location.longitude) 


import mechanize 
from bs4 import BeautifulSoup
import json


try:
  browser = mechanize.Browser()
  browser.set_handle_robots(False)
  browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:43.0) Gecko/20100101 Debian 3.2.73-2+deb7u1 Firefox/43.0')]
  htmltext = browser.open('http://maps.google.com.br/maps/api/geocode/json?address=250+neuza+goulart+brizola,campinas,brasil&sensor=false')
  soup = BeautifulSoup(htmltext, "html.parser")

  ola1 = json.loads(str(soup))
  print ola1['results'][0]['geometry']['location']['lat']
  print ola1['results'][0]['geometry']['location']['lng']

except Exception, e:
  print e










# ola = json.loads(ola);
# print [obj for obj in ola if(obj['results'] == 1)] 

# Transform json input to python objects




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

# EE DOM BARRETO
# FACULDADE ANHANGUERA DE CAMPINAS - UNIDADE 3 (FAC)
# EMEI PREFEITO JOSÉ PIRES NETO

# from cipher import Cipher
# from vigenere import Vigenere
# import sys

# class Cipher(object):
#     """ Classe base para as cifras classicas """
#     def format_str(self, text):
#         '''
#         Retorna text sem espacos e em maiusculas
#         '''
#         return text.replace(' ', '').upper()
 
#     def shift_alphabet(self, alphabet, shift):
#         '''
#         Retorna alphabet com deslocamento de valor shift
#         '''
#         return alphabet[shift:] + alphabet[:shift]

# print '565'.isdigit()
 
# class Vigenere(Cipher):
#     """ Cifra de Vigenere """
#     def __init__(self):
#         self.plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
#     def repeat_password(self, password, text):
#         '''
#         Repete a password ate o tamanho de text
#         '''
#         if len(password) < len(text):
#             new_pass = password * (len(text)/len(password))
#             if len(new_pass):
#                 new_pass += password[:len(new_pass)]
#             return new_pass.upper()
#         return password.upper()
 
#     def encrypt(self, plaintext, password, decrypt=False):
#         '''
#         Cifra plaintext com a cifra de Vigenere
#         Decifra se decrypt for True
#         '''
#         password = self.repeat_password(password, plaintext)
#         plaintext = self.format_str(plaintext)
#         textout = ''
#         for idx, char in enumerate(plaintext.upper()):
#             # indice da letra da cifra
#             idx_key = self.plain.find(password[idx])
#             # gera alfabeto cifrado
#             c_alphabet = self.shift_alphabet(self.plain, idx_key)
 
#             if decrypt:
#                 idx_p = c_alphabet.find(char)
#                 textout += self.plain[idx_p]
#             else:
#                 idx_p = self.plain.find(char)
#                 textout += c_alphabet[idx_p]
 
#         return textout
 
#     def decrypt(self, ciphertext, password):
#         '''
#         Decifra ciphertext
#         '''
#         return self.encrypt(ciphertext, password, True)



 
# versao = sys.version_info[0]
 
# if versao == 2:
#     leitura = raw_input
# elif versao == 3:
#     leitura = input
 
# txt_in = 'Ola meu nome e paolla'#leitura('Texto a ser cifrado: ')
# password = 'sagaz'#leitura('Senha: ')
 
# cifra = Vigenere()
# txt_cifrado = cifra.encrypt(txt_in, password)

# print('Texto cifrado: {0}'.format(txt_cifrado))
# print('  Texto plano: {0}'.format(cifra.decrypt(txt_cifrado, password)))
