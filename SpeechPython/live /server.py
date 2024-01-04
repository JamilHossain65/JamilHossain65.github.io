import os
import speech_recognition as sr
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename


UPLOAD_DIRECTORY = ""
ALLOWED_EXTENSIONS = {'flac', 'wav'}

# if not os.path.exists(UPLOAD_DIRECTORY):
#     os.makedirs(UPLOAD_DIRECTORY)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_DIRECTORY

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def getText(filepath):
    r = sr.Recognizer()
    with sr.AudioFile(filepath) as source:
         r.adjust_for_ambient_noise(source)
         audio = r.listen(source)
         text = r.recognize_google(audio,language='en')
         os.remove(filepath) # remove file after converting text
         return text

@app.route('/')
def test_live():
  return 'Live Test'

@app.route('/convert/voice', methods=['POST'])
def convertSpeech():
    file = request.files['file']
    if file and allowed_file(file.filename):
       filename = secure_filename(file.filename)
       filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
       file.save(filepath) #save audio file to this path
    return jsonify({'convert_speech':getText(filepath)})

if __name__ == '__main__':
  app.run(debug=False)
