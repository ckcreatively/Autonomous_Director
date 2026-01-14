from framing import draw_rule_of_thirds, framing_error
"""
Person Tracker Prototype
Autonomous Director - Phase 1

Detects and tracks a person in a video stream and visualizes
basic cinematic framing intent.
"""

import cv2

# --- Configuration ---
VIDEO_PATH = "sample_video.mp4"  # placeholder
CONFIDENCE_THRESHOLD = 0.5

# --- Load pre-trained HOG person detector ---
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

frame = draw_rule_of_thirds(frame)

def main():
    cap = cv2.VideoCapture(VIDEO_PATH)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize for speed
        frame = cv2.resize(frame, (960, 540))

        # Detect people
        boxes, weights = hog.detectMultiScale(
            frame,
            winStride=(8, 8),
            padding=(16, 16),
            scale=1.05
        )

        # Draw detections
        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Subject center
            cx = x + w // 2
            cy = y + h // 2
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

        # Draw frame center (cinematic reference)
        h, w, _ = frame.shape
        cv2.circle(frame, (w // 2, h // 2), 5, (255, 0, 0), -1)

        cv2.imshow("Autonomous Director - Perception", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        # Desired framing point (right rule-of-thirds)
        target_x = int(w * 2 / 3)
        target_y = int(h / 2)

        # Draw target framing point
        cv2.circle(frame, (target_x, target_y), 6, (255, 255, 0), -1)

        # Draw correction vector
        error_x, error_y = framing_error((cx, cy), (target_x, target_y))
        cv2.arrowedLine(
        frame,
        (cx, cy),
        (cx + error_x, cy + error_y),
        (0, 255, 255),
        2
    )
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
