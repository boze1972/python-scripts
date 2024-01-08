# Author: Craig Ferguson
# 01/07/2024

import socket as socket

my_hostname = socket.gethostname()

print('Your hostname is: ' + my_hostname)

my_ip = socket.gethostbyname(my_hostname)

print('Your IP Address is: ' + my_ip)

host = 'wellsfargo.com'

ip = socket.gethostbyname(host)

print('The IP Address of ' + host + ' is: ' + ip)