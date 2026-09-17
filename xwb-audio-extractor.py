import subprocess
import re
import os

print("-- .xwb Audio Extractor; by blazinblaze --")
print("Please make sure to have the .xsb file (with the same name as the .xwb file) in the same directory of the .xwb file, or else you won't get any audio file names.")
print("Additionally, have the vgmstream-cli.exe and .xwb file in the same directory as this file.")
xwb_file = input("Please enter the name (with file extension) of the .xwb file you are using: ")
#is_music = input("Is your file a music .xwb? (Important as music, at least in Minecraft, does not have multiple audio cues - music tracks will be overwitten otherwise - if you only end up with one .wav file, try this) (Y/N) ") == "Y"

numCmd = subprocess.run(["vgmstream-cli.exe", "-m", xwb_file], capture_output=True, text=True)
findNum = re.search(r"stream\s*count:\s*(\d+)", numCmd.stdout)
num = 1
if findNum:
    num = int(findNum.group(1)) + 1

for i in range(1, num):
    #if is_music:
        getCueName = subprocess.run(["vgmstream-cli.exe", "-s", str(i), "-m", xwb_file], capture_output=True, text=True)
        findName = re.search(r"stream\s*name:\s*(.*)", getCueName.stdout)
        name = "track"
        if findName:
            name = findName.group(1).strip()
        counter = 1
        fileName = f"{name}.wav";
        while os.path.exists(fileName):
            fileName = f"{name}_{counter}.wav"
            counter += 1
        cmd = subprocess.run(["vgmstream-cli.exe", "-s", str(i), "-o", fileName, xwb_file], capture_output=True, text=True)
        print(cmd.stdout)
        print(cmd.returncode)
    #else:
        #cmd = subprocess.run(["vgmstream-cli.exe", "-s", str(i), "-o", "?n.wav", xwb_file], capture_output=True, text=True)
        #print(cmd.stdout)
        #print(cmd.returncode)