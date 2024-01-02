from flask import Flask, render_template, request, jsonify
 
app = Flask(__name__,template_folder='template')
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/square/', methods=['POST'])
def square():
    print(request.form)
    num = float(request.form.get('number', 0))
    square = num ** 2
    data = {'square': square}
    data = jsonify(data)
    return data
 
app.run()
