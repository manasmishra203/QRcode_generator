import qrcode
import tkinter as tk #for making gui

def generate_qr():
    website_link = entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=5
    )

    qr.add_data(website_link)
    qr.make()

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    img.save(entry.get())

    print("QR code generated successfully!")

window =tk.Tk()  #main app window
window.title("QR Code Generator") #object.method() window->object title->method
window.geometry("500x400")

label = tk.Label(window, text="Enter URL: ")
label.pack() #it put the widget into the window

entry = tk.Entry(window)
entry.pack()

#command=generate_qr()-> run the dunction immediately
#command=generate_qr-> tkinter run it laterwhen button is clicked
button = tk.Button(window, text="Generate QR",command=generate_qr)
button.pack()

window.mainloop() #it creates window running