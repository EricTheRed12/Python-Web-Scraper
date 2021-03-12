import requests
import time

from bs4 import BeautifulSoup

word = input()

url = "http://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_a.html"

r = requests.get(url)#urllib.request.urlopen(url).read()
print(r.status_code)

result = BeautifulSoup(r.text, "html.parser")

print(result.prettify())

#time.sleep(15)
