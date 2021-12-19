from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
import os
from PIL import Image
import numpy as np

UPLOAD_FOLDER = 'static/images'
DEFAULT_IMG = f"{UPLOAD_FOLDER}/upload.png"
DELTA = 23

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

hexadecimal = list(map(str, range(10))) + ['A', 'B', 'C', 'D', 'E', 'F']
decimal_to_hex = {
    i: hexadecimal[i] for i in range(16)
}


def rgb2hex(rgb):
    hex_code = ""
    for num in rgb:
        code = hex(num * DELTA).split('x')[-1]
        hex_code += "0" + code if len(code) == 1 else code
    return hex_code.upper()


def extract_colors(img_path):
    img = Image.open(img_path)
    img_array = np.array(img)

    rgb_colors = {}
    n_pixels = 0
    for rgb_group in img_array:
        for pixels in rgb_group:
            n_pixels += 1
            pixel_tuple = tuple([p // DELTA for p in pixels[:3]])
            if pixel_tuple not in rgb_colors:
                rgb_colors[pixel_tuple] = 1
            else:
                rgb_colors[pixel_tuple] += 1
    top_10_rgb = sorted(rgb_colors.items(), key=lambda pair: pair[1], reverse=True)[:10]
    return [(rgb2hex(rgb), round(n / n_pixels * 100, 2)) for rgb, n in top_10_rgb]


@app.route("/")
def home():
    return render_template("index.html", image=DEFAULT_IMG, colors=extract_colors(DEFAULT_IMG))


@app.route('/extracted-image', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']

        if f.filename == '':
            return redirect(url_for('home'))

        file_name = secure_filename(f.filename)
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        f.save(img_path)

        return render_template("index.html", image=img_path, colors=extract_colors(img_path))


if __name__ == '__main__':
    app.run(debug=True)
