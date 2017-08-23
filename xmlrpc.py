#!/usr/bin/python
# coding: utf8
import sys
import time
import xml.etree.cElementTree as ET
import csv
from collections import defaultdict
import xmlrpclib

reload(sys)
sys.setdefaultencoding('utf-8')


log_report = defaultdict(lambda: 0)

url = 'http://localhost:8969'
xmlrpctxt = '/xmlrpc/'
#db = 'preprodputhod'
db = 'test2'
username = 'admin'
password = 'admin'

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

csv.register_dialect('pointvirg', delimiter=';', quoting=csv.QUOTE_ALL)

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890"

clients = models.execute_kw(
    db, uid, password,
    'res.partner', 'search_read',
    [[('customer', '=', True)]],
    {'limit': 10, 'fields': [
        'property_account_receivable',
        'property_payment_term',
        'property_account_position']
    })

for client in clients:
    print client

for tva_file in ["Clients.csv", "Articles.csv"]:
    f = open(tva_file, 'rt')
    i = 0
    rez = []

    reader = csv.reader(f, dialect='pointvirg')
    if tva_file == 'Clients.csv' :
        modl = 'tmpclient'
    else : 
        modl = 'tmparticle'
    for row in reader:
        print 'Current Line : ' + str(i)
        i += 1
        if i == 1:
            keys = row
            ki = 0
            for k in keys:
                for ch in k:
                    if ch not in alphabet:
                        k = k.replace(ch ,"_")
                k = k.lower() + "_" + str(ki)
                keys[ki] = k
                ki += 1
            print keys
        else:
            try:
                obj = {}
                for k in range(min(len(keys),len(row))):
                    obj[keys[k]] = row[k]
                rez.append(obj)
                # for fild in ['Prix_Etiquette','Poids_Brut']:
                #     if obj[fild] == '':
                #         obj[fild] = 0
                id = models.execute_kw(db, uid, password, modl, 'create', [obj])
            except Exception as ex:
                print 'Error in FILE : ' + tva_file
                print 'Error in Line : ' + str(i)
                print ex
                pass
    print rez
    f.close()
        
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "New Partner",
}])