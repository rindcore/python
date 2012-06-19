#!/usr/bin/env python

import Image
import re

im = Image.open("oxygen.png").convert("L")
all_pixels = im.load()

print "".join(map(chr, (map(int, (k for k in re.findall("\d+", "".join(map(chr, (all_pixels[i,43] for i in range(0,608,7))))))))))
