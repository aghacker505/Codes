import qrcode as qr

img = qr.make("https://youtu.be/TT5OlqNSbK4")
img.save("youtube.jpg")

# #for displaying the image
# from PIL import Image

# image = Image.open('gitprofile.jpg')
# image.show()