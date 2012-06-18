#!/usr/bin/env python

import Image

im = Image.open("oxygen.png").convert("L")
(pw, ph) = im.size

pixs = im.load()

pval = []

py = 43

ptmp = -1

for i in range(607):
    if ptmp != pixs[i,py]: 
        pval.append(pixs[i,py])
        ptmp = pixs[i,py]

print pval

[105, 10, 16, 101, 103, 14, 105, 16, 121]

dpix = []

for i in range(pw):
    for j in range(ph):
        if pixs[i,j] in [105, 10, 16, 101, 103, 14, 105, 16, 121]: dpix.append((i,j))

print "".join(chr(k) for k in pval)


print dpix
