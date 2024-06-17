import os
import time
path = 'C:/Windows/help'
for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        full_file_path = os.path.join(dirpath, file)
        filetime = os.path.getatime(full_file_path)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(full_file_path)
        parent_dir = os.path.dirname(full_file_path)
        print(f'Обнаружен файл: {file}, Путь: {full_file_path}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
