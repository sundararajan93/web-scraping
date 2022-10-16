#!/usr/bin/python3

import re
import urllib.request


#URL = 'https://www.digitalgyd.com/email-name-ideas/'
URL = input("Enter the URL - ")
open_url = urllib.request.urlopen(URL)
html = open_url.read()

mystr = html.decode("utf8")
open_url.close()

text = mystr

email_pattern = re.compile(r"([a-zA-Z0-9-_.]+)@([a-zA-Z0-9-]+)\.([a-zA-Z-]+)")
matches = email_pattern.finditer(text)

for i in matches:
    print(i.group())


# By default group(0) - Display all the values
# since we grouped as three (....)@(....).(....) we can call with respective numbers
# group(1) -> mailid -> sundararajan.t1
# group(2) -> Domain -> gmail
# group(2) -> Extension -> com