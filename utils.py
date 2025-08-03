import qrcode
import os
import random
from moviepy.editor import ImageClip

def generate_qr(url, filename):
    os.makedirs("assets/qrcodes", exist_ok=True)
    qr = qrcode.make(url)
    qr.save(f"assets/qrcodes/{filename}.png")

def select_music():
    music_dir = "assets/music"
    tracks = [os.path.join(music_dir, f) for f in os.listdir(music_dir) if f.endswith(".mp3")]
    return random.choice(tracks) if tracks else None

def extract_offer_info(text):
    lines = text.splitlines()
    title = lines[0] if lines else "Offre"
    url = next((line for line in lines if line.startswith("https://")), "")
    return title, url

def qr_clip(filename, duration=3):
    qr_path = f"assets/qrcodes/{filename}.png"
    if os.path.exists(qr_path):
        qr = ImageClip(qr_path).resize(height=200)
        return qr.set_position(("right", "bottom")).set_duration(duration)
    return None
