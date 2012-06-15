#!/usr/bin/env python3

import string

def pc_map(ch):
    if string.ascii_lowercase(ch) or string.ascii_uppercase(ch):
        ch = chr(ord(ch)+2)

    return ch


cipher_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. \
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq \
qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

clear_text = ""

for i in range(len(cipher_text)):
    clear_text = pc_map(cipher_text[i])


print(cipher_text)
