#!/usr/bin/python
import sys    #comand line argument
import requests  #to download
import bs4  #beautifulsoup to extract data

res = reuests.get('https://en.wikipedia.org/wiki/' + ''.join(sys.argv[1:]))
res.raise_for_status()  #just to raise the status code
wiki = bs4.BeautifulSoup(res.text, "html.parser")
for i in wiki.select('p'):
    print(i.getText())