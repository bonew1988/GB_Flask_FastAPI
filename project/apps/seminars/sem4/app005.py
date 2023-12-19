import asyncio
import os
import aiofiles

async def count_words_in_file(file_path):
    try:
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
            content = await file.read()
            word_count = len(content.split())
            print(f"File: {file_path}, Word Count: {word_count}")
    except Exception as e:
        print(f"Error counting words in {file_path}: {e}")

async def process_files(directory_path):
    file_paths = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]
    tasks = [count_words_in_file(file_path) for file_path in file_paths]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    directory_path = "/home/bonew/Рабочий стол/Flask_FastAPI/downloaded_files"
    asyncio.run(process_files(directory_path))
