import math

def angle_degrees(a, b):
    return math.degrees(math.atan2(b[1]-a[1], b[0]-a[0]))

def body_aspect_ratio(bbox):
    x1, y1, x2, y2 = bbox
    return max(1, x2-x1) / max(1, y2-y1)

def torso_angle(shoulder_mid, hip_mid):
    return abs(angle_degrees(shoulder_mid, hip_mid))
