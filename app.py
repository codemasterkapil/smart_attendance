from flask import Flask, render_template, Response
from backend.detection_engine import gen_frames

app=Flask(__name__)

# API endpoints
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/marked')
def marked():
    return render_template('marked.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
    app.run(debug=True)
