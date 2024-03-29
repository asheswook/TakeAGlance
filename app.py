from flask import Flask, render_template, Response,request, url_for
import datetime
from frame import *
import VisageSnap
from add_csv import save_data_to_csv, csv_data_visualization, vs_in_csv_confirm, csv_to_dict


app = Flask(__name__)
vs = VisageSnap.Core()
vs.load_model()
vs.set_label(["jaewook", "haehyeon", "taeyoung", "jihun"])
# vs.train_labeled_data()
vs.threshold = 0.42

UPLOAD_FOLDER = 'image'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/introduce')
def index():
    return render_template('introduce.html')

@app.route('/')
def recog():
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
    if request.method=='GET':
        csv_data=csv_to_dict() # csv 데이터를 dict으로 가져오기.
        if len(csv_data)==0:
            csv_data={}
        print(csv_data, 'ddddddddddddddddddd') # 이게 왜 작동을 안 하지...?
        for get_face in vs.get_faces(): # vs로 학습한 데이터가 csv데이터에 있는지 확인 이후 추가 유무 확인.
            vs_row=[get_face.label, get_face.filenames[0]]
            vs_in_csv_confirm(vs_row, csv_data=csv_data)
            csv_data=csv_to_dict()
            
        trs=csv_data_visualization() # html 파일 table에 값 형성.
        
    if request.method=='POST':
        
        img_label=request.form['label']
        img_file=request.files['image']
        image_path='static/images/' + img_file.filename
        img_file.save(image_path)
        if img_label in list(csv_data.keys()) or image_path in list(csv_data.values()): # 이미 csv에 있을 때.
            trs=csv_data_visualization()  # çsv에 저장은 안하고 그냥 csv 파일만 보여줌.
        else:
            save_data_to_csv(img_label=img_label, img_path=image_path)
            trs=csv_data_visualization()
        return render_template('train.html', trs=trs) # 그냥 전체 re-rendering 함.
        
    
    return render_template('train.html', trs=trs)

if __name__ == '__main__':
    app.run(port=8000, debug=True)