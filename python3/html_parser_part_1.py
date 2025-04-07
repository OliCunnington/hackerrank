# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class mHTML(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print("->", i[0], ">", i[1])
    
    def handle_endtag(self, tag):
        print("End   :", tag)
    
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in attrs:
            print("->", i[0], ">", i[1])

p = mHTML()
comment = False
for i in range(int(input())):
    _in = input()
    if "<!--" in _in and "-->" not in _in:
        comment = True
    if not comment: 
        p.feed(_in)
    if comment and "-->" in _in:
        comment = False