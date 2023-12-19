import aiohttp
import asyncio
import os


async def download_and_save(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.text()

            filename = f"downloaded_files/{url.split('//')[1].replace('/', '_')}.html"
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(data)
            print(f"Downloaded and saved {url} to {filename}")

    except aiohttp.ClientError as e:
        print(f"Error downloading {url}: {e}")


async def main():
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

    async with aiohttp.ClientSession() as session:
        tasks = [download_and_save(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
