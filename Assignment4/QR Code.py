
import qrcode

name = input("please enter your name: ")
phone_number = input("please enter your phone_number: ")

a = name + phone_number

img = qrcode.make(a)
img.save("phone_number.png")
