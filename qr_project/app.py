from flask import Flask, render_template, request, send_from_directory
import os
from qRCode import generate_qr_code, decode_qr_code

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Configure upload folder

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form['data']
    filename = generate_qr_code(data)
    return render_template('index.html', qr_image=filename)

@app.route('/decode', methods=['POST'])
def decode():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        decoded_data = decode_qr_code(filepath)
        return render_template('index.html', decoded_data=decoded_data)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)