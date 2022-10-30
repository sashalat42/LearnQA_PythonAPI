import pytest
import requests


class TestUserAgent:
    payload = [
        {'user': 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', 'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
        {'user': 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1', 'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
        {'user': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
        {'user': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0', 'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
        {'user': 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1', 'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
    ]

    @pytest.mark.parametrize('data', payload)
    def test_user_agent(self, data):

        response = requests.get('https://playground.learnqa.ru/ajax/api/user_agent_check', headers={'User-Agent': data['user']})

        assert 'platform' in response.json(), 'There is no field platform in the response'
        assert 'browser' in response.json(), 'There is no field browser in the response'
        assert 'device' in response.json(), 'There is no field device in the response'

        platform = response.json()['platform']
        browser = response.json()['browser']
        device = response.json()['device']

        assert data['platform'] == platform, 'Platform for user agent is not equal to expected platform'
        assert data['browser'] == browser, 'Browser for user agent is not equal to expected browser'
        assert data['device'] == device, 'Device for user agent is not equal to expected device'
