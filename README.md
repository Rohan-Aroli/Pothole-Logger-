# 🛣️ AI Pothole Detection & Logging System

An AI-powered pothole detection system built using:

- YOLOv8
- OpenCV
- Python
- PostgreSQL
- SQLAlchemy

The system detects potholes from road videos, estimates severity, simulates GPS coordinates, and stores pothole records inside a PostgreSQL database.

---

# 🚀 Features

✅ Real-time pothole detection using YOLOv8  
✅ Severity classification (Low / Medium / High)  
✅ GPS coordinate simulation  
✅ PostgreSQL database logging  
✅ Duplicate pothole prevention  
✅ OpenCV live visualization  
✅ Modular project structure  

---

# 🧠 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| YOLOv8 | Object detection |
| OpenCV | Video processing |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Ultralytics | YOLO framework |

---

# 📂 Project Structure

```bash
AI-Pothole-Detection/
│
├── main.py
├── detector.py
├── db.py
├── config.py
├── models.py
├── .env
├── yolov8m.pt
├── test.py
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Pothole-Detection.git
cd AI-Pothole-Detection
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install ultralytics opencv-python sqlalchemy psycopg2-binary python-dotenv torch torchvision
```

---

# 🗄️ PostgreSQL Setup

## Install PostgreSQL

Download from:

https://www.postgresql.org/download/

---

## Create Database

Open PostgreSQL shell:

```sql
CREATE DATABASE pothole_db;
```

---

## Configure `.env`

Create a `.env` file:

```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=pothole_db
```

---

# ▶️ Run the Project

```bash
python main.py
```

Press `ESC` to stop detection.

---

# 🧪 How It Works

1. Video frames are read using OpenCV
2. YOLOv8 detects potholes
3. Severity is calculated:
   - 1 pothole → Low
   - 2-3 potholes → Medium
   - 4+ potholes → High
4. GPS coordinates are simulated
5. Data is stored in PostgreSQL
6. Duplicate nearby potholes are skipped

---

# 📸 Output

The system displays:

- Bounding boxes
- Severity level
- Live video feed

And logs potholes into PostgreSQL.

---

# 🧱 Database Table

| Column | Type |
|---|---|
| id | Integer |
| latitude | Float |
| longitude | Float |
| severity | String |
| timestamp | DateTime |

---

# 🔮 Future Improvements

- Real GPS integration
- CARLA simulator integration
- Web dashboard
- Heatmap visualization
- Cloud deployment
- Mobile app integration
- Stereo vision depth estimation

---

# 👨‍💻 Author

Built as an ML + Computer Vision mini project for smart road infrastructure research.
