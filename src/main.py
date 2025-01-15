import qrcode
from qrcode.constants import ERROR_CORRECT_L

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
    qr_image.save("imgs/i-wanna-thank-me.png")
