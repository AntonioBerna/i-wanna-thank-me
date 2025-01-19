import qrcode
from qrcode.constants import ERROR_CORRECT_L
from PIL import Image

if __name__ == "__main__":
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=20,
        border=3,
    )
    qr.add_data("https://antonioberna.github.io/i-wanna-thank-me")
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="#00833f", back_color="white")

    qr_image = qr_image.convert("RGBA")

    cap_image = Image.open("imgs/cap.png")
    cap_size = (100, 100)
    cap_image = cap_image.resize(cap_size, Image.LANCZOS)

    qr_width, qr_height = qr_image.size
    cap_width, cap_height = cap_image.size
    position = (
        (qr_width - cap_width) // 2,
        (qr_height - cap_height) // 2
    )
    qr_image.paste(cap_image, position, cap_image)
    qr_image.save("imgs/i-wanna-thank-me-with-cap.png")
