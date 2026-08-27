import os
CAMERA_INDEX = int(os.getenv("CAMERA_INDEX", "0"))
FALL_THRESHOLD = float(os.getenv("FALL_THRESHOLD", "0.80"))
CONFIRMATION_FRAMES = int(os.getenv("CONFIRMATION_FRAMES", "8"))
INCIDENT_DIR = os.getenv("INCIDENT_DIR", "../incidents")
PRIVACY_MODE = os.getenv("PRIVACY_MODE", "true").lower() == "true"
