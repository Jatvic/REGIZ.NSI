#! /usr/bin/env python3

import requests
import sys
from variables import guid, test, prod

server = test

sys.stdout = open('oids.txt', "w")

URL = 'http://' + f"{ server }" '/nsi/fhir/term/ValueSet/$expand?_format=json'
HEADERS = {"Authorization": f"{guid}"}
BODY = {"resourceType": "Parameters",
        "parameter": [{
            "name": "system",
            "valueString": "urn:oid:1.2.643.2.69.1.1.1.84"
        }
        ]
        }

res = requests.post(url=URL, headers=HEADERS, json=BODY)
json = res.json()
size = len(json['parameter'][0]['resource']['expansion']['contains'])
for i in range(0, size):
    print(json['parameter'][0]['resource']['expansion']['contains'][i]['code'])
    # print(json['parameter'][0]['resource']['expansion']['contains'][i]['display'])
