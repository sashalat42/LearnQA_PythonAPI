import requests

#Делает http-запрос любого типа без параметра method.
response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"Если запрос без параметра method ответ {response1.text}")

#Делает http-запрос не из списка.
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(f"Если http-запрос не из списка ответ {response2.text}")

#Делает запрос с правильным значением method.
response3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print(f"Когда запрос совпадает с правильным значением method ответ {response3.text}")

#С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
methods = ["GET", "POST", "PUT", "DELETE"]
for method in methods:
    payload = {"method":method}
    response4=requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
    print(f"Для метода GET с параметром {payload['method']} ответ {response4.text}")
for method in methods:
    payload = {"method":method}
    response4=requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f"Для метода POST с параметром {payload['method']} ответ {response4.text}")
for method in methods:
    payload = {"method":method}
    response4=requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f"Для метода PUT с параметром {payload['method']} ответ {response4.text}")
for method in methods:
    payload = {"method":method}
    response4=requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f"Для метода DELETE с параметром {payload['method']} ответ {response4.text}")