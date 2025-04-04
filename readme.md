# Docker QR Code Generator

This project creates a QR code PNG file using a Python script running inside a Docker container. The QR code links directly to my GitHub homepage.

## QR Code Output

Scan this QR code to visit: [https://github.com/ladyarachne](https://github.com/ladyarachne)

![QR Code](qr_codes/my_github_qr.png)

## Docker Log

Below is a screenshot of the terminal showing successful QR code generation:

![Docker Log](images/docker_log_screenshot.png)

## How to Run (Optional for Reviewers)

```bash
docker run --rm --name qr-generator \
-e QR_DATA_URL='https://github.com/ladyarachne' \
-e QR_CODE_DIR='qr_codes' \
-e QR_CODE_FILENAME='my_github_qr.png' \
-e FILL_COLOR='black' \
-e BACK_COLOR='pink' \
-v "$(pwd)/qr_codes:/app/qr_codes" \
my-qr-app