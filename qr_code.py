import pyqrcode

def qrcode():
	qr = pyqrcode.create(input("Enter website etc..."))
	qr.png('qrcode.png',scale = 10)
	print("Fin")

qrcode()
