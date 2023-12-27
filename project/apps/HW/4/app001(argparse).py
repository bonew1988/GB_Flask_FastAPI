import argparse
import os
import requests
import threading
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
            print(
                f"Downloaded {url} to {image_name} in {end_time - start_time:.2f} seconds")
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
            print(
                f"Downloaded {url} to {image_name} in {end_time - start_time:.2f} seconds")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


def download_image_process(url, folder="downloads"):
    try:
        start_time = time.time()
        threading.Thread(target=download_image_thread,
                         args=(url, folder)).start()
        end_time = time.time()
        print(
            f"Started download process for {url} in {end_time - start_time:.2f} seconds")
    except Exception as e:
        print(f"Error starting download process for {url}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Download images from URLs.")
    parser.add_argument("urls", nargs="+", help="URLs of images to download.")
    parser.add_argument("--folder", default="downloads",
                        help="Folder to save the downloaded images.")
    args = parser.parse_args()

    create_download_folder(args.folder)

    start_time = time.time()

    # Asynchronous
    loop = asyncio.get_event_loop()
    tasks = [download_image_async(url, args.folder) for url in args.urls]
    loop.run_until_complete(asyncio.gather(*tasks))

    # Multi-threading
    with ThreadPoolExecutor(max_workers=len(args.urls)) as executor:
        executor.map(download_image_thread, args.urls,
                     [args.folder] * len(args.urls))

    # Multi-processing
    with ProcessPoolExecutor(max_workers=len(args.urls)) as executor:
        executor.map(download_image_process, args.urls,
                     [args.folder] * len(args.urls))

    end_time = time.time()

    print(f"Total time: {end_time - start_time} seconds")


if __name__ == "__main__":
    main()
