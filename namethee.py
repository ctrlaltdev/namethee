#!/usr/bin/python3
import sys
import json
import urllib.request
import urllib.parse

keyfile = open('./APIKEY')
key = keyfile.read()

def party(list):
  print(list)

def binomial(list):
  for word in list:
    url = 'http://thesaurus.altervista.org/thesaurus/v1?language=en_US&output=json&word='+word+'&key='+key
    f = urllib.request.urlopen(url)
    j = json.loads(f.read().decode('utf-8'))['response']

words = sys.argv
del words[0]

if len(words) > 2:
  party(words)
else:
  binomial(words)