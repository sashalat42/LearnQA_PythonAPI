import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
number_of_redirects = len(response.history)
last_url = response.url

print(f"Количество редиректов = {number_of_redirects}")
print(last_url)