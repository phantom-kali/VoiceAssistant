import os
from pathlib import Path
import re

video_path = str(Path.home() / 'Videos')

os.chdir(video_path)
files = os.listdir()

def play(video):
    for file in files:
        if "." in file:
            # Split the file name and extension
            base_name, extension = os.path.splitext(file)
            
            # Check if the video term is in the base name
            if re.search(video, base_name, re.IGNORECASE):
                os.system(f"mplayer '{file}'")

# Call the play function with the search term "with"
