from flask import Flask
import time
import datetime
import sys
import os
app = Flask(__name__)

port = int(os.getenv("PORT"))

@app.route('/')
def hello_world():
    ltime = str(datetime.datetime.now())
    return '<HTML><BODY>Hello World!' + ltime + ' h</BODY><HTML>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)
