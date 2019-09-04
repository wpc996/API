import requests

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()

#处理结束
print(response_dict.keys())