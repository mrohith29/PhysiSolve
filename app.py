from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    text_input = request.form.get('text_input')
    image_file = request.files.get('image_file')

    extracted_text = ""
    if image_file:
        filename = secure_filename(image_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image_file.save(filepath)

        # Extract text from image
        extracted_text = pytesseract.image_to_string(Image.open(filepath))
        os.remove(filepath)  # Clean up uploaded file

    final_input = text_input if text_input else extracted_text

    return render_template('index.html', result=final_input)

if __name__ == '__main__':
    app.run(debug=True)
