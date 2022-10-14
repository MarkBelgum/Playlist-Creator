import random
import os
import statistics

artistPath="/Users/markbelgum/Music/Queen/"  #path to the folder with all of the albums you want to pull from
# array of folder names for each album
albums=["Queen","Queen II","Sheer Heart Attack","A Night At The Opera","A Day At The Races","News Of The World","Jazz",
        "The Game","Flash Gordon","Hot Space","The Works","A Kind Of Magic","The Miracle","Innuendo","Made In Heaven"]
filePath="/Users/markbelgum/Documents/Music/Custom Playlists/Queen.m3u" # path to the file to be imported into iTunes
cycles=12   # number of times the playlist will cycle through the albums as an integer


# randomizes order of all tracks in an album
def getTracks(album):
    pathList=[]
    albumPath=artistPath+album+"/"
    for track in os.listdir(albumPath):
        path = os.path.join(albumPath, track)
        if ("jpg" not in track and "reapeaks" not in track and "13" not in track):
            pathList.append(path)

    return sorted(pathList, key = lambda x: random.random())

# factors allow for an even distribution of songs from an album throughout the playlist
def adjustFactors():
    for index in range(0,len(factorsSource)):
        factor=round(factorsSource[index],5)
        indexLoop=index+1
        while indexLoop<len(factorsSource):
            if round(factorsSource[indexLoop],5)==factor:
                factors[indexLoop]+=factor
            indexLoop+=1
        factor=factors[index]
        factors[index]=round(factor%1,5)
    pass

# places tracks in order evenly
def placeTracks(albumIndex):
    factor=factors[albumIndex]+factorsSource[albumIndex]
    while factor>=1:
        if len(tracks[indexLoop])>0:
            file.write(tracks[albumIndex].pop(0)+"\n")
        factor-=1
    factors[albumIndex]=factor
    pass

# initialize                                                    
tracks=[]
numTracks=[]
factorsSource=[]
factors=[]
isFinished=False

# place album arrays with randomized tracks into tracks array
for album in albums:
    albumTracks=getTracks(album)
    tracks.append(albumTracks)
    numTracks.append(len(albumTracks))
    factorsSource.append(round((len(albumTracks)/cycles),5))
    factors.append(round((len(albumTracks)/cycles),5))

adjustFactors()

# write to file
file = open(filePath, "w")

while isFinished==False:
    isFinished=True
    for indexLoop in range(0,len(tracks)):
        if len(tracks[indexLoop])>0:
            isFinished=False
            placeTracks(indexLoop)

file.close()

# check that all tracks have been placed
count=0
for album in tracks:
    count+=len(album)
if count != 0:
    print("Some tracks were not placed")

# recommended cycles is a good place to start for the number of cycles
print("\nRecommended number of cycles:", int(statistics.median(numTracks)),"\n")
