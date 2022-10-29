import qrcode as qr
from PIL import Image

#customizing qrcode
code = qr.QRCode(version=1,
error_correction = qr.constants.ERROR_CORRECT_H,
box_size= 10,
border = 10)

#adding data to qrcode and 
code.add_data("https://github.com/aghacker505")
#generating qrcoding
code.make(fit = True)

#making image
img = code.make_image(fil_color = "black", back_color= "blue")
#saving image
img.save("gitprofile2.jpg")