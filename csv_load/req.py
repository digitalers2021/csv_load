import requests

def usando_httpbin():
    res = requests.get("https://www.httpbin.org/get")
    data = res.json()
    print(data["headers"]["User-Agent"])


res = requests.post("https://www.httpbin.org/post", data={"id": "pepe", "username": "jose"})
print(res.json())
