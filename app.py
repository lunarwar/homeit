from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_from_directory, send_file
from flask_cors import CORS
import random
import os
from werkzeug.utils import secure_filename
import webbrowser
import hashlib


app = Flask(__name__)
CORS(app)
app.secret_key = '!@#$%^^7'

@app.route('/')
def default_page():
    return render_template('homeIT.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=45575)
