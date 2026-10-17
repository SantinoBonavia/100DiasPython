import qrcode
data=input("Entre el texto o el link:")
img=qrcode.make(data)
img.save("img.png")
img.show()

print("QR generado!")