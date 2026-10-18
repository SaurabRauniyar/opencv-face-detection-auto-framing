
import cv2

# Step 1: Load the face detector
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Step 2: Open webcam
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Camera could not be opened")
    exit()

# Step 3: Read video continuously
while True:
    ret, frame = video.read()

    if not ret:
        break

    # Step 4: Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Step 5: Detect faces
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Step 6: Draw a box around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    # Step 7: Display camera
    cv2.imshow("Real-Time Face Detection", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 8: Close camera
video.release()
cv2.destroyAllWindows()
