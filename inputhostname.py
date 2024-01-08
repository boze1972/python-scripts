# Author: Craig Ferguson
# 01/07/2024
# Script to get IP from hostname.

import socket as socket

host = input('host: ')

ip = socket.gethostbyname(host)

print('The IP Address of ' + host + ' is: ' + ip)