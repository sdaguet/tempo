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

url = 'http://localhost:8069'
#url = 'http://localhost:8969'
xmlrpctxt = '/xmlrpc/'
db = 'preprodputhod'
username = 'admin'
password = 'qualifputhod1406'

#db = 'test2'
#username = 'admin'
#password = 'admin'

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

for tva_file in ["Articles-Famille.csv"]:
    f = open(tva_file, 'rt')
    i = 0
    rez = []

    reader = csv.reader(f, dialect='pointvirg')
    if tva_file == 'Clients.csv' :
        modl = 'tmpclient'
        modl_std = 'res.partner'
        fild_cxt = 'N_Client'
        fild_tmp_cxt = 'n_client_0'
    else :
        modl = 'tmparticle'
        fild_cxt = 'n_article'
        modl_std = 'product.product'
        fild_tmp_cxt = 'n_article_0'

    for row in reader:
        print 'Current Line : ' + str(i)
        i += 1
        if i == 1:
            keys = row
            ki = 0
            for ks in keys:
                for ch in ks:
                    if ch not in alphabet:
                        ks = ks.replace(ch ,"_")
                ks = ks.lower() + "_" + str(ki)
                ks = ks.replace("___","_")
                ks = ks.replace("__","_")
                keys[ki] = ks
                ki += 1
            print keys
        else:
            try:
                obj = {}
                for k in range(min(len(keys), len(row))):
                    obj[keys[k]] = row[k]
                rez.append(obj)
                print "obj 'tmqprix_45' "
                print obj['tmqprix_45']
                #break
                filds_exist = models.execute_kw(
                    db, uid, password,
                    modl_std, 'search_read',
                    [[(fild_cxt, '=', row[0])]],{'limit': 10,'fields': ['id']})
                print "ici search"
                print filds_exist
                if filds_exist:
                    filds_exist_tmp = models.execute_kw(
                        db, uid, password,
                        modl, 'search_read',
                        [[(fild_tmp_cxt, '=', row[0])]], {'limit': 10, 'fields': ['id']})
                    if filds_exist_tmp :
                        print "ici update"
                        models.execute_kw(db, uid, password, modl, 'write', [[filds_exist_tmp[0]['id']], {'prix_etiquette_24':obj['tmqprix_45']}])
                        print "ici update after"
                        print "ici update 2"
                        models.execute_kw(db, uid, password, 'product.product', 'write', [[filds_exist[0]['id']], {'lst_price':float(obj['tmqprix_45'].replace(",", "."))}])
                        print "ici update after 2"

                    else:
                        print "ici Rien du tt"
                else:
                    print "ici Rien"

            except Exception as ex:
                print 'Error in FILE : ' + tva_file
                print 'Error in Line : ' + str(i)
                print ex
                pass
    print rez
    f.close()