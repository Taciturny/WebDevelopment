from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'This is my first flask project'

@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed and his mark is '+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed and his mark is '+ str(score)

if __name__=='__main__':
    app.run(debug=True)