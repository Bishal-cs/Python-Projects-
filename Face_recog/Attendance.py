import os
import cv2 
import csv 
import time 
import pickle
import numpy as np
from datetime import datetime 
from sklearn.neighbors import KNeighborsClassifier

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(r'C:\Users\bisha\Documents\Desktop_Files\Python Projects\Face_recog\haarcascade_frontalface_default.xml')

with open('data/names.pkl','rb') as w:
    LABELS = pickle.load(w)

with open('data/face_data.pkl','rb') as f:
    FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

# Load background image
imagebackgroud = cv2.imread("bg.png") 

# Check if the image was loaded correctly
if imagebackgroud is None:
    print("Error: Background image not found. Please check the file path.")
    exit()

COL_NAMES = ['NAME', 'TIME']

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)

        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        exist = os.path.isfile(f"Attendance/Attendance_{date}.csv")

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
        cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(output[0]), (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 2)

        attendance = [str(output[0]), str(timestamp)]

    # Resize the frame to fit the background size
    frame_resized = cv2.resize(frame, (640, 480))
    imagebackgroud[160:160+480, 55:55+640] = frame_resized

    cv2.imshow("frame", imagebackgroud)

    k = cv2.waitKey(1)
    if k == ord('0'):
        time.sleep(5)

        if exist:
            with open(f'Attendance/Attendance_{date}.csv', "a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(attendance)
        else:
            with open(f'Attendance/Attendance_{date}.csv', "w") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)
        
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
