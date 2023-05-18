from pydub import AudioSegment
from pydub.playback import play
import random

playlist = [
    ("/home/ganesh/Downloads/playlist/IMG_0553.mp3", "IMG_0553.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0555.mp3", "IMG_0555.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0556.mp3", "IMG_0556.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0557.mp3", "IMG_0557.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0558.mp3", "IMG_0558.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0559.mp3", "IMG_0559.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0560.mp3", "IMG_0560.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0561.mp3", "IMG_0561.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0562.mp3", "IMG_0562.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0563.mp3", "IMG_0563.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0565.mp3", "IMG_0565.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0566.mp3", "IMG_0566.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0567.mp3", "IMG_0567.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0568.mp3", "IMG_0568.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0569.mp3", "IMG_0569.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0570.mp3", "IMG_0570.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0571.mp3", "IMG_0571.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0572.mp3", "IMG_0572.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0574.mp3", "IMG_0574.mp3"),
    ("/home/ganesh/Downloads/playlist/IMG_0575.mp3", "IMG_0575.mp3")
]

songs = [(AudioSegment.from_file(file), name) for file, name in playlist]

# Shuffle the songs
random.shuffle(songs)
count = 0
next_song = True

# Infinite loop
while True:
    song, name = songs[count]
    print("PLAYING:", name)
    play(song)
    print("Press 'r' to replay, Press 'e' to exit, Press 'b' for the previous song")
    print("Press 'n' for the next song")
    query = input(" ")

    if query == 'n':
        count += 1
    elif query == 'r':
        # Resuming the music
        if next_song:
            continue
    elif query == 'e':
        break
    elif query == 'b':
        if count != 0:
            count -= 1
            continue
        else:
            count = len(songs) - 1
            continue

    # Returning

