import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Set the path to the directory containing the images
path = "C:\\Users\\vyshg\\Downloads\\attendance system\\ImagesAttendance"
images = []
classNames = []
myList = os.listdir(path)
print("Files found in directory:", myList)

# Load images and corresponding class names
for cls in myList:
    curImg = cv2.imread(os.path.join(path, cls))
    if curImg is not None:  # Check if the image is loaded correctly
        images.append(curImg)
        classNames.append(os.path.splitext(cls)[0])  # Remove file extension from the class name
    else:
        print(f"Warning: Could not load image {cls}. It may be corrupted or not an image file.")

# Function to find encodings for all images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

# Function to mark attendance in a CSV file
def markAttendance(name):
    with open('attendance.csv', 'r+') as f:  # Open the CSV file
        myDataList = f.readlines()
        nameList = []

        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        Attendance = 'present'

        # Write to the CSV file if the name is not already listed
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            Date = now.strftime("%d/%m/%y")
            f.writelines(f'\n{name},{dtString},{Date},{Attendance}')

# Find encodings of known images
if images:  # Ensure there are images to process
    encodeListKnown = findEncodings(images)
    print("Encoding complete")

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to capture image from webcam. Exiting...")
            break

        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # Resize frame to 1/4 for faster processing
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        # Detect face locations and encodings in the current frame
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # Scale back to original frame size
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)

        cv2.imshow('Webcam', img)  # Display the webcam feed with detected faces
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
else:
    print("No valid images found in the directory.")
