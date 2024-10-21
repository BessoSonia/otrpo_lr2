# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем зависимости для OpenCV
RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev wget

# Устанавливаем OpenCV
RUN pip install opencv-python-headless

# Скачиваем классификатор каскада Хаара для обнаружения лиц
RUN wget https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml -P /app

# Копируем приложение и изображение в контейнер
COPY lr2.py /app/lr2.py
COPY image.jpg /app/image.jpg

# Устанавливаем рабочую директорию
WORKDIR /app

# Запуск приложения
CMD ["python", "lr2.py"]

