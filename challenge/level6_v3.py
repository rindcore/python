#!/usr/bin/env python3

import re
import zipfile

nothing_no = '90052'

afile = ''
comm_str = ''

with zipfile.ZipFile('channel.zip') as f:
    while nothing_no:
        afile = nothing_no+'.txt'
        lines = f.read(afile).decode('UTF-8')
        comm_str += f.getinfo(afile).comment.decode('UTF-8')

        try:
            nothing_no = re.findall(r"([0-9]+)", lines)[0]
        except IndexError:
            nothing_no = None

print(comm_str)
