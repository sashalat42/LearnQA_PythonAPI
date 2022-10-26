import requests


def test_cookie():

    response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    print(dict(response.cookies))

    assert response.status_code == 200, "Wrong response code"
    assert "HomeWork" in response.cookies, "There is no field 'HomeWork' in the response"

    expected_value = response.cookies.get('HomeWork')
    assert expected_value == 'hw_value', "Cookie value is not correct"
