# Author: Craig Ferguson
# 01/01/2024
# Script using tinyurl to get a short link based on your input.

import pyshorteners as sh

link = input('link: ')

s=sh.Shortener()

print(s.tinyurl.short(link))