# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:51:28 2021

@author: Manish Kuamr Goswami

"""

#!/bin/python
#Importing Module of Python

import time
import pyfiglet
import sys
from datetime import datetime
import socket

start = time.time()

banner = pyfiglet.figlet_format("MKG PORT SCANNER")
print(banner)

#Defining Targert

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4

else:
    print("invalid amount of arguments.")
    print("Syntex: python3 filename.py")
    
#Adding Banner 

print("-" * 50)
print("Tool created by Manish Kumar Goswami")
print("Scanning Target: " + target)
print("Scanning Started: "+ str(datetime.now()))
print("-" * 50)

# Error handling

count = 0

try:
    for port in range(1,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)
        result = s.connect_ex((target.port))
        
        if result == 0:
            count += 1
            print("port {} is open".format(port))
        else:
            print("port {} is close".format(port))
        s.close
    print("{} Ports are open".format(count))
            
except KeyboardInterrupt:
    print("\n Exiing program.")
    sys.exit()
    
except socket.gaierror:
    print("Hostname could not be resoulved.")
    sys.exit()
    
except socket.error:
    print("Couldn't Connect to server.")
    sys.exit()
 
totleTime = int(time.time() - start)

if totleTime >= 60:
    print("Scanning Completed in: {} min".format(totleTime/60))

else:
    print("Scanning Completed in: {} sec".format(totleTime))
