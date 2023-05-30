from flask import Flask, render_template, Response
import cv2
import numpy as np
import time
import datetime
import sys

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
num = 3

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title': 'Image Streaming',
        'time': timeString
    }
    return render_template('index.html', **templateData)


def gen_frames():
    camera = cv2.VideoCapture(0)
    width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = 30

    time.sleep(0.2)
    lastTime = time.time()*1000.0
    while True:
        ret, image = camera.read()

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=6)
        delt = time.time()*1000.0-lastTime
        s = str(int(delt))
        # print (delt," Found {0} faces!".format(len(faces)) )
        lastTime = time.time()*1000.0
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.circle(image, (int(x+w/2), int(y+h/2)),
                       int((w+h)/3), (255, 255, 255), 3)
        cv2.putText(image, s, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 255, 0), 2)
        now = datetime.datetime.now()
        timeString = now.strftime("%Y-%m-%d %H:%M")
        cv2.putText(image, timeString, (10, 45),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        # cv2.imshow("Frame", image)

        key = cv2.waitKey(1) & 0xFF
     # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

        ret, buffer = cv2.imencode('.jpg', image)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
    camera.release()
    cv2.destroyAllWindows()

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run()