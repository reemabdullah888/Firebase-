# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 19:39:50 2022

@author: reema
"""

import requests
import json
import sys

# To make my code run from the command line
if len(sys.argv) == 2:
    ksenior = sys.argv[1]
else:
    ksenior = input()
# send a request to the specified url to take the information under specific conditons and commands
re = requests.get('https://dsci551-a7a0e-default-rtdb.firebaseio.com/.json?&orderBy="Churn"&equalTo="Yes"&print=pretty')
# to make the respond readable
resutl = re.json()

ids = []
# to return the customer id
for key in resutl.keys():
        ids.append(resutl[key]['customerID'])
ids.sort()
# to assending order the customer id
for i in range(int(ksenior)):
    print(ids[i])
