#!/usr/bin/python
# encoding=utf8
#https://github.com/addenial/scripts/blob/master/bloodhound-users-json-parser.py

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import simplejson

if len(sys.argv) == 1:
    print "Usage: " + sys.argv[0] + " bloodhound_users.json"
    sys.exit()

bhuserfile = sys.argv[1]
with open(bhuserfile) as data_file:
    data = simplejson.load(data_file)


for i in data['nodes']:
    if not ('NONHUMAN' or 'TEST') in i['props']['distinguishedname']:
        if i['type'] == 'User':
            print i['label'].rsplit('@')[0]
