# Author: Craig Ferguson
# 01/01/2024
# Random password generator

import random
import string

print('Hello, welcome to password generator!')

length = int(input('Enter the length of password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
#print(lower)
#print(upper)
num = string.digits
symbols = string.punctuation
#print(num)
#print(symbols)

all = lower + upper + num + symbols

temp = random.sample(all, length)
#print(temp)
password = "".join(temp)
print(password)