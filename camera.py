
import cv2

# Step 1: Open the built-in webcam
video = cv2.VideoCapture(0)

# Check whether camera opened successfully
if not video.isOpened():
    print("Error: Cannot open webcam")
    exit()

print("Webcam opened successfully!")

# Step 2: Continuously capture video
while True:
    ret, frame = video.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Step 3: Display webcam video
    cv2.imshow("Basic Webcam", frame)

    # Step 4: Press Q to close
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 5: Release camera resources
video.release()
cv2.destroyAllWindows()
