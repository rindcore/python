#!/usr/bin/env python3

import urllib.request
import re

f = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')

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
mess_text = htmldata.get_comment()[0]

m = re.findall(r"(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])", mess_text)

print(m)
