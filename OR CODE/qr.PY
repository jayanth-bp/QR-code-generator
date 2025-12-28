import os
import qrcode

url=input("paste the link: ").strip()
name=input("save as: ").strip()
choice = input("Do you want to change QR color? (yes / no): ").strip().lower()

if choice == "yes":
    fill_color = input("Enter QR color: ").strip()
    back_color = input("Enter background color: ").strip()
else:
    fill_color="black"
    back_color="white"

file_path="C:\\Users\\Jaynth\\OneDrive\\Desktop\\f\\Projects\\OR CODE\\Generated QR's"

file_path = os.path.join(file_path, name + ".png")


qr=qrcode.QRCode(box_size="10" , border="5")
qr.add_data(url)

img=qr.make_image(fill_color=fill_color , back_color=back_color)
img.save(file_path)

print("QR is generated")