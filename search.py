import urllib.request
import time
import numpy as np
from bs4 import BeautifulSoup

word = input()
search = f"{word}%20definition"

url = f"https://www.google.com/search?&q={search}"

req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
    }
)

r = urllib.request.urlopen(req).read()

result = BeautifulSoup(r, "html.parser")
result = str(result.get_text())
result = result[result.find(word+";"):result.find("Definitions")]
result = result.split(';')
print(result)
#print(result.prettify())

time.sleep(15)
