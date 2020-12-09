"""
For IGCSE Computer Science course
"""

import pyotp
import qrcode

def register_user(key):
    auth = pyotp.TOTP(key)
    # Generate QR code data
    qr_data = auth.provisioning_uri(issuer_name="Sooraj's Secure Application")
    print("QR Data: ",qr_data)
    # Render a QR code image
    img = qrcode.make(qr_data)
    img.save("qrcode.png") # Save to PNG image file
    img.show() # Display image in a preview window
    return qr_data

def verify(key, code):
    auth = pyotp.TOTP(key)
    return auth.verify(code)
    # Cheat mode: Get the current valid code

def cheat(key):
    auth = pyotp.TOTP(key)
    print( "The phone code would be ", auth.now() )

#### MAIN
# Warning - Anyone who knows the key can generate codes for your "secure app"
# Typically this key should be customised per-user
encryption_key = 'superdupersecretpasswordthatyoucannotguess'
while True:
    choice = input("(r)egister, (v)alidate, or (q)uit? ")
    # Register a new user
    if choice == "r":
        data = register_user(encryption_key)
        print(data)
    # Verify an existing user
    elif choice == "v":
        print("Open Authy on your phone and get the validation code...")
        confirm = input("Code shown on app: ")
        if verify(encryption_key, confirm):
            print("Your code is correct")
        else:
            print("Access denied!!! You will be shot dead...")
        # Quit
    elif choice == "q":
        break