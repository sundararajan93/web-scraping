#!/usr/bin/python3
import re
import urllib.request

URL = input("Enter the URL - ")

# URL = 'https://www.labnol.org/internet/101-useful-websites/18078/'

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
      'AppleWebKit/537.11 (KHTML, like Gecko) '
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

req = urllib.request.Request(url=URL, headers=header) 
html = urllib.request.urlopen(req).read()

decoded_string = html.decode('utf-8')

pattern = re.compile(r"https?://(www\.)?([a-zA-Z0-9-_.]+)(\.[a-zA-Z0-9-_.]+)")
matches = pattern.finditer(decoded_string)
for i in matches:
    print(i.group(2)+i.group(3))
print("--------------------------------------------")
