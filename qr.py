# coding=utf-8

import qrcode

img = qrcode.make('Hello World')
img.save('hello.png')
