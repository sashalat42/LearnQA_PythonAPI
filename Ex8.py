import requests
import time
import json

response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
answer = json.loads(response.text)

payload = {'token': answer["token"]}
before = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=payload)
print(before.text)

time.sleep(answer["seconds"])
after = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=payload)
print(after.text)
