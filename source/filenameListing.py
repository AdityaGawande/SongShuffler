# import OS
import os
import random

dirname = os.path.dirname(__file__)
directory = os.path.join(dirname, 'songs')

SongList = []

for x in os.listdir(directory):
    if x.endswith(".mp3"):
        # Prints only text file present in My Folder
        x = (dirname+'/'+x)
        x = x.replace('\\', '/')
        SongList.append(x)

# for i in reversed(range(1, len(SongList))):
#             # pick an element in SongList[:i+1] with which to exchange SongList[i]
#             j = random.randint(0, i)
#             SongList[i], SongList[j] = SongList[j], SongList[i]

print(SongList[1])