
import cv2

# 1. Load pretrained face detector
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# 2. Open webcam
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Cannot open camera")
    exit()

# 3. Tracking settings
alpha = 0.25
smooth_box = None

while True:
    ret, frame = video.read()

    if not ret:
        break

    # 4. Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 5. Detect faces
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    if len(faces) > 0:

        # 6. Choose the largest detected face
        x, y, w, h = max(
            faces,
            key=lambda face: face[2] * face[3]
        )

        new_box = [float(x), float(y), float(w), float(h)]

        # 7. Apply exponential smoothing
        if smooth_box is None:
            smooth_box = new_box
        else:
            smooth_box = [
                alpha * new + (1 - alpha) * old
                for new, old in zip(new_box, smooth_box)
            ]

        sx, sy, sw, sh = map(int, smooth_box)

        # 8. Draw smooth bounding box
        cv2.rectangle(
            frame,
            (sx, sy),
            (sx + sw, sy + sh),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Smooth Face Tracking",
            (sx, max(25, sy - 10)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    else:
        smooth_box = None

    # 9. Display video
    cv2.imshow("Face Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 10. Release camera
video.release()
cv2.destroyAllWindows()
