
import cv2

# Load face detector
detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

video = cv2.VideoCapture(0)

if not video.isOpened():
    raise RuntimeError("Cannot open webcam")

# Settings
zoom = 1.2
box_alpha = 0.15
camera_alpha = 0.08
dead_zone = 0.12

smooth_box = None
camera_center = None

try:
    while True:
        ret, frame = video.read()

        if not ret:
            break

        height, width = frame.shape[:2]

        gray = cv2.cvtColor(
            frame, cv2.COLOR_BGR2GRAY
        )

        faces = detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=6,
            minSize=(60, 60)
        )

        if len(faces) > 0:
            x, y, w, h = max(
                faces,
                key=lambda f: f[2] * f[3]
            )

            detected = [float(x), float(y),
                        float(w), float(h)]

            # Smooth bounding box
            if smooth_box is None:
                smooth_box = detected
            else:
                smooth_box = [
                    box_alpha * new +
                    (1 - box_alpha) * old
                    for new, old in zip(
                        detected, smooth_box
                    )
                ]

            sx, sy, sw, sh = map(int, smooth_box)

            # Draw smoothed bounding box
            cv2.rectangle(
                frame,
                (sx, sy),
                (sx + sw, sy + sh),
                (0, 255, 0),
                2
            )

            face_cx = sx + sw / 2
            face_cy = sy + sh / 2

            if camera_center is None:
                camera_center = [
                    width / 2, height / 2
                ]

            # Only move framing outside dead zone
            if abs(face_cx - camera_center[0]) > (
                width * dead_zone
            ):
                camera_center[0] += camera_alpha * (
                    face_cx - camera_center[0]
                )

            if abs(face_cy - camera_center[1]) > (
                height * dead_zone
            ):
                camera_center[1] += camera_alpha * (
                    face_cy - camera_center[1]
                )

        if camera_center is None:
            camera_center = [
                width / 2, height / 2
            ]

        # Create digital camera crop
        crop_w = int(width / zoom)
        crop_h = int(height / zoom)

        cx, cy = camera_center

        x1 = int(max(0, min(
            cx - crop_w / 2, width - crop_w
        )))

        y1 = int(max(0, min(
            cy - crop_h / 2, height - crop_h
        )))

        cropped = frame[
            y1:y1 + crop_h,
            x1:x1 + crop_w
        ]

        framed = cv2.resize(
            cropped, (width, height)
        )

        cv2.putText(
            framed,
            "Auto Framing",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.imshow("Original Camera", frame)
        cv2.imshow("Auto Framing", framed)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    video.release()
    cv2.destroyAllWindows()
