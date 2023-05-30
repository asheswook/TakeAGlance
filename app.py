from flask import Flask, render_template, Response,request, url_for
import os
import datetime
from frame import *
import VisageSnap
import csv
from add_csv import save_data_to_csv, reading_csv_Data


app = Flask(__name__)
vs = VisageSnap.Core()
vs.load_model()
vs.set_label(["biden", "obama", "jaewook", "haehyeon"])

UPLOAD_FOLDER = 'image'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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

@app.route('/video_feed')
def video_feed(): 
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/train', methods=['GET', 'POST'])
def train():
    # csv 파일 데이터 확인
    trs=reading_csv_Data()
    
    if request.method=='POST':
        print('post method activated')
        img_label=request.form['label']
        img_file=request.files['image']
        image_path='static/images/' + img_file.filename
        img_file.save(image_path)
        save_data_to_csv(img_label=img_label, img_path=image_path)
        trs=reading_csv_Data()
        return render_template('train.html', trs=trs) # 그냥 전체 re-rendering 함.
        
    
    return render_template('train.html', trs=trs)

if __name__ == '__main__':
    app.run(port=8000, debug=True)