#! /usr/bin/env python3

import requests
from variables import guid, prod, test

server = test

file_oids = open("oids.txt", "r")

URL = 'http://' + f"{ server }" + '/nsi/fhir/term/ValueSet/$lookup?_format=json'
HEADERS = {"Authorization": f"{ guid }",
           'Content-Type': 'application/json'}


def get_snils(mcode):
    file_snils = open("persons/%s.txt" % mcode.replace('\n',""), 'w')
    BODY = {"resourceType": "Parameters",
            "parameter": [
                {"name": "system",
                 "valueString": "urn:oid:1.2.643.2.69.1.1.1.84"},
                {"name": "code",
                 "valueString": "%s" % mcode.replace('\n',"")}
            ]
            }
    res = requests.post(URL, headers=HEADERS, json=BODY)
    json = res.json()
    size = len(json['parameter'][0]['valueCodeableConcept'])
    for i in range(0, size):
        print(json['parameter'][0]['valueCodeableConcept'][i]['code']
              , file=file_snils)
    file_snils.close()


while True:
    line = file_oids.readline()
    if not line:
        break
    get_snils(line)
file_oids.close()
