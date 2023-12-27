import os
import requests
import threading
import multiprocessing
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def create_download_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


async def download_image_async(url, folder="downloads"):
    try:
        start_time = time.time()
        response = await loop.run_in_executor(None, lambda: requests.get(url, stream=True))
        end_time = time.time()
        if response.status_code == 200:
            image_name = os.path.join(folder, url.split("/")[-1])
            with open(image_name, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded {url} to {image_name} in {end_time - start_time:.2f} seconds")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


def download_image_thread(url, folder="downloads"):
    try:
        start_time = time.time()
        response = requests.get(url, stream=True)
        end_time = time.time()
        if response.status_code == 200:
            image_name = os.path.join(folder, url.split("/")[-1])
            with open(image_name, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded {url} to {image_name} in {end_time - start_time:.2f} seconds")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


def download_image_process(url, folder="downloads"):
    try:
        start_time = time.time()
        threading.Thread(target=download_image_thread, args=(url, folder)).start()
        end_time = time.time()
        print(f"Started download process for {url} in {end_time - start_time:.2f} seconds")
    except Exception as e:
        print(f"Error starting download process for {url}: {e}")


if __name__ == "__main__":
    urls = ["https://img3.fonwall.ru/o/zy/cat-wildlife-zoo-gray.jpeg?auto=compress&fit=resize&w=1200&display=large",
            "https://img3.fonwall.ru/o/fw/frohes-neues-jahr-christmas-toys-sleet.jpg?auto=compress&fit=resize&w=1200&display=large",
            "https://img3.fonwall.ru/o/vo/panther-predator-a-cat-knhg.jpg?auto=compress&fit=resize&w=1200&display=large"]
    folder_name = "downloads"
    create_download_folder(folder_name)

    start_time = time.time()

    # Asynchronous approach
    loop = asyncio.get_event_loop()
    tasks = [download_image_async(url, folder_name) for url in urls]
    loop.run_until_complete(asyncio.gather(*tasks))

    # Multi-threading approach
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        executor.map(download_image_thread, urls, [folder_name]*len(urls))

    # Multi-processing approach
    with ProcessPoolExecutor(max_workers=len(urls)) as executor:
        executor.map(download_image_process, urls, [folder_name]*len(urls))

    end_time = time.time()

    print(f"Total time: {end_time - start_time} seconds")
