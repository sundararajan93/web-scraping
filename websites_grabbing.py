#!/usr/bin/python3
import re
import urllib.request

URL = 'https://www.independence.edu/blog/useful-websites-for-college-students'

open_url = urllib.request.urlopen(URL)
html = open_url.read()

decoded_string = html.decode('utf-8')
open_url.close()

pattern = re.compile(r"https?://(www\.)?([a-zA-Z0-9-_.]+)(\.[a-zA-Z0-9-_.]+)")
matches = pattern.finditer(decoded_string)
for i in matches:
    print(i.group(2)+i.group(3))
print("--------------------------------------------")

# subbed_url = pattern.sub(r"\1", decoded_string)
# print(subbed_url)