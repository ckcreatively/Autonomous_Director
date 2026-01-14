"""
Cinematic Framing Utilities
Defines framing zones and visualizes camera intent.
"""

import cv2

def draw_rule_of_thirds(frame):
    h, w, _ = frame.shape

    # Vertical lines
    v1 = w // 3
    v2 = 2 * w // 3

    # Horizontal lines
    h1 = h // 3
    h2 = 2 * h // 3

    color = (255, 255, 255)
    thickness = 1

    cv2.line(frame, (v1, 0), (v1, h), color, thickness)
    cv2.line(frame, (v2, 0), (v2, h), color, thickness)
    cv2.line(frame, (0, h1), (w, h1), color, thickness)
    cv2.line(frame, (0, h2), (w, h2), color, thickness)

    return frame


def framing_error(subject_center, target_point):
    sx, sy = subject_center
    tx, ty = target_point
    return tx - sx, ty - sy
