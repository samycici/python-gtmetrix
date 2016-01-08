__author__ = 'samycici'
import time
from gtmetrix import *
import json
from gtmetrix import settings

with open('sites.json') as data_file:
    list_sites = json.load(data_file)

    for key, value in list_sites.items():
        print ("Site: %s - Url: %s" % (key, value))
        gt = GTmetrixInterface(settings.USER, settings.API_KEY)
        print ("Starting Analysis")
        my_test = gt.start_test(value)
        time.sleep(60)
        print ("Recording the Results")
        results = gt.poll_state_request(key, my_test.test_id)


