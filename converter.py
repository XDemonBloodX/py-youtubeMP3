# Convert webm files to mp3 using FFMPEG
# To use this script you need to install FFMPEG in your system
# For windows users, you need to download & add FFMPEG to the PATH (Windows Environment Variables)

import os
import re
import subprocess
import argparse
import sys

# The arguments
folderConvert= "./convert"
folderSongs="./songs"

if not os.path.isdir(folderConvert):
    print(f'The webm path "{folderConvert}" does not exist.')
    sys.exit()


for file in os.listdir(folderConvert):
    webmFile = os.path.join(folderConvert, file)
    mp3File = os.path.join(folderSongs, file).replace(
        "webm", "mp3")

    command = f"ffmpeg -i \"{webmFile}\" -vn -ab 128k -ar 44100 -y \"{mp3File}\""
    subprocess.call(command, shell=True)

print('conversion finished')

import os

dir_name = "./convert"
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".webm"):
        os.remove(os.path.join(dir_name, item))