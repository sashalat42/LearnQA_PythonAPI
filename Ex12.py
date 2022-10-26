import requests


def test_header():
    response = requests.get("https://playground.learnqa.ru/api/homework_header")
    print(response.headers)

    assert response.status_code == 200, "Wrong response code"
    assert 'x-secret-homework-header' in response.headers, "There is no field 'x-secret-homework-header' in the response"

    expected_value = response.headers.get('x-secret-homework-header')
    assert expected_value == 'Some secret value', "Header value is not correct"
