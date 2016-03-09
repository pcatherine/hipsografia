#-*- coding: utf-8 -*-

class Status(object):
  OK = 'OK'
  FILE_FORMAT = 'Formato do arquivo incorreto.'
  READ_FILE = 'Não pôde ler no arquivo CSV.'
  WRITE_FILE = 'Não pôde escrever no arquivo CSV.'

  # Instapush
  IPUSH_EVENT_EXCEPTION = 'Exception'

  # Google Maps 
  GMAPS_ZERO_RESULTS     = 'GMaps: Nenhum resutado.'
  GMAPS_OVER_QUERY_LIMIT = 'GMaps: Excedido o limite de requisições.'
  GMAPS_REQUEST_DENIED   = 'GMaps: Requesicao negada.'
  GMAPS_INVALID_REQUEST  = 'GMaps: Requisicao inválida.'
  GMAPS_UNKNOWN_ERROR    = 'GMaps: Erro desconhecido.'