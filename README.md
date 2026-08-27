# GuardianVision AI 🚨🤖
Real-time computer-vision fall detection and emergency response prototype.

Features:
- Pose/keypoint analysis
- Body geometry and torso-angle risk scoring
- Temporal confirmation to reduce false positives
- Incident recording hooks
- Email alert integration hooks
- FastAPI + WebSocket live dashboard
- Incident history API
- Privacy-mode configuration
- Docker setup

## Run
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r ../requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000

Open http://localhost:8000

Important: this is a prototype, not a certified medical/safety device. Validate it on representative labeled footage before real-world deployment.
