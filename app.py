import os
import PIL.Image
from flask import Flask, request, redirect
from flask import render_template, session
from flask_session import Session

from utils import process_image


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.secret_key = 'BAD_SECRET_KEY'
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def check_allowed_file(filename): return True
def secure_filename(filename): return filename


@app.route("/",methods=['POST'])
def index_post():
    context = {}

    print('post', request.files)
    if 'file' not in request.files:
        print('No file attached in request')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        print('No file selected')
        return redirect(request.url)

    if not (file and check_allowed_file(file.filename)):
        return redirect(request.url)

    filename = secure_filename(file.filename)
    img = PIL.Image.open(file.stream)

    os.makedirs("static/temp", exist_ok=True)
    processed_image = process_image(img).image
    processed_image.save(f"static/temp/{filename}")

    if not session.get("images"): session["images"] = []
    session["images"].append({"path" : f"temp/{filename}"})
    context["images"] = session["images"]
    return render_template('display.html', context=context), 200


@app.route("/",methods=['GET'])
def index_get():
    context = {}
    if not session.get("images"): session["images"] = []
    context["images"] = session["images"]
    return render_template('display.html', context=context), 200


if __name__ == '__main__':
    app.run()
