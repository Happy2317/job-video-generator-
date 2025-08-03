import os
import json
from datetime import datetime
from config import JOB_DATA_PATH, OUTPUT_DIR
from text_utils import prepare_text
from video_generator import generate_video

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(JOB_DATA_PATH, 'r', encoding='utf-8') as f:
    jobs = json.load(f)

for job in jobs:
    text = prepare_text(job['description'])
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = os.path.join(OUTPUT_DIR, f"{job['title'].replace(' ', '_')}_{timestamp}.mp4")
    generate_video(text, output_file)
