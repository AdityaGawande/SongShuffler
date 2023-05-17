import tkinter as tk
import pygame
from tkinter import filedialog
import os
import random

dirname = os.path.dirname(__file__)
song_path = os.path.join(dirname, 'songs')

SongList = []

for x in os.listdir(song_path):
    if x.endswith(".mp3"):
        x = (song_path+'/'+x)
        SongList.append(x)

PlaylistEnd = len(SongList) - 1

def NewListGen():
    global PlaylistEnd
    SongList.clear()
    for x in os.listdir(song_path):
        if x.endswith(".mp3"):
            x = (song_path+'\\'+x)
            SongList.append(x)
    PlaylistEnd = len(SongList) - 1

def shuffle():
    for i in reversed(range(1, len(SongList))):
            # pick an element in SongList[:i+1] with which to exchange SongList[i]
            j = random.randint(0, i)
            SongList[i], SongList[j] = SongList[j], SongList[i]

Position = 0
Playback = False
def PlaybackToggle():
    global Playback
    if Playback:
        Playback = False
    else:
        Playback = True

shuffle()


# Initialize Pygame mixer
pygame.mixer.init()

def play_song():
    path = repr(SongList[Position])[1:-1]
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    PlaybackToggle()

def next_song():
    global Position
    if Position < PlaylistEnd:
        Position += 1
    else:
        shuffle()
        Position = 0
    pygame.mixer.music.load(SongList[Position])
    pygame.mixer.music.play()
    PlaybackToggle()

def prev_song():
    global Position
    if Position > 0:
        Position -= 1
    pygame.mixer.music.load(SongList[Position])
    pygame.mixer.music.play()
    PlaybackToggle()

def stop_song():
    pygame.mixer.music.stop()
    PlaybackToggle()


def pause_song():
    pygame.mixer.music.pause()
    PlaybackToggle()


def choose_directory():
    global song_path
    song_path = filedialog.askdirectory()
    NewListGen()


def resume_song():
    pygame.mixer.music.unpause()
    PlaybackToggle()


# Create the main window
window = tk.Tk()
window.title("Song Shuffler")

# Create buttons for choosing, playing, pausing, stopping, and resuming the song
choose_button = tk.Button(window, text="Choose Folder", command=choose_directory)
choose_button.pack()

play_button = tk.Button(window, text="Play Song", command=play_song)
play_button.pack()

pause_button = tk.Button(window, text="Pause Song", command=pause_song)
pause_button.pack()

resume_button = tk.Button(window, text="Resume Song", command=resume_song)
resume_button.pack()

next_button = tk.Button(window, text="Next Song", command=next_song)
next_button.pack()

prev_button = tk.Button(window, text="Previous Song", command=prev_song)
prev_button.pack()

stop_button = tk.Button(window, text="Stop Song", command=stop_song)
stop_button.pack()

# Run the GUI
window.mainloop()
