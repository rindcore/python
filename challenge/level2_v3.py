#!/usr/bin/env python3

import urllib.request

f = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')

page_src = f.read().decode('utf-8')

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._comment = []

    def handle_comment(self, data):
        self._comment.append(data)
        

    def get_comment(self):
       	return self._comment

htmldata = MyHTMLParser()
htmldata.feed(page_src)
mess_text = htmldata.get_comment()[1]

char_dict = {}
seq = []

for i in range(len(mess_text)):
    if mess_text[i] in char_dict:
        char_dict[mess_text[i]] += 1
    else:
        seq.append(mess_text[i])
        char_dict[mess_text[i]] = 1

rare_no = 5000

for i in range(len(seq)):
    if char_dict[seq[i]] < rare_no:
        print(seq[i], end='')

print()
