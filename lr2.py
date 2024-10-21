import cv2
from cv2 import data 

# Загрузка классификатора для детектирования лиц (Haar Cascade)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Загрузка изображения
image = cv2.imread('image.jpg')

# Преобразование изображения в оттенки серого, так как детектор работает лучше с серыми изображениями
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Детектирование лиц
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(f"Обнаружено лиц: {len(faces)}")
