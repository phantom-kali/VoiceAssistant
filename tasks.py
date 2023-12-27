import subprocess
from pytube import YouTube
from pathlib import Path


def download_youtube_video(url) -> list[str]:
    downloads_path = str(Path.home() / 'Videos/YouTube')
    video = YouTube(url)
    name = video.title
    # / and \ need to be removed from the name. otherwise tkinter calls OSError as it's taking it as part of path
    name = name.replace('\\', '').replace('/', '')

    new_name = f'{name}.mp4'
    print(video.streams.get_highest_resolution())
    video.streams.get_highest_resolution().download(filename=new_name, output_path=downloads_path)

    return [new_name, downloads_path]

def download_youtube_audio(url):
    downloads_path = str(Path.home() / 'Music/YouTube')
    video = YouTube(url)
    name = video.title
    name = name.replace('\\', '').replace('/', '')
    
    new_name = f'{name}.mp3'
    print(video.streams.get_audio_only())
    video.streams.get_audio_only().download(filename=new_name, output_path=downloads_path)    
    
    return [new_name, downloads_path]


download_youtube_video("https://www.youtube.com/watch?v=KCVN-SuBBWM")
