import requests
from multiprocessing import Pool
import os


def download_and_save(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.text

        filename = f"downloaded_files/{url.split('//')[1].replace('/', '_')}.html"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(data)
        print(f"Downloaded and saved {url} to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")


def main():
    # Введите список URL-адресов
    urls = [
        'https://gb.ru',
        'https://www.ozon.ru',
        'https://www.youtube.com',
        'https://mail.ru',
        'https://www.google.com',
        'https://www.facebook.com',
        'https://www.instagram.com',
        'https://www.twitter'
        'https://www.linkedin.com'
        'https://www.pinterest.com'
        'https://www.reddit.com'
        'https://www.tumblr.com'
        'https://www.vk.com'
    ]

    if not os.path.exists('downloaded_files'):
        os.makedirs('downloaded_files')

    with Pool() as pool:
        pool.map(download_and_save, urls)


if __name__ == "__main__":
    main()
