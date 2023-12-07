import requests
from itertools import combinations, product
import base64
import threading

#IP spoofing
url = "http://challenge01.root-me.org/web-serveur/ch68/"

header = {"X-Forwarded-For": "192.168.1.6"}
response = requests.get(url, headers = header)
print(response.text)