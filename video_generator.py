from moviepy.editor import TextClip, CompositeVideoClip

def generate_video(text, output_path):
    clip = TextClip(text, fontsize=40, color='white', bg_color='black', size=(1280, 720), method='caption')
    clip = clip.set_duration(30)
    video = CompositeVideoClip([clip])
    video.write_videofile(output_path, fps=24)
