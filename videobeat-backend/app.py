from flask import Flask,request
from flask_cors import CORS, cross_origin
import csv

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

cors = CORS(app, resources={r'/*': {"origins": '*'}})
app.config['CORS_HEADER'] = 'Content-Type'

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
@cross_origin(origin='*', allow_headers=['Content-Type'])
def index():
    return 'Server'
    
@app.route('/uploadOne', methods = ['GET', 'POST'])
@cross_origin(origin='*',allow_headers=['Content-Type'])
def upload_file1():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return 'file uploaded succesfully'

@app.route('/uploadTwo', methods = ['GET', 'POST'])
@cross_origin(allow_headers=['Content-Type'])
def upload_file2():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return 'file uploaded succesfully'

if __name__ =="__main__":
    print("server is running")
    app.run()