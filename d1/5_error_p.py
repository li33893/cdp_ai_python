import requests

#  0. https://jsonplaceholder.typicode.com/posts/1
try:
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    resp.raise_for_status()
    print(f"请求成功，",resp.status_code)
except requests.exceptions.HTTPError as e:
    print(f"请求失败，",e)

#  1.请求一个成功的URL、一个失败的URL，都用 try/except 包起来，打印出不同的提示信息 
try: 
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/9999")
    resp.raise_for_status()
    print(f"请求成功，",resp.status_code)
except requests.exceptions.HTTPError as e:
    print(f"请求失败，",e)
