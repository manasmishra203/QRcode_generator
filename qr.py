import qrcode

number = int(input("Enter the number of QR codes you want to generate: "))

qr_color = input("Enter color of QR: ")
bg_color = input("Enter color of background: ")
for i in range(number):

    website_link = input("Enter the URL: ")

    qr=qrcode.QRCode(
        version=2,#defines the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5, #defines how many pixels each “box” of the QR code is
        border=5, #defines how many boxes thick the border should be
    )
    qr.add_data(website_link)
    qr.make()
    #this saving image comes under pillow library

    img=qr.make_image(fill_color=qr_color,back_color=bg_color)
    img.save(input("enter the name of the file to save qrcode with extension: ")) #'qrcode.png'
print("All QR codes generated successfully!")