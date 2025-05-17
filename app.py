import os
import PIL.Image
from flask import Flask, request, redirect
from flask import render_template

from utils import process_image


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

def check_allowed_file(filename): return True
def secure_filename(filename): return filename


@app.route("/",methods=['GET', 'POST'])
def index():
    context = {}
    context["images"] = []

    if request.method == 'POST':
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

        context["images"].append({"path" : f"temp/{filename}"})
        return render_template('index.html', context=context), 200

    else:
        context["images"].append({"path" : "image1.jpg"})
        return render_template("index.html", context=context), 200


if __name__ == '__main__':
    app.run()
