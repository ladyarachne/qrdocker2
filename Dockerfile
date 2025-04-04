# Use official Python image
FROM python:3.13-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY generate_qr.py .

# Create default directory inside the container
RUN mkdir -p qr_codes

# Set environment variables (optional defaults)
ENV QR_DATA_URL=https://github.com/kaw393939
ENV QR_CODE_DIR=qr_codes
ENV QR_CODE_FILENAME=my_qr.png
ENV FILL_COLOR=black
ENV BACK_COLOR=white

# Run the script when the container starts
CMD ["python", "generate_qr.py"]