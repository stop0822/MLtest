from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mnist',methods=['GET','POST'])
def mnist():
    if request.method == 'GET':
        return render_template('mnistform.html')
    else:
         f = request.files['mnistfile']
        path = os.path.dirname(__file__)+'/upload/'+f.filename
        f.save(path)
        return ★★★★★

if __name__ == '__main__':
    app.run(debug=True)