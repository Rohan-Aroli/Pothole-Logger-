from db import engine
from models import Base
from detector import process_video

# create tables
Base.metadata.create_all(bind=engine)

process_video(r"C:\Users\aroli\Downloads\Watch Video Terrible potholes in Rangoon Road - Northern Natal News (360p, h264, youtube).mp4")