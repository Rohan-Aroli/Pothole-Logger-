import cv2
import random
from ultralytics import YOLO
from db import SessionLocal
from models import Pothole

model = YOLO("yolov8m.pt")

def simulate_gps():
    lat = 12.9716 + random.uniform(-0.01, 0.01)
    lon = 77.5946 + random.uniform(-0.01, 0.01)
    return lat, lon

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    db = SessionLocal()

    frame_count = 0

    cv2.namedWindow("Pothole Detection", cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # run detection every 10 frames (performance boost)
        if frame_count % 10 != 0:
            cv2.imshow("Pothole Detection", frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
            continue

        results = model.predict(frame, conf=0.3, device="cpu", verbose=False)

        # draw boxes
        annotated = frame.copy()

        boxes = results[0].boxes

        if boxes is not None and len(boxes) > 0:
            lat, lon = simulate_gps()

            # ---------- SEVERITY ----------
            count = len(boxes)
            if count > 3:
                severity = "High"
            elif count > 1:
                severity = "Medium"
            else:
                severity = "Low"

            # ---------- DEDUP ----------
            last = db.query(Pothole).order_by(Pothole.id.desc()).first()

            if last:
                if abs(last.latitude - lat) < 0.0005 and abs(last.longitude - lon) < 0.0005:
                    print("Skipped duplicate")
                else:
                    pothole = Pothole(
                        latitude=lat,
                        longitude=lon,
                        severity=severity
                    )
                    db.add(pothole)
                    db.commit()

                    print(f"Logged pothole at {lat}, {lon}, {severity}")
            else:
                pothole = Pothole(
                    latitude=lat,
                    longitude=lon,
                    severity=severity
                )
                db.add(pothole)
                db.commit()

                print(f"Logged pothole at {lat}, {lon}, {severity}")

            # ---------- DISPLAY TEXT ----------
            cv2.putText(
                annotated,
                f"Severity: {severity}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

        # ---------- SHOW ----------
        cv2.imshow("Pothole Detection", annotated)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    db.close()
    cv2.destroyAllWindows()