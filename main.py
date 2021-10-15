#!flask/bin/python
import sys
from flask import Flask, render_template, request, redirect, Response
import random, json, csv

def writecsv(l):
    with open('logs.csv','a') as fd:
            writer = csv.writer(fd)
            writer.writerow(l)

app = Flask(__name__)
@app.route('/')
def output():
	# serve index template
	return render_template('index.html')

@app.route('/receivedata', methods=['POST'])
def receive_data():
    writecsv([request.form['Instance'], request.form['Time']])

    return 'OK', 200

if __name__ == '__main__':
	# run!
	app.run()