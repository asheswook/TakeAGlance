from flask import Flask, render_template, Response
import datetime
from frame import *
import VisageSnap


app = Flask(__name__)
vs = VisageSnap.Core()
vs.load_model()
vs.set_label(["biden", "obama", "jaewook", "haehyeon"])

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

if __name__ == '__main__':
    app.run()