# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 15:57:32 2022

@author: reema
"""

import sys 
import json 
import requests



# to make my code run from command line and recive argument
if len( sys.argv) == 2:
    monthsNum  = sys.argv[1]

else: 
    monthsNum = input()
# send request to the firebase and take the specifid data that meets the commands, conditons
rq = requests.get ('https://dsci551-a7a0e-default-rtdb.firebaseio.com/.json?orderBy="tenure"&print=pretty&startAt={}'.format(int(monthsNum)))
result = rq.json()

# get the cutomer who has tenure
l = []
for key in result.keys():
    val = result[key]['tenure']
    l.append(val)
# count their number
print(len(l))
