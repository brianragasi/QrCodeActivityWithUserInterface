from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_image = None
    if request.method == 'POST':
        data = request.form['data']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img_buffer = BytesIO()
        img.save(img_buffer, format="PNG")
        img_buffer.seek(0)
        qr_code_image = "image/png;base64," + str(base64.b64encode(img_buffer.read()).decode('utf-8'))
    return render_template('index.html', qr_code_image=qr_code_image)

if __name__ == '__main__':
    app.run(debug=True)
