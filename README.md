# QR Code Generator

A Python-based QR Code Generator that creates QR codes from URLs or text. The project has been extended with multiple QR-code generation, custom colors, styled QR codes, and a Tkinter graphical user interface.

## Features

- Generate QR codes from URLs or text
- Generate multiple QR codes in one run
- Customize QR and background colors
- Generate square, rounded, and circular QR styles
- Configure QR version, error correction, box size, and border
- Save generated QR codes as image files
- Tkinter GUI for generating QR codes
- Pillow support for image handling and styled QR codes

## Technologies Used

- **Python**
- **qrcode** — QR code generation
- **Pillow (PIL)** — image handling and styled QR colors
- **Tkinter** — graphical user interface

## Installation

Clone the repository:

```bash
git clone https://github.com/manasmishra203/QRcode_generator.git
cd QRcode_generator
```

Install the required packages:

```bash
pip install "qrcode[pil]"
```

Pillow can also be installed directly if needed:

```bash
pip install Pillow
```

## Project Structure

```text
QRcode_generator/
│
├── qr.py
├── styled_qr.py
├── EnhancedGUI.py
├── output/
├── codedex.png
└── README.md
```

## Command-Line QR Generator

The basic QR generator uses the `qrcode` library:

```python
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=5
)

qr.add_data("https://example.com")
qr.make()

img = qr.make_image(
    fill_color="black",
    back_color="white"
)

img.save("qrcode.png")
```

## Multiple QR Codes

The project can generate multiple QR codes in a single execution.

The user enters the number of QR codes and then provides the URL or text for each one.

```text
Enter the number of QR codes you want to generate: 3
Enter the URL: https://google.com
Enter the URL: https://youtube.com
Enter the URL: https://github.com
```

## QR Code Styling

Styled QR codes use `StyledPilImage` and module drawers from the `qrcode` library.

### Square

The standard QR-code appearance.

### Rounded

Uses:

```python
RoundedModuleDrawer()
```

to create rounded modules.

### Circle

Uses:

```python
CircleModuleDrawer()
```

to create circular modules.

Example:

```python
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=CircleModuleDrawer(),
    color_mask=SolidFillColorMask(
        front_color=qr_color,
        back_color=bg_color
    )
)
```

## Custom Colors

QR and background colors can be customized.

Examples:

```text
red
blue
purple
green
black
white
```

The project can also use hexadecimal color values through Pillow's color handling.

## Tkinter GUI

The project includes a Tkinter-based graphical interface so the user can generate QR codes without entering commands in the terminal.

Basic workflow:

```text
Enter URL/Text
       ↓
Click Generate QR
       ↓
QR Code is generated
       ↓
QR Code is saved
```

The GUI is being developed to support options such as:

- QR color
- Background color
- QR style
- File name
- QR preview

## QR Code Settings

| Parameter | Purpose |
|---|---|
| `version` | Controls the QR code size |
| `error_correction` | Controls error recovery capability |
| `box_size` | Controls the size of each QR module |
| `border` | Controls the border width |

Example:

```python
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=5
)
```

## Future Improvements

- [ ] Complete Tkinter GUI
- [ ] Add GUI color selection
- [ ] Add GUI style selection
- [ ] Add QR-code preview
- [ ] Add user-selected save location
- [ ] Batch generation from CSV/text files
- [ ] Add logos/images to QR codes
- [ ] Experiment with PyQRCode and other QR libraries

## Learning Goals

This project is also used to practice:

- Python loops
- Functions
- Lists and dictionaries
- File handling
- External Python libraries
- Pillow
- Object-oriented programming concepts through the `qrcode` library
- Tkinter GUI development

## Author

**Manas Mishra**

GitHub: https://github.com/manasmishra203
