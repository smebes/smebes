from pytube import YouTube
import os

def yt_download(videoUrl):
    try:
        yt = YouTube(videoUrl)
        only_audio = yt.streams.filter(only_audio=True).first()
        dest = "C:/Users/GUNEY/Desktop/programming/PYTHON/flet/deneme/music" 
        out_file = only_audio.download(output_path = dest)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        return True
    except:
        return False
