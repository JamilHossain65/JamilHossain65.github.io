import os
import speech_recognition as sr
#from flask import Flask, request, abort, jsonify, send_from_directory

from flask import Flask, flash, request, redirect, url_for,jsonify
from werkzeug.utils import secure_filename

#https://www.youtube.com/watch?v=BNBjJ5AvTG0
UPLOAD_DIRECTORY = "/Users/jamil/Desktop"
ALLOWED_EXTENSIONS = {'flac', 'wav'}

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_DIRECTORY

courses = [
{'id':"0",'name':"Jamil"},
{'id':"1",'name':"Aliyar"},
{'id':"2",'name':"Eti"},
]

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def getText(name):
    r = sr.Recognizer()
    with sr.AudioFile(name) as source:
         r.adjust_for_ambient_noise(source)
         audio = r.listen(source)
         text = r.recognize_google(audio,language='en')
         # remove file after converting text
         os.remove(UPLOAD_DIRECTORY +'/'+ name)
         return text
    
@app.route('/convert/voice', methods=['POST'])
def convertSpeech():
    print(request.files)
    file = request.files['file']
    if file and allowed_file(file.filename):
       filename = secure_filename(file.filename)
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    return jsonify({'convert text':getText(filename)})

@app.route('/user/list', methods=['GET'])
def getUser():
    return jsonify({'courses':courses})

@app.route('/')
def hello_world():
    print("This will print Hello, World!")
    return 'Hello, World!'

app.run()

