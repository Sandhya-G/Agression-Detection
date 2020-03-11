#!/usr/bin/env python
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
#print(strip_tags("&lt3  &lt &amp <html> sdghd <b> <head><<fotter> <body> <img></html> <3"))
#print(strip_tags("YAAAAAAY!!! &gt;:-D http://sentimentsymposium.com/."))