
import face_recognition
import cv2
import numpy as np
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import VisageSnap
from VisageSnap import To
from dataclasses import dataclass
# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("labeled/obama-1.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("labeled/biden-1.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

jaewook_image = face_recognition.load_image_file("labeled/jaewook-1.jpg")
jaewook_face_encoding = face_recognition.face_encodings(jaewook_image)[0]

haehyeon_image = face_recognition.load_image_file("labeled/haehyeon-1.jpg")
haehyeon_face_encoding = face_recognition.face_encodings(haehyeon_image)[0]

# taeyoung_image = face_recognition.load_image_file("taeyoung.jpg")
# taeyoung_face_encoding = face_recognition.face_encodings(taeyoung_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding,
    jaewook_face_encoding,
    haehyeon_face_encoding
]
known_face_names = [
    "Barack Obama",
    "Joe Biden",
    "Jaewook",
    "Haehyeon"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

vs = VisageSnap.Core()
base_label = ["biden", "haehyeon", "jaewook"]

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_this_frame: 
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)


        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            numlabel = vs.predict_encoding(face_encoding)
            name = vs.convert_labelType(numlabel, To.NAME)

            face_names.append(name)
            print(numlabel)

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)
    # real_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # img = ImageTk.PhotoImage(Image.fromarray(real_frame))
    # canvas.create_image(0, 0, anchor=NW, image=img)
    # app.update()


    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break





# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()