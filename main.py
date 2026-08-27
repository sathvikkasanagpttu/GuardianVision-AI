import os, base64, asyncio
import cv2
from datetime import datetime
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from config import FALL_THRESHOLD
from fall_detection.risk_engine import FallRiskEngine
from database.database import load_incidents

app = FastAPI(title="GuardianVision AI")
engine = FallRiskEngine(FALL_THRESHOLD)

@app.get("/api/status")
def status():
    return {"system": "active", "threshold": FALL_THRESHOLD}

@app.get("/api/incidents")
def incidents():
    return load_incidents()

@app.get("/", response_class=HTMLResponse)
def dashboard():
    path = os.path.join(os.path.dirname(__file__), "../frontend/index.html")
    with open(path, encoding="utf-8") as f: return HTMLResponse(f.read())

@app.websocket("/ws")
async def stream(ws: WebSocket):
    await ws.accept()
    camera = cv2.VideoCapture(0)
    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                await ws.send_json({"error": "camera unavailable"})
                break
            # Live demo state. Connect the detector/pose pipeline here for real inference.
            result = engine.score()
            ok, buf = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
            await ws.send_json({
                "frame": base64.b64encode(buf).decode() if ok else "",
                "state": result.state,
                "score": result.score,
                "reasons": result.reasons,
                "timestamp": datetime.now().isoformat(timespec="seconds")
            })
            await asyncio.sleep(0.03)
    finally:
        camera.release()
