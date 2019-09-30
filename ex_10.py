"""This is the first 4-chili exercise of this blog! We’ll see what people think, and decide whether or not to continue with 4-chili exercises in the future."""

import requests
from bs4 import BeautifulSoup

a=[]
html = requests.get("https://www.nytimes.com/")
content = html.content
soup = BeautifulSoup(content, 'html.parser')
titles= soup.find_all('h2')
title_string=titles.text

for i in titles:
    a.append(i.text)

print(a)
