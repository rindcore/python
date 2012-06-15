#!/usr/bin/env python3

import urllib.request
import pickle

peak_banner = pickle.loads(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read())

for i in peak_banner:
    print(''.join(k*v for (k,v) in i))
