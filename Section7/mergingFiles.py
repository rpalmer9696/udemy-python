from datetime import datetime
from glob import iglob

files = []
mergeFileName = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f') + ".txt"

[files.append(i) for i in iglob('*.txt') if 'file' in i]

with open(mergeFileName, 'w') as file:
    for i in files:
        with open(i, "r") as contentFile:
            file.write(contentFile.read() + "\n")
