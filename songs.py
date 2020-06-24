from pytube import YouTube
from moviepy.editor import *
import datetime

# using now() to get current time
current_time = datetime.datetime.now()

# Printing value of now.
print("Time now at greenwich meridian is : ", end="")
print(current_time)

# Put the songs in the file in a list
songs_list = []
songs_file = open('songs.txt')
songs_list = songs_file.read().split()

# Remove duplicates from the list
songs_list = list(dict.fromkeys(songs_list))

# Download a file with only audio, to save space
# if the final goal is to convert to mp3

for song in songs_list:

    youtube_link = song
    y = YouTube(youtube_link)
    t = y.streams.filter(only_audio=True).all()
    t[0].download(output_path=r'C:\Users\user\Desktop\songsMeran')

print("Time now at greenwich meridian is : ", end="")
print(current_time)
