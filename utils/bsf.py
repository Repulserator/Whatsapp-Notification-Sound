import base64
import os

INPUT_FOLDER = "sounds"
OUTPUT_FILE = "base64_sounds.js"

lines = []
lines.append("const SOUND_LIST = [")

for file in sorted(os.listdir(INPUT_FOLDER)):
    if file.endswith(".mp3") or file.endswith(".wav"):
        path = os.path.join(INPUT_FOLDER, file)

        filename = str(file[:-4])

        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")

        mime = "audio/mp3" if file.endswith(".mp3") else "audio/wav"

        lines.append(f'  {filename}: "data:{mime};base64,{encoded}",')

lines.append("];")

with open(OUTPUT_FILE, "w") as f:
    f.write("\n".join(lines))

print("Done! Paste SOUND_LIST into your Tampermonkey script.")