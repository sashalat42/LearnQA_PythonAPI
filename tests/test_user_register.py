import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    #Создание пользователя с некорректным email - без символа @
    def test_create_user_with_wrong_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", f"Unexpected response content {response.content}"

    #Создание пользователя без указания одного из полей
    empty_fields = [
        'username',
        'firstName',
        'lastName',
        'email',
        'password'
    ]

    @pytest.mark.parametrize('field', empty_fields)
    def test_create_user_without_required_fields(self, field):
        data = self.prepare_registration_data()

        del data[field]

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {field}", f"Unexpected response content {response.content}"

    #Создание пользователя с очень коротким именем в один символ
    def test_create_user_with_short_username(self):
        data = self.prepare_registration_data()
        data['username'] = 'l'

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short", f"Unexpected response content {response.content}"

    #Создание пользователя с очень длинным именем - длиннее 250 символов
    def test_create_user_with_long_username(self):
        data = self.prepare_registration_data()
        data['username'] = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium q'

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long", f"Unexpected response content {response.content}"
