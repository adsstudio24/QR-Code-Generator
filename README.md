# QR-Code-Generator

import qrcode

def generate_qr(data, filename="qr_code.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR-код збережено як {filename}")

if __name__ == "__main__":
    text = input("Введіть текст або посилання для генерації QR-коду: ")
    generate_qr(text)
