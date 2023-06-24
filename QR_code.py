import qrcode
from PIL import Image

#instance of qrcode class
qr=qrcode.QRCode()

# set the data to encode
data="https://github.com/yogesh0535/QR_code_generator/new/main"

#add data to qr code class
qr.add_data(data)

#generates the QR code
qr.make()

# creates image of QR code
img=qr.make_image()

#save image to file
img.save("github.png")

#open image
qr_image=Image.open("github.png")

#show image
qr_image.show()
                    
