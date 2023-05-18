from pydub import AudioSegment
from pydub.playback import play
import random

playlist=["/home/ganesh/Downloads/playlist/IMG_0553.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0555.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0556.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0557.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0558.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0559.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0560.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0561.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0562.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0563.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0565.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0566.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0567.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0568.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0569.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0570.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0571.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0572.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0574.mp3",
          "/home/ganesh/Downloads/playlist/IMG_0575.mp3"]
          
songs = [AudioSegment.from_file(file) for file in playlist]

# Shuffle the songs
random.shuffle(songs)
count = 0
next = True 
# infinite loop
while True:
	song = songs[count]
	print("PLAYING")
	play(song)
	print(" 'r' to replay", "'e' ")
	print("Press 'n' to next song")
	query = input(" ")	
	if query == 'n':
	        count += 1
	        continue
	elif query == 'r':
# Resuming the music
		if next: 
	         continue
	elif query == 'e' :
	        break        
	if index == len(songs):
	                      index = 0
		             

