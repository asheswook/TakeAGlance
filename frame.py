import cv2
import time
import sys
import face_recognition
from app import *
from VisageSnap import To


def gen_frames():
    camera = cv2.VideoCapture(0)
    width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = 30

    time.sleep(0.2)
    lastTime = time.time()*1000.0
    
    while True:
        try:
            ret, frame = camera.read()

            # 1/4 size
            small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        except:
            print("Error: ", sys.exc_info()[0])
            camera = cv2.VideoCapture(0)
            continue

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_locations = [(top*2, right*2, bottom*2, left*2) for top, right, bottom, left in face_locations]

        face_names = []
        for encoding in face_encodings:
            prediction = vs.predict_encoding(encoding)
            print(prediction)

            name = vs.convert_labelType(prediction, To.NAME)
            face_names.append(name)
            print(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            name = "Unknown" if name == None else name
            cv2.circle(frame, (int((left+right)/2), int((top+bottom)/2)), int((right-left)/2), (255, 255, 255), 3)
            cv2.putText(frame, name, (left+3, bottom+22), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        now = time.time()*1000.0
        fps = 1000.0/(now-lastTime)
        lastTime = now
        cv2.putText(frame, "FPS: "+str(int(fps)), (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        key = cv2.waitKey(1) & 0xFF

     # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
        
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    camera.release()
    cv2.destroyAllWindows()