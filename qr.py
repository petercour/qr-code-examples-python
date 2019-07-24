#!/usr/bin/python3
import qrcode
img = qrcode.make('hello world')
img.save('test.png')
