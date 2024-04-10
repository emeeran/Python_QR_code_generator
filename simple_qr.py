import qrcode  # https://pypi.org/project/qrcode/

source = input("Enter text you want to encode: ")
file_name = input("Enter a name output file: ")

img = qrcode.make(f"{source}")
type(img)  # qrcode.image.pil.PilImage
img.save(f"{file_name}.png")
