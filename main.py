import os
import json
import sys
from datetime import datetime
from config import JOB_DATA_PATH, OUTPUT_DIR
from text_utils import prepare_text
from video_generator import generate_video

def get_video_limit_by_hour():
    current_hour = datetime.utcnow().hour
    if current_hour == 5:
        return 3
    elif current_hour == 12:
        return 3
    elif current_hour == 19:
        return 4
    else:
        return 0

MAX_VIDEOS = get_video_limit_by_hour()

print(f"[INFO] Heure actuelle (UTC) : {datetime.utcnow().hour}h")
print(f"[INFO] Nombre de vidéos à générer : {MAX_VIDEOS}")

if MAX_VIDEOS == 0:
    print("[WARNING] Script lancé à une heure non prévue. Aucune vidéo ne sera générée.")
    sys.exit()

# Charger les offres
with open(JOB_DATA_PATH, 'r', encoding='utf-8') as f:
    jobs = json.load(f)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Génération des vidéos
for i, job in enumerate(jobs):
    if i >= MAX_VIDEOS:
        break
    print(f"[INFO] Génération de la vidéo {i+1}/{MAX_VIDEOS} pour le job : {job['title']}")
    text = prepare_text(job['description'])
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M")
    filename = f"{job['title'].replace(' ', '_')}_{timestamp}.mp4"
    output_path = os.path.join(OUTPUT_DIR, filename)
    generate_video(text, output_path)

# Résumé final
print("\n[SUMMARY] Exécution terminée")
print(f"[SUMMARY] Heure UTC : {datetime.utcnow().hour}h")
print(f"[SUMMARY] Vidéos générées : {MAX_VIDEOS}")
print("[SUMMARY] Titres des vidéos :")
for i in range(MAX_VIDEOS):
    print(f"  - {jobs[i]['title']}")
    
