# xwb-audio-extractor
Python script that extracts .wav files (and names them) from .xwb/.xsb files using vgmstream
- **Requires [vgmstream-cli.exe](https://github.com/vgmstream/vgmstream)**
- **Place your .xwb and .xsb files in the same directory as this script and vgmstream-cli.exe**
- **Make sure .xwb and .xsb files have the same name.** If you do not have a .xsb file, or if it is not the same name, you will end up with generic file names (ex. track_#)
- This script will automatically find the number of .wav files inside a wave bank and name them using a provided .xsb file based on their sound cues, then extract them into the same directory as the script
- Made for Windows
