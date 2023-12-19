import threading
import os


def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            word_count = len(content.split())
            print(f"File: {file_path}, количество слов: {word_count}")
    except Exception as e:
        print(f"Error counting words in {file_path}: {e}")


def main(directory_path):
    file_paths = [os.path.join(directory_path, file) for file in os.listdir(
        directory_path) if os.path.isfile(os.path.join(directory_path, file))]

    threads = []
    for file_path in file_paths:
        thread = threading.Thread(
            target=count_words_in_file, args=(file_path,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    
    directory_path = "/home/bonew/Рабочий стол/Flask_FastAPI/downloaded_files"
    main(directory_path)
