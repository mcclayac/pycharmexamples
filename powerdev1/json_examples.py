"""
        
   created: mcclayac
   Company Name : BigMAN Software
   MyName: Tony McClay
   date: 11/21/18
   day of month: 21
   
   Project Name: pycharmexamples
   filename:  
   package name: 
   IDE: PyCharm
   
   
"""

import json

with open('../json_examples/usd.json') as f:
    data = json.load(f)

print("Base Dollar {}".format(data['base']))

print("To Canada Dollars Base: {}".format(data['rates']['CAD']))

