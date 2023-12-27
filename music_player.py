import os
from pathlib import Path
import re

music_path = str(Path.home() / 'Music')

os.chdir(music_path)
files = os.listdir()

def play(music):
    for file in files:
        if "." in file:
            # Split the file name and extension
            base_name, extension = os.path.splitext(file)
            
            # Check if the music term is in the base name
            if re.search(music, base_name, re.IGNORECASE):
                os.system(f"mplayer '{file}'")

# Call the play function with the search term "with"
# play("count")


