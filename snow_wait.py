import requests
import json

# 从文件中逐行读取电子邮件地址
with open('email.txt', 'r') as file:
    emails = file.readlines()

# 去除每行末尾的换行符
emails = [email.strip() for email in emails]

# 设置请求头
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,ay;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'xxxxxx',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://snowstorm.snowball.money/',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

# 对每个电子邮件地址发送请求
for email in emails:
    data = {
        "telegram": "",
        "email": email
    }
    
    response = requests.post(
        xxxxxxxxx',
        headers=headers,
        data=json.dumps(data)
    )
    
    # 打印每个响应的状态码和内容
    print(f"Email: {email} - Status Code: {response.status_code}")
    print(response.text)
