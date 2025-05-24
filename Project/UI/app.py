import os
import PIL.Image

from flask import Flask, request, render_template, session, redirect, url_for, send_file
from flask_session import Session
from uuid import uuid4
from Project.UI.utils import process_image


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'Project/UI/static'
app.secret_key = 'BAD_SECRET_KEY'
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def check_allowed_file(filename): return True
def secure_filename(filename): return str(uuid4()) + '-' + filename


@app.route("/download/<ind>", methods=["POST", "GET"])
def download_image(ind):
    try:
        ind = int(ind)
        path = f"static/{session["images"][ind]["path"]}"
        return send_file(path,  as_attachment=True)

    except Exception as e:
        print("Failed to download", e)

    return redirect(url_for('index')), 301


@app.route("/magnify/<ind>", methods=["POST", "GET"])
def magnify_image(ind):
    if request.method == "POST":
        return redirect(url_for('index')), 307

    if not session.get("images"):
        print("No images to magnify")
        return redirect(url_for('index')), 301

    try:
        ind = int(ind)
        processed_image = session["images"][ind]["path"]
        raw_image = "raw" + session["images"][ind]["path"].strip("processed")
        masked_image = "masked" + session["images"][ind]["path"].strip("processed")
        return render_template(
            "magnify.html",
            raw_image = raw_image,
            processed_image=processed_image,
            masked_image=masked_image,
            magnified_ind=ind
        ), 200
    except ValueError as e:
        print(f"Error deleting {ind}, {e}")
        return redirect(url_for('index')), 301



@app.route("/delete/<ind>", methods=["POST", "GET"])
def delete_image(ind):
    if not session.get("images"):
        print("No images to delete")
        return redirect(url_for('index')), 301

    if len(session["images"]) == 1:
        session.pop("images", default=None)
        return redirect(url_for('index')), 301

    try:
        ind = int(ind)
        session["images"].pop(ind)
    except ValueError as e:
        print(f"Error deleting {ind}, {e}")

    return redirect(url_for('index')), 301


@app.route("/",methods=['POST', 'GET'])
def index():
    if not session.get("images"): session["images"] = []

    if request.method == 'GET':
        return render_template('display.html', context=session, enumerate=enumerate), 200

    print('post', request.content_type, request.files)


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
    try:
        img = PIL.Image.open(file.stream)
    except IOError:
        return redirect(request.url)

    os.makedirs(f"{app.config['UPLOAD_FOLDER']}/raw", exist_ok=True)
    os.makedirs(f"{app.config['UPLOAD_FOLDER']}/processed", exist_ok=True)
    os.makedirs(f"{app.config['UPLOAD_FOLDER']}/masked", exist_ok=True)

    img.save(f"{app.config['UPLOAD_FOLDER']}/raw/{filename}")
    process_image(
        f"{app.config['UPLOAD_FOLDER']}/raw/{filename}",
        f"{app.config['UPLOAD_FOLDER']}/processed/{filename}",
        f"{app.config['UPLOAD_FOLDER']}/masked/{filename}"
    )

    session["images"].append({"path" : "processed/" + filename})
    return render_template('display.html', context=session, enumerate=enumerate), 200


if __name__ == '__main__':
    app.run(debug=True)
