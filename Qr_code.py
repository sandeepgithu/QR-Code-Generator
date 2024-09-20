import qrcode as qr
from PIL import Image

qr_code = qr.QRCode(version=1,
                    error_correction=qr.constants.ERROR_CORRECT_H,
                    box_size=10, border=4)

qr_code.add_data("https://www.instagram.com/singsandeep971/")

qr_code.make(fit=True)

img = qr_code.make_image(fill_color='red', back_color='white')

img.save("Singsandeep971.png")
