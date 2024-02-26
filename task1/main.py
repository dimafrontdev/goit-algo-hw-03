import os
import shutil
import sys


def copy_and_sort_files(src, dest):
    try:
        # Створює директорію призначення, якщо вона не існує
        os.makedirs(dest, exist_ok=True)
        # Перебирає всі елементи в директорії src
        for item in os.listdir(src):
            item_path = os.path.join(src, item)
            # Якщо елемент є директорією, рекурсивно викликає функцію
            if os.path.isdir(item_path):
                copy_and_sort_files(item_path, dest)
            else:
                # Визначає розширення файлу, використовує 'no_extension', якщо розширення відсутнє
                file_ext = os.path.splitext(item)[1][1:].lower() or "no_extension"
                # Створює шлях до директорії на основі розширення файлу
                ext_dir = os.path.join(dest, file_ext)
                # Створює директорію, якщо вона не існує
                os.makedirs(ext_dir, exist_ok=True)
                # Копіює файл у відповідну директорію
                shutil.copy(item_path, ext_dir)
    except Exception as e:
        print(f"Error during processing: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [destination_directory]")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2] if len(sys.argv) > 2 else "dist"

    copy_and_sort_files(source_directory, destination_directory)
    print(
        f"Files have been successfully copied and sorted from '{source_directory}' to '{destination_directory}'."
    )
