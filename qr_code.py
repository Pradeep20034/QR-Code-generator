import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15 meansthe version of the qr code high the numberbigger the code image and complicated image
    box_size = 10, #size of the box where qrcode will be displayed
    border = 5 #it is the white part of the image -- border in all the 4 sides
)

data = "https://www.linkedin.com/in/pradeep-yadav-19088b287?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
# as i have given the path of my linkedin handle same way you can give anything

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("test.png")
