import random
import time
import threading
import multiprocessing
import asyncio


def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]


def sum_array(arr):
    return sum(arr)


def multithreaded_sum(arr):
    start_time = time.time()

    result = 0
    num_threads = 4  # Количество потоков

    def worker(start, end):
        nonlocal result
        result += sum_array(arr[start:end])

    threads = []
    step = len(arr) // num_threads

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i < num_threads - 1 else len(arr)
        thread = threading.Thread(target=worker, args=(start, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(
        f"Multithreaded sum: {result}, Time: {end_time - start_time:.5f} seconds")


def multiprocessing_sum(arr):
    start_time = time.time()

    num_processes = 4  # Количество процессов
    step = len(arr) // num_processes
    chunks = [arr[i:i+step] for i in range(0, len(arr), step)]

    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(sum_array, chunks)

    result = sum(results)

    end_time = time.time()
    print(
        f"Multiprocessing sum: {result}, Time: {end_time - start_time:.5f} seconds")


async def async_sum(arr):
    return sum_array(arr)


async def asynchronous_sum(arr):
    start_time = time.time()

    result = await async_sum(arr)

    end_time = time.time()
    print(
        f"Asynchronous sum: {result}, Time: {end_time - start_time:.5f} seconds")


async def main():
    size = 1000000
    arr = generate_random_array(size)

    multithreaded_sum(arr)
    multiprocessing_sum(arr)
    await asynchronous_sum(arr)

if __name__ == "__main__":
    asyncio.run(main())
