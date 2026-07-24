import qrcode

url=input("Enter the url : ").strip()
file_path="C:\\Users\\HP\\Desktop\\qrcode.png"

qr=qrcode.QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(file_path)

print("QR Code is generated!")