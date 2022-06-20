
import requests

url = "http://127.0.0.1:5000/pair/20"
response=requests.get(url=url)
print(response)
for i in list(response):
    print(i)