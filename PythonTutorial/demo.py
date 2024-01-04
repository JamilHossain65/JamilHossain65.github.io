import webbrowser

from flask import Flask, render_template, jsonify
app = Flask(__name__)

users = [
{'id':"0",'name':"Jamil"},
{'id':"1",'name':"Aliyar"},
{'id':"2",'name':"Eti"},
]

#@app.route('/')
#def index():
# return render_template('index.html')

@app.route('/')
def test():
  return 'Home Page Shown Successfully!'

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')
  #webbrowser.open('https://www.google.com') 
  return 'Click.'

@app.route('/user/list', methods=['GET'])
def getUser():
    return jsonify({'users': users})

if __name__ == '__main__':
  app.run(debug=True)
