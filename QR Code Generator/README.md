# QR Code Generator

A simple Python script to generate QR codes from text or URLs and save them as image files.

## Description

The QR Code Generator script allows you to generate a QR code from any text or URL. The generated QR code is saved as an image file in the specified format (e.g., PNG).

## Requirements

Python 3.x
qrcode (Python library)

## How to Install
1. Clone the Repository:
```bash
               git clone https://github.com/yourusername/qr-code-generator.git
              cd qr-code-generator
```             
2. Install Required Modules:
```bash
               pip install qrcode[pil]
```
## How to Run the Script
1. Navigate to the Directory:
```bash
          cd path/to/qr-code-generator
```
2. Run the Script:
```bash
           python qr_code_generator.py
```        
3. Follow the Prompts:

Enter the text or URL to generate the QR code, and specify the file name to save the QR code image.

## Example Output
When you run the script, you will be prompted to enter the text or URL and the file name for the QR code image:
```bash
              Enter text or URL to generate QR code: https://example.com
              Enter the file name to save the QR code (e.g., qr_code.png): example_qr.png
              QR code saved as example_qr.png
```