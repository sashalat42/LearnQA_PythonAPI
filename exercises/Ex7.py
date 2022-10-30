import requests

# Делает http-запрос любого типа без параметра method.
response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"Если запрос без параметра method ответ {response1.text}")

# Делает http-запрос не из списка.
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"Если http-запрос не из списка ответ {response2.text}")

# Делает запрос с правильным значением method.
response3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print(f"Когда запрос совпадает с правильным значением method ответ {response3.text}")

# С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
methods = ["GET", "POST", "PUT", "DELETE"]
req = [requests.get, requests.post, requests.put, requests.delete]

for item in req:
    if item != requests.get:
        for method in methods:
            payload = {"method": method}
            response4 = item("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
            print(f"Для метода {item} с параметром {payload['method']} ответ {response4.text}")
    else:
        for method in methods:
            payload = {"method": method}
            response4 = item("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
            print(f"Для метода {item} с параметром {payload['method']} ответ {response4.text}")
