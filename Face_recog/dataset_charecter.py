import cv2
import os
import pickle
import numpy as np


video = cv2.VideoCapture(0)
faceDetect = cv2.CascadeClassifier(r'C:\Users\bisha\Documents\Desktop_Files\Python Projects\Face_recog\haarcascade_frontalface_default.xml')

face_data = []
i = 0


name = input("Enter Your Name: ")

while True:
    ret, frame = video.read()

    # Check if frame is captured correctly
    if not ret:
        print("Failed to capture video. Exiting.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resize_img = cv2.resize(crop_img, (50, 50))
        if len(face_data) <= 100 and i % 10 == 0:
            face_data.append(resize_img)
            cv2.putText(frame, str(len(face_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)

    cv2.imshow("Frame", frame)

    # Stop the loop when 50 faces are collected
    if len(face_data) == 50:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video and close windows
video.release()
cv2.destroyAllWindows()

# Reshape the collected face data
face_data = np.array(face_data)
face_data = face_data.reshape(50, -1)

# Saving the names and face data
if 'names.pkl' not in os.listdir('data/'):
    names = [name] * 50
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)
else:
    with open('data/names.pkl', 'rb') as f:
        names = pickle.load(f)
    names = names + [name] * 50
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)

if 'face_data.pkl' not in os.listdir('data/'):
    with open('data/face_data.pkl', 'wb') as f:
        pickle.dump(face_data, f)
else:
    with open('data/face_data.pkl', 'rb') as f:
        faces = pickle.load(f)
    faces = np.append(faces, face_data, axis=0)
    with open('data/face_data.pkl', 'wb') as f:
        pickle.dump(faces, f)


# import cv2
# import os
# import pickle
# import numpy as np
# import sqlite3


# video = cv2.VideoCapture(0)
# faceDetect = cv2.CascadeClassifier(r'C:\Users\bisha\Documents\Desktop_Files\Python Projects\Face_recog\haarcascade_frontalface_default.xml')

# face_data = []

# i = 0

# name = input("Enter Your Name: ")

# while True:
#     ret,frame = video.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = faceDetect.detectMultiScale(gray, 1.3, 5)

#     for (x,y,w,h) in faces:
#         crop_img = frame[y:y+h,x:x+w,:]
#         resize_img = cv2.resize(crop_img,(50,50))
#         if len(face_data)<=100 and i % 10 == 0:
#             cv2.putText(frame,str(len(face_data)), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50.255), 1)
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
        
#         cv2.imshow("frame",frame)
#         k = cv2.waitKey(1)
#         if len(face_data) == 50:
#             break

#     video.release()
#     cv2.destroyAllWindows()

#     face_data = np.array(face_data)
#     face_data = face_data.reshape(100, -1)
    
#     if 'names.pkl' not in os.listdir('data/'):
#         names = [name]*100
#         with open('data/names.pkl','wb') as f:
#             pickle.dump(names,f)
#     else:
#         with open('data/names.pkl','rb') as f:
#             names = pickle.load(f)
#         names = names + [name] * 100

#         with open('data/face_data.pkl','wb') as f:
#             pickle.dump(names,f)
#     if 'face_data.pkl' not in os.listdir('data/'):
#         with open('data/face_data.pkl','wb') as f:
#             pickle.dump(face_data,f)
#     else:
#         with open('data/face_data.pkl','rb') as f:
#             faces = pickle.load(f)
#         faces = np.append(faces,face_data,axis=0)
#         with open('data/face_data.pkl','wb') as f:
#             pickle.dump(faces,f)        

# def insert_update(ID,Name,age):
#     connection = sqlite3.connect("database.db")
#     cmd = "SELECT * FROM STUDENTS WHERE ID = "+str(ID)
#     cursor = connection.execute(cmd)
#     isRecodExist = 0
#     for row in cursor:
#         isRecodExist=1
#     if(isRecodExist==1):
#         connection.execute("UPDATE STUDENT SET Name = ? Where ID = ?",(Name,ID,))
#         connection.execute("UPDATE STUDENT SET age = ? Where ID = ?",(age,ID,))
#     else:
#         connection.execute("INSERT INTO STUDENTS(ID,Name,age) Value(?,?,?)",(ID,Name,age))

#     connection.commit()
#     connection.close()
