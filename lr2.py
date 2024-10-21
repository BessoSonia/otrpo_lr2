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

# Рисуем прямоугольники вокруг лиц
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Отображение изображения с детектированными лицами
cv2.imshow('Image with faces', image)

# Ожидание нажатия любой клавиши и закрытие окна
cv2.waitKey(0)
cv2.destroyAllWindows()
