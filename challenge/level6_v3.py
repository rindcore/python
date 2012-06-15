#!/usr/bin/env python3

import re
import zipfile

zf = '/home/warren/Downloads/channel.zip'

print("Please input the nothing number:")
nothing_no=input()

afile = ''
comm_str = ''

with zipfile.ZipFile(zf) as f:
    while nothing_no:
        afile = nothing_no+'.txt'
        lines = f.read(afile).decode('UTF-8')
        comm_str += f.getinfo(afile).comment.decode('UTF-8')

        try:
            nothing_no = re.findall(r"([0-9]+)", lines)[0]
        except IndexError:
            nothing_no = None

print(comm_str)
