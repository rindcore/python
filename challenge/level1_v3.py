#!/usr/bin/env python3

frmtab = "abcdefghijklmnopqrstuvwxyz"
totab = "cdefghijklmnopqrstuvwxyzab"
transtab = str.maketrans(frmtab, totab)

cipher_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. \
rfyrq ufyr amknsrcpq ypc dmp. \
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.\
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

cipher_url = "map"

print(cipher_text.translate(transtab))

print(cipher_url.translate(transtab))
