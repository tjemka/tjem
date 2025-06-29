import subprocess
import time

# Путь к вашему main.py
file_path = r"C:\Users\gygyg\Desktop\прога\GG MINES BOT\bot\start.bat"

# Интервал в секундах (30 минут = 1800 секунд)
interval = 1200

# Переменная для хранения процесса
current_process = None

def run_file():
    global current_process

    # Если процесс уже существует, закрываем его
    if current_process is not None:
        current_process.terminate()  # Отправляем сигнал на завершение процесса
        current_process.wait()  # Ждем завершения

    # Указываем правильный рабочий каталог
    current_process = subprocess.Popen(
        ["python", file_path],
        cwd=r"C:\Users\gygyg\Desktop\bot",  # Указываем рабочий каталог
        creationflags=subprocess.CREATE_NEW_CONSOLE,  # Открываем в новой консоли (Windows)
        shell=False
    )

# Бесконечный цикл, который каждые 30 минут запускает файл
while True:
    run_file()
    time.sleep(interval)