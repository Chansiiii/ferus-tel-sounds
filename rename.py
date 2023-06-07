import os

directory = os.path.dirname(os.path.abspath(__file__))
files = []
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        files.append(filename)
# write files to text file
with open("sounds.txt", "w") as f:
    for file in files:
        f.write(f"{file}\n")
