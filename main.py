import face_recognition
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import VisageSnap
from dataclasses import dataclass
import os

@dataclass
class Label:
    value: list[str]


# Tkinter GUI
window = tk.Tk()
window.title("얼굴 인증 시스템")
window.geometry("640x600")

recog_frame = tk.Frame(window)
train_frame = tk.Frame(window)

recog_frame.grid(row=0, column=0, sticky="nsew")
train_frame.grid(row=0, column=0, sticky="nsew")

recog_frame.pack()
train_frame.pack()

def show_frame(frame: tk.Frame):
    frame.tkraise()

# Recog 부분

def start_recog_webcam():
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        raise ValueError('Falled to open.')

    ret, frame = video_capture.read()
    

start_recog_button = tk.Button(recog_frame, text="Start Recog", command=start_recog_webcam)
start_recog_button.pack()

# Train 부분
def start_train_webcam():
    pass

start_train_button = tk.Button(train_frame, text="Start Train", command=start_train_webcam)
start_train_button.pack()

name_entry = tk.Entry(train_frame)
name_entry.pack()


vs = VisageSnap.Core()
base_label = Label(["biden", "haehyeon", "jaewook"])

def train(name):
    base_label.value.append(name)
    vs.set_label(base_label.value)
    vs.train_labeled_data()

def load_image(name) -> str:  # 파일을 labeled 폴더에 저장하고, 옮겨진 파일의 경로를 반환
    file_path = filedialog.askopenfilename(initialdir="./jpg", title="학습할 사진 파일 선택", filetypes=(("jpg 사진 파일", "*.jpg")))
    print(file_path)

    with open(file_path, "rb") as f:
        data = f.read()
        
        # Check if the file is already exist
        for i in range(1, 1000):
            if not os.path.exists(f"./labeled/{name}-{i}.jpg"):
                name = f"{name}-{i}"
                break

        # Save the file
        with open(f"./labeled/{name}.jpg", "wb") as f2:
            f2.write(data)

    return f"./labeled/{name}.jpg"




window.mainloop()







