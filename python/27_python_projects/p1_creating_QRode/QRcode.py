import qrcode as qr

img = qr.make("https://github.com/aghacker505")
img.save("gitprofile.jpg")

# #for displaying the image
# from PIL import Image

# image = Image.open('gitprofile.jpg')
# image.show()