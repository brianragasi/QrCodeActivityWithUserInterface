import qrcode
import cv2

def generate_qr_code(data, filename="github.jpg"):
    """Generates a QR code and saves it as an image."""
    img = qrcode.make(data)
    img.save("static/uploads/" + filename)  # Save to uploads folder
    return filename

def decode_qr_code(image_path):
    """Decodes a QR code from an image."""
    d = cv2.QRCodeDetector()
    val, _, _ = d.detectAndDecode(cv2.imread(image_path))
    return val