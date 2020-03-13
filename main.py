import argparse
import requests
from dotenv import load_dotenv
import os

BITLY_SERVICE_URL = 'https://api-ssl.bitly.com/v4/bitlinks'

def shorten_link(token, url):
    body = {"long_url": url}
    bitly_service_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(bitly_service_url, json=body, headers={'Authorization': token})
    return response.json()['link']

def count_click(token, bit_link):
    modified_bitlink = bit_link.split('//')[1]
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{modified_bitlink}/clicks/summary'
    params = {
        'unit': 'day',
        'units': '-1'
    }
    response = requests.get(url, headers={'Authorization': token}, params=params)
    response.raise_for_status()
    total_clicks = response.json()['total_clicks']
    return total_clicks
if __name__ == '__main__':
    load_dotenv()
    bitly_token = os.getenv("BITLY_TOKEN")
    parser = argparse.ArgumentParser(
        description='Создаёт короткую ссылку или возвращает количество переходов по короткой ссылке')
    parser.add_argument('url', help='Обрезанная или длинная ссылка')
    args = parser.parse_args()
    entered_url = args.url
    if entered_url.startswith("http://bit.ly"):
        try:
            total_clicks = count_click(bitly_token, entered_url)
            print(f'Количестве переходов по ссылке {total_clicks}')
        except requests.exceptions.HTTPError:
            print("Ошибка сервиса bitly.com")
        except KeyError:
            print("Ошибка в введенном названии сайта")
    else:
        try:
            bit_link = shorten_link(bitly_token, entered_url)
            print(bit_link)
        except requests.exceptions.HTTPError:
            print("Ошибка сервиса bitly.com")
        except KeyError:
            print("Ошибка в введенном названии сайта")
