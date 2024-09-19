import os
import cv2
import numpy as np
import tensorflow as tf

# 加载人脸检测级联分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 加载人脸情绪识别模型
model = tf.keras.models.load_model('./emotion_detection_model.h5')
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
input_size = 48


def detect_emotion(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 16)
        face_img = gray[y:y + h, x:x + w]
        resized_face = cv2.resize(face_img, (input_size, input_size))
        normalized_face = resized_face / 255.0
        expanded_face = np.expand_dims(normalized_face, axis=-1)
        expanded_face = np.expand_dims(expanded_face, axis=0)
        prediction = model.predict(expanded_face)
        emotion_label = np.argmax(prediction)
        cv2.putText(image, emotion_labels[emotion_label], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 24, (255, 0, 0),
                    thickness=32)
    return image

if __name__ == '__main__':
    img = cv2.imread('img.png')
    res = detect_emotion(img)
    cv2.imshow('test', res)
    cv2.waitKey(0)