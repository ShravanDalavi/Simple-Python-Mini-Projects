import qrcode

def generate_qr_code(data, file_name):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the QR code image
    img.save(file_name)

    print(f"QR code saved as {file_name}")

if __name__ == "__main__":
    data = input("Enter text or URL to generate QR code: ")
    file_name = input("Enter the file name to save the QR code (e.g., qr_code.png): ")

    generate_qr_code(data, file_name)
