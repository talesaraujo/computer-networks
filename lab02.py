"""
Created on Fri Apr 12 22:12:59 2018

Practice 2 - TI0145
@author: talesaraujo
"""

import os
import json
import urllib as url

from urllib import request, error


def q1():

    hostnames = ['google.com', 'wikipedia.org', 'ufc.br', 'si3.ufc.br', 
                 'debian.org', 'python.org', 'manjaro.org', 'telegram.org', 
                 'github.com', 'kaggle.com', 'stackoverflow.com', 'tensorflow.org', 
                 'cam.ac.uk', 'uni-heidelberg.de', 'ec-nantes.fr', 'shonenjump.com']

    print('Retrieving metainfo data from site list...')
    print("")

    request_return = {}
    for address in hostnames[:7]:
        try:
            req = request.urlopen('http://{}'.format(address))
            request_return[address] = [str(req.info()), req.getcode()]
            print('{}\n{}'.format(address, request_return[address][0]))

        except error.HTTPError as e:
            request_return[address] = [e, req.getcode()]
            print('{}\n{}'.format(address, e))          

    print ('\nShowing up HTTP response code for each request...')
    print ("")
    for address, (info, code) in request_return.items():
        print("Address: {:<25}HTTP Status: {}".format(address,code))

    print('\n')


def q2a():
    ceps = ['60455580', '60811341', '60060390', '60540215', '60020181']
    viacep = 'http://viacep.com.br/ws/{}/json'

    print("Querying places by 'CEP'...")
    print("")

    for cep in ceps:
        try:
            req = request.urlopen(viacep.format(cep))
            data = json.load(req)

            print("CEP: {}   Logradouro: {:<30} Bairro: {:<20}".format(cep, data['logradouro'], data['bairro']))

        except error.HTTPError as e:
            print('Error code: ', e.code)

        except error.URLError as e:
            print('Reason: ', e.reason)

    print("\n")


def q2b1():
    google_search = 'https://www.google.com/search?q={}'
    keywords = ['translate', 'youtube', 'sigaa', 'python-programming']

    print("Searching on Google keywords from list...")
    print("")
    
    for keyword in keywords:
        try:
            link = google_search.format(keyword)
            req = request.urlopen(link) 

            print("Search for '{}' got the following result: ".format(keyword))
            print("HTTP Response Status: ", req.getcode())
            print("Info: ", req.info())

        except error.HTTPError as e:
            if e.code == 403:
                print("Search for '{}' got HTTP error {}: Access Denied.".format(keyword, e.code))
            else:
                print("Search for '{}' got HTTP error {}.".format(keyword, e.code))

        except error.URLError as e:
            print("Search for '{}' got the following URL error: \n{}".format(keyword, e.reason))

    print("\n")

def q2b2():
    google_search = 'https://www.google.com/search?q={}'
    keywords = ['translate', 'youtube', 'sigaa', 'python-programming']

    for keyword in keywords:
        try:
            link = google_search.format(keyword)
            request_obj = request.Request(link, headers={'User-Agent': 'Mozilla/5.0'}) 

            req = request.urlopen(request_obj)

            print("Search for '{}' got the following result: ".format(keyword))
            print("HTTP Response Status: ", req.getcode())
            print("Info: ", req.info())

        except error.HTTPError as e:
            if e.code == 403:
                print("Search for '{}' got HTTP error {}: Access Denied.".format(keyword, e.code))
            else:
                print("Search for '{}' got HTTP error {}.".format(keyword, e.code))

        except error.URLError as e:
            print("Search for '{}' got the following URL error: \n{}".format(keyword, e.reason))
            
    print("\n")


if __name__ == '__main__':

    os.system('clear')

    q1()
    q2a()
    q2b1()
    q2b2()
