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
  lists = []
  for word in list:
    tmplist = []
    tmplist.extend(word)
    url = 'http://thesaurus.altervista.org/thesaurus/v1?language=en_US&output=json&word='+word+'&key='+key

    f = urllib.request.urlopen(url)
    j = json.loads(f.read().decode('utf-8'))['response']

    for item in j:
      tmplist.extend(item['list']['synonyms'].split('|'))

    lists.append(tmplist)
  for l in lists[0]:
    for ll in lists[1]:
      print(l.replace(' ','').replace('\'','').replace('(relatedterm)','')+ll.replace(' ','').replace('\'','').replace('(relatedterm)',''))

words = sys.argv
del words[0]

if len(words) > 2:
  party(words)
else:
  binomial(words)