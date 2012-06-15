#!/usr/bin/env python3

def pc_map(ch):
    ret = ''
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
       ret = chr(ord(ch)+2)
       if ord(ret) > ord('z'):
          ret = chr(ord(ret)-26)
    else:
       ret = ch

    return ret

cipher_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. \
rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb \
gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(cipher_text)

clear_text=''

for i in range(len(cipher_text)):
    clear_text += pc_map(cipher_text[i])

print(clear_text)
