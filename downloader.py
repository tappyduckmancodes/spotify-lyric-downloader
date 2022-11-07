# coding:utf-8
import os, re, sys, spotipy, itertools, json, requests, base64, linecache, bs4, time, pyautogui, pyperclip, pprint, datetime, shutil, platform, subprocess
import spotipy.util as util
import requests
from os import path
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from pathlib import Path #using this module to solve difference path syntax between Mac OS and Windows

# MAKE SURE THESE ARE CORRECT
CLIENT_ID = '(spotify API client ID here)'
CLIENT_SECRET = '(spotify API client SECRET here)'
REDIRECT_URI =  'http://example.com/example'
authorization='(spotify authorization here)'
# MAKE SURE THESE ARE CORRECT

os.environ['SPOTIPY_CLIENT_ID']  = CLIENT_ID
os.environ['SPOTIPY_CLIENT_SECRET'] = CLIENT_SECRET
os.environ['SPOTIPY_REDIRECT_URI'] = REDIRECT_URI
scope = "user-read-currently-playing"
# spotipy authentication to see currently playing song
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(scope = scope))
current_track = sp.current_user_playing_track()


def replace_line(database, line_num, text):
    lines = open(database, 'r').readlines()
    lines[line_num] = text
    out = open(database, 'w')
    out.writelines(lines)
    out.close()

#for opening folder in various operating system explorers
def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path]) 

#see if song is playing
if current_track == None:
    print("No song detected, make sure you're actively playing a song!")
    os._exit(0)
song_uri_link = current_track.get("item").get("uri").replace('spotify:track:','')
song_name = current_track.get("item").get("name")
cover_link = current_track.get("item").get("album").get("images")[0].get("url")
release_date = current_track.get("item").get("album").get("release_date")
album_name = current_track.get("item").get("album").get("name")
artist_name = current_track.get("item").get("album").get("artists")[0].get("name")
track_number = current_track.get("item").get("track_number")
album_uri_link = current_track.get("item").get("album").get("uri")


# generate lyrics link
original_link = cover_link
a = cover_link
a = a.replace("/", "%2F")
a = a.replace(":", "%3A")
cover_link = a
link_start = "https://spclient.wg.spotify.com/color-lyrics/v2/track/"
lyrics_url = (link_start + song_uri_link + "/image/" + cover_link + "?format=json&vocalRemoval=false&market=from_token")
lyrics_url_no_access = (link_start + song_uri_link + "/image/" + cover_link)

print("Success! Song detected! \n")
print("Song: ", song_name)
print("Album name:", album_name)
print("Artist name:", artist_name)
print("Track number: ", track_number)
print("Release date: ", release_date)
print("Album cover URL:", original_link)
print("Track URI:", song_uri_link)
print("Album URI:", album_uri_link)
print("Lyric URL:", lyrics_url, "\n")

# getting release year for album
release_date = release_date.replace('-', '/')
release_year = release_date[:4]

# creates directory
artist = artist_name
album = (album_name + " (" + release_year + ")")
song = song_name
track_number = track_number
lyrics = "Lyrics"
host_dir = os.getcwd()
# print("Host Directory: \n" + host_dir)

album_info = sp.album_tracks(album_uri_link)

# saves currently playing album info to txt file
result = json.dumps(album_info)
z = open("album_info.txt", "w")
z.write(result)
z.close()
album_database = "album_info.txt"
with open('album_info.txt', 'r') as handle:
    parsed = json.load(handle)
    parsed2 = (json.dumps(parsed, indent=1, sort_keys=True))
with open('album_info.txt', 'w') as file: # line breaks
    file.write(parsed2)
    file.close()

#reading for short line removal
with open('album_info.txt', 'r')  as f:
    lines = f.readlines()
# Removes region codes by removing all short lines
filtered_lines = [line for line in lines if len(line) > 10]
# writing out file w no 2-character country codes
with open('filtered_album_info.txt', 'w') as f:
    for line in filtered_lines:
        f.write(line)
os.remove("album_info.txt")
os.rename('filtered_album_info.txt', "album_info.txt")
#if needed, commewnt below line out for album_info saved to txt
os.remove("album_info.txt")
    
#creates lyrics folder
if os.path.isdir(lyrics):
    os.chdir(lyrics)
    lyricdir = os.getcwd()
else:
    os.mkdir(lyrics)
    os.chdir(lyrics)

#creates artist folder
if os.path.isdir(artist):
    os.chdir(artist)
    artistdir = os.getcwd()
else:
    os.mkdir(artist)
    os.chdir(artist)
    artistdir = os.getcwd()

#creates album folder
if os.path.isdir(album):
    os.chdir(album)
    albumdir = os.getcwd()
else:
    os.mkdir(album)
    os.chdir(album)
    albumdir = os.getcwd()

os.chdir(host_dir)

#set up variables for moving lyric and setting up cover.jpg location
host_folder = host_dir
lyrics = "Lyrics"
artist_name = artist_name
albumdir = albumdir
song = song
cover = lyrics_url
originallyricsfile = (Path(host_folder)/"output.lrc")
movedlyricsfile = (Path(albumdir)/(str(track_number) + ". " + str(song) + ".lrc"))
movedcoverjpg = (Path(albumdir)/"cover.jpg")

#checks if cover exists, if not it downloads
os.chdir(albumdir)
try:
    f = open(movedcoverjpg)
    print("Cover already downloaded, skipping download.")
    f.close()
except IOError:
    print("No cover.jpg detected, downloading now")
    cover =requests.get(original_link).content
    f = open(movedcoverjpg,'wb')
    f.write(cover)
    f.close()
    print("Cover downloaded!")

os.chdir(host_dir)
#checks if lyric exists, if not it downloads
try:
    f = open(movedlyricsfile)
    print("Lyric already downloaded, skipping download. Enjoy!")
    f.close()
    open_file(albumdir)
    os.remove("currentsong.txt")
    quit()

except IOError:
    print("No lyric detected, downloading now")

headers = {
    'Host': 'spclient.wg.spotify.com',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'accept-language': 'en',
    'sec-ch-ua-mobile': '?0',
    'app-platform': 'WebPlayer',
    'authorization': authorization,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'spotify-app-version': '1.1.98.597.g7f2ab0d4',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://open.spotify.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://open.spotify.com/',
}
params = {
    'format': 'json',
    'vocalRemoval': 'false',
    'market': 'from_token',
}
response = requests.get(lyrics_url, params=params, headers=headers)
lyricdata=response.text
#print(lyricdata)
z = open("lyrics.txt", "w", encoding="utf-8")
z.write(lyricdata)
z.close()
print("Successfully saved page text, will verify...")
