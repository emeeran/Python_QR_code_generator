import qrcode  # pip install "qrcode[pil]" to color print

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

data = input("Enter data to encode: ")
file_name = input("Enter a name for file: ")

qr.add_data(f"{data}")
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")
img.save(f"{file_name}.png")
print("QR code saved successfully!")
