import requests
import threading


def download_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки в запросе
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error downloading {url}: {e}"


def save_to_file(url, data):
    with open(f"{url.split('//')[1].replace('/', '_')}.html", 'w', encoding='utf-8') as file:
        file.write(data)


def download_and_save(url):
    data = download_url(url)
    save_to_file(url, data)
    print(f"Downloaded and saved {url}")


def main():
    print("Start downloading")
    urls = [
        'https://gb.ru',
        'https://www.ozon.ru',
        'https://www.youtube.com',
        'https://mail.ru',
    ]

    threads = []
    for url in urls:
        thread = threading.Thread(target=download_and_save, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
