# Author: Kyla Moore
# Created: 02/1/2022
# Course: ITSC 3155

import requests

r = requests.get("https://www.charlotte.edu/")

print(r.text)
