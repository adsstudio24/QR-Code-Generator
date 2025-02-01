import qrcode

def generate_qr(data, filename="qr_code.png", fill_color="black", back_color="white"):
    """
    Генерує QR-код на основі вхідних даних.
    
    :param data: Текст або посилання для кодування
    :param filename: Ім'я файлу для збереження
    :param fill_color: Колір QR-коду
    :param back_color: Колір фону
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill=fill_color, back_color=back_color)
    img.save(filename)
    print(f"QR-код збережено як {filename}")

if __name__ == "__main__":
    text = input("Введіть текст або посилання для генерації QR-коду: ").strip()
    if text:
        generate_qr(text)
    else:
        print("Помилка: Введено порожній рядок.")
