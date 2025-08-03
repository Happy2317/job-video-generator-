import os
from utils import generate_qr, select_music, extract_offer_info, qr_clip
from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip, concatenate_videoclips

input_dir = "input_texts"
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(input_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        title, url = extract_offer_info(content)
        base_name = filename.replace(".txt", "")

        # Générer QR code
        if url:
            generate_qr(url, base_name)

        # Créer clip texte
        clip = TextClip(title, fontsize=40, color='white', size=(1080, 1920), method='caption')
        clip = clip.set_duration(7).set_position('center')

        # Ajouter musique
        music_path = select_music()
        if music_path:
            audio = AudioFileClip(music_path).subclip(0, 7)
            clip = clip.set_audio(audio)

        # Ajouter QR code
        qr = qr_clip(base_name)
        final = concatenate_videoclips([clip, qr]) if qr else clip

        # Export vidéo
        final.write_videofile(f"output/{base_name}.mp4", fps=24)

        # Métadonnées
        with open(f"output/{base_name}_metadata.txt", "w", encoding="utf-8") as out:
            out.write(f"Titre : {title}\n")
            out.write(f"Lien : {url}\n")
            out.write(f"QR code : assets/qrcodes/{base_name}.png\n")
