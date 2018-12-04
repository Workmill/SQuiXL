#!usr/bin/env Python
# -*- coding: utf-8 -*-

import json

def loadJSON(file):
    json_data = open(file).read()
    data = json.loads(json_data)
    return data

def fetchoptions2JSON(fetch):
    # You get anyone list of duples (key, value) and convert fetch in json options
    json_data = {}
    for row in fetch:
        json_data[row[0]] = row[1] 
    return json_data