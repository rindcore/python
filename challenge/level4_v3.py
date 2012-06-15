#!/usr/bin/env python3

import urllib.request
import re


base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

print("Please input the nothing number:")
nothing_no=input()

while nothing_no:
    f = urllib.request.urlopen(base_url+nothing_no)
    page_src = f.read().decode('utf-8')
    print(page_src)
    
    try:
        nothing_no = re.findall(r"([0-9]+)", page_src)[0]
    except IndexError:
        nothing_no = None
