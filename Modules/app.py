from flask import Flask, render_template, request
import threading
import time
import sys
import imageconverter
import pyrecorder
import MongoDBcon
import summarize
import background

app = Flask(__name__)
topic = ""
name = ""
dur = ""
s=""
 
val = 0

def getVal():
    return val

def fun(arg):
    runtime = int(arg)*100
    t = time.time()
    while 1:
        imageconverter.convert()
        if((time.time()-t)<runtime):
            print("done")
        else:
            sys.exit()

@app.route('/')
def index():
    if getVal() == 0:
        return render_template('admin.html')
    else:
        return render_template('error.html')

val = 0
@app.route('/start', methods=['POST'])
def start():
    if getVal() == 0:
        topic = request.form['topic']
        name = request.form['name']
        dur = request.form['dur']
        s = topic+","+name+","+dur
        global val 
        val = 1
        back_thread1 = threading.Thread(target=background.start_back, args=(s,))
        back_thread2 = threading.Thread(target=fun, args=(dur,))
        back_thread3 = threading.Thread(target=pyrecorder.recog, args=(int(dur)*100,))
        back_thread1.start()
        back_thread2.start()
        back_thread3.start()
        return render_template('start.html')

    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6969)
