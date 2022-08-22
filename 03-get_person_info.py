#!/usr/bin/env python3

import requests
from variables import guid, prod, test

server = test

file_oids = open("oids.txt", "r")

URL = 'http://' + f"{ server }" + '/nsi/fhir/get_resource?_format=json'
HEADERS = {"Authorization": f"{guid}"}
SYSTEM = '1.2.643.2.69.1.1.1.104'


def get_persons(snils):
    params = dict(system=SYSTEM, code=snils)
    res = requests.get(URL, headers=HEADERS, params=params)
    json = res.json()
    print(
        json['general']['snils'],
        json['general']['lastName'],
        json['general']['firstName'],
        json['general']['patronymic'],
        json['general']['birthDate'],
        file=file_persons
    )

while True:
    mcode = file_oids.readline()
    if not mcode:
        break
    print(mcode)
    file_persons = open("persons/%s-persons.txt" % mcode.replace("\n", ""), 'w')
    file_snils = open("persons/%s.txt" % mcode.replace('\n',''), "r")
    while True:
        snils = file_snils.readline()
        if not snils:
            break
        try:
            get_persons(snils.strip())
        except KeyError:
            pass

