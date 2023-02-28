# Playlist-Creator
The Best Playlist Creator Ever! Takes a random song from every album of an artist you have music files and makes a playlist in the album order of your choosing. I initially created this to spice up listening to my favorite artists when I couldn't choose one album to listen to. The end result is an m3u file that you can open in iTunes or Apple music (and probably other media players).

TLDR: modify the variables in lines 5-10 for your files.

```python
artistPath="/Users/markbelgum/Music/Queen/"  #path to the folder with all of the albums you want to pull from
# array of folder names for each album
albums=["Queen","Queen II","Sheer Heart Attack","A Night At The Opera","A Day At The Races","News Of The World","Jazz",
        "The Game","Flash Gordon","Hot Space","The Works","A Kind Of Magic","The Miracle","Innuendo","Made In Heaven"]
filePath="/Users/markbelgum/Documents/Music/Custom Playlists/Queen.m3u" # path to the file to be imported into iTunes
cycles=12   # number of times the playlist will cycle through the albums as an integer
```
