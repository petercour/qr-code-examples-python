#!/usr/bin/python3
import qrcode
import glob

files = glob.glob("*.py")
for filename in files:
    data = ""
    with open(filename, 'r') as file:
            data = file.read()
            
    img = qrcode.make(data)
    img.save('qr-' + filename + '.png')
