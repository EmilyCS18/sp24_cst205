from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    return '''
    <p>Emily C. : OMG</p>
    <p>Claire L. : lmao</p>
    <p>Parker M. : yuh</p>
    '''

@app.route('/emily')
def emily():
    return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)
