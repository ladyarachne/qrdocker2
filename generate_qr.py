# generate_qr.py
import os
from datetime import datetime
from pathlib import Path
import qrcode

# Get environment variables (with defaults if not provided)
data_url = os.getenv("QR_DATA_URL", "https://github.com/ladyarachne")
output_dir = os.getenv("QR_CODE_DIR", "qr_codes")
filename = os.getenv('QR_CODE_FILENAME', f"QRCode_{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
fill_color = os.getenv("FILL_COLOR", "black")
back_color = os.getenv("BACK_COLOR", "white")

# Make sure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data_url)
qr.make(fit=True)

# Customize colors
img = qr.make_image(fill_color=fill_color, back_color=back_color)

# Save QR code image
file_path = os.path.join(output_dir, filename)
img.save(file_path)

print(f"QR Code generated for: {data_url}")
print(f"Saved to: {file_path}")

