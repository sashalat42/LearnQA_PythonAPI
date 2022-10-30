import requests
import time

response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
answer = response.json()

payload = {'token': answer["token"]}
before = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=payload)
not_ready = before.json()
print(not_ready['status'])

time.sleep(answer["seconds"])
after = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=payload)
ready = after.json()
print(f"{ready['status']}! Your result is {ready['result']}")
