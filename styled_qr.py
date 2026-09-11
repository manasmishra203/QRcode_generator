import qrcode
from PIL import ImageColor

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import (
    RoundedModuleDrawer,
    CircleModuleDrawer
)
from qrcode.image.styles.colormasks import SolidFillColorMask


number = int(input("Enter the number of QR codes you want to generate: "))

qr_color = input("Enter color of QR: ")
bg_color = input("Enter color of background: ")

# Convert color names into RGB values
qr_color = ImageColor.getrgb(qr_color)
bg_color = ImageColor.getrgb(bg_color)


for i in range(number):

    website_link = input("Enter the URL: ")

    qr = qrcode.QRCode(
        version=1,  # defines the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # defines how many pixels each box of the QR code is
        border=5,  # defines how many boxes thick the border should be
    )

    qr.add_data(website_link)
    qr.make(fit=True)

    style = input("Enter QR style (square/rounded/circle): ")

    if style == "rounded":
        drawer = RoundedModuleDrawer()

    elif style == "circle":
        drawer = CircleModuleDrawer()

    else:
        drawer = None

    if drawer:

        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=drawer,
            color_mask=SolidFillColorMask(
                front_color=qr_color,
                back_color=bg_color
            )
        )

    else:

        img = qr.make_image(
            fill_color=qr_color,
            back_color=bg_color
        )

    # Save QR code
    filename = input(
        "Enter the name of the file to save QR code with extension: "
    )

    img.save(filename)


print("All QR codes generated successfully!")