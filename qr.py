import qrcode
website_link = input("enter the URL: ") #'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
qr=qrcode.QRCode(
    version=1,#defines the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5, #defines how many pixels each “box” of the QR code is
    border=5, #defines how many boxes thick the border should be
)
qr.add_data(website_link)
qr.make()
#this saving image comes under pillow library
img=qr.make_image(fill_color=input("enter color of qr: "),back_color=input("enter color of background: "))
img.save(input("enter the name of the file to save qrcode with extension: ")) #'qrcode.png'
