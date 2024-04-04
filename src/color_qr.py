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

img = qr.make_image(fill_color="red", back_color="white")
# type(img)  # qrcode.image.pil.PilImage
img = qr.make_image(
    fill_color="red",
    back_color="white",
    module_color="blue",
    background="yellow",
    quiet_zone=10,
)
img.save(f"{file_name}.png")
print("QR code saved successfully!")
