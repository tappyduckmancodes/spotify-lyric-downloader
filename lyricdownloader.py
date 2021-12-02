import os, re, sys, spotipy, itertools, json, requests, base64, linecache, webbrowser, bs4, time, pyautogui, pyperclip, urllib3
import spotipy.util as util
from os import path
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

# MAKE SURE THESE ARE CORRECT
CLIENT_ID = '(spotify API client ID here)'
CLIENT_SECRET = '(spotify API client SECRET here)'
REDIRECT_URI =  '(spotify API REDIRECT URI here)'
# MAKE SURE THESE ARE CORRECT

os.environ['SPOTIPY_CLIENT_ID']  = CLIENT_ID
os.environ['SPOTIPY_CLIENT_SECRET'] = CLIENT_SECRET
os.environ['SPOTIPY_REDIRECT_URI'] = REDIRECT_URI
scope = "user-read-currently-playing"
# spotipy authentication to see currently playing song
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(scope = scope))
current_track = sp.current_user_playing_track()

# saves currently playing song info to txt file
result = json.dumps(current_track)
z = open("currentsong.txt", "w")
z.write(result)
z.close()


# attempting to clean up the rest of the text
with open('currentsong.txt', 'r') as file :
    filedata = file.read()
filedata = filedata.replace(', ', ', \n')

with open('currentsong.txt', 'w') as file: # line breaks
    file.write(filedata)

#reading for short line removal
with open('currentsong.txt', 'r')  as f:
    lines = f.readlines()
# Removes region codes by removing all short lines
filtered_lines = [line for line in lines if len(line) > 10]
# writing out file w no 2-character country codes
with open('filtered.txt', 'w') as f:
    for line in filtered_lines:
        f.write(line)

os.remove("currentsong.txt") # deletes leftover file



def search_string_in_file(file_name, string_to_search):
#    Search for the given string in file and return lines containing that string,
#    along with line numbers
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

with open('filtered.txt', 'r') as file :
    filedata = file.read()
filedata = filedata.replace(',', '\n')
with open('filtered.txt', 'w') as file:
    file.write(filedata)

#i dont know how to make tables so this finds text and finds the line below which is the string needed
uri_links = search_string_in_file('filtered.txt', '"uri": "spotify:track:')
names = search_string_in_file('filtered.txt', '"name": ')
cover_link = search_string_in_file('filtered.txt','"width": 640}')
artist_name = search_string_in_file('filtered.txt','"type": "artist"')
album_name = search_string_in_file('filtered.txt','"width": 64}]')
album_name_pt2 = search_string_in_file('filtered.txt','"release_date": ')

# get song uri
for elem in uri_links:
    uri_url = elem[0]

# get url of 640x640 album cover
for elem in cover_link:
    album_url = elem[0] -2

#song title
for elem in names:
    name_text = elem[0]

#album title
releasedatetag = '"release_date":'
for elem in album_name:
    album_title = elem[0] + 2

#artist name
for elem in artist_name:
    artist = elem[0] - 2

# shitty variables
album_line = linecache.getline('filtered.txt', album_url)
uri_line = linecache.getline('filtered.txt', uri_url)
title_line = linecache.getline('filtered.txt', name_text)
album_cover_line = linecache.getline('filtered.txt', album_title)
artist_line = linecache.getline('filtered.txt', artist)

# writes all fields to file
full_line = ("Album Cover: " + album_line + "\n" + "Track URI: " + uri_line + "\n" + title_line + "\n" + album_cover_line + "\n" + artist_line)

with open('corrected.txt', 'w') as file:
    file.write(full_line)

#os.remove('filtered.txt')
#more shitty replacement
with open('corrected.txt', 'r') as file :
    filedata = file.read()
filedata = filedata.replace('Album Cover: "url": ', 'Album Cover: \n')
filedata = filedata.replace('Track URI: "uri": "spotify:track:', 'Track URI: \n')
filedata = filedata.replace('}', '')
filedata = filedata.replace(']', '')
filedata = filedata.replace('"', '')
filedata = filedata.replace('\\u00e9', 'é')
filedata = filedata.replace('\\u00e0', 'à')
filedata = filedata.replace('\\u2019', "'")
filedata = filedata.replace('\\u0027', '\'')

with open('corrected.txt', 'w') as file:
    file.write(filedata)
file.close()


# math to find which line corresponds to which field
album = search_string_in_file('corrected.txt','name:')
for elem in album:
    album = elem[0] - 4
song = elem[0] - 3
band = elem[0] - 5

replace_line('corrected.txt', album, 'Album: ')
replace_line('corrected.txt', song, 'Band: ')

#more replacement
with open('corrected.txt', 'r') as file :
    filedata = file.read()
filedata = filedata.replace('name: ', '')
with open('corrected.txt', 'w') as file:
    file.write(filedata)
file.close()

# add song name descriptor
f = open("corrected.txt", "r")
contents = f.readlines()
f.close()
contents.insert(band, "Song: ")
f = open("corrected.txt", "w")
contents = "".join(contents)
f.write(contents)
f.close()


#concatenating lyrics link

link_start = "https://spclient.wg.spotify.com/color-lyrics/v2/track/"
a_file = open("corrected.txt", "r")
lines_to_read = [5]
for position, line in enumerate(a_file):

#Iterate over each line and its index

    if position in lines_to_read:
        print(line)

track_uri = search_string_in_file('corrected.txt', 'Track URI: ')
for elem in track_uri:
    print('Line Number = ', elem[0], ' :: Line = ', elem[1])
track_concat = elem[0]  

album_line = linecache.getline('corrected.txt', track_concat)

# get uri and store as variable
a_file = open( "corrected.txt", "r" )
lines_to_read = [track_concat]
for position, line in enumerate(a_file):
    if position in lines_to_read: 
        uri = line
a_file.close()

# get album cover link
a_file = open( "corrected.txt", "r" )
lines_to_read = [1]
for position, line in enumerate(a_file):
    if position in lines_to_read: 
        cover = line
a_file.close()

a = cover
a2 = (a.replace(":", "%3A"))
coverreplacement = (a2.replace("/", "%2F"))

full_url = (link_start + uri + "/image/" + coverreplacement + "?format=json&vocalRemoval=false&market=from_token")
lyric_url = str(full_url) 

full_link= lyric_url.replace("\n", "")
URL = full_link
URL2 = "https://open.spotify.com/lyrics"
lyricsmaybe = webbrowser.open(URL2, new=0, autoraise=True)
time.sleep(5)
lyricsmaybe = webbrowser.open(URL, new=0, autoraise=True)
time.sleep(1.2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.1)
pyautogui.hotkey('ctrl', 'w')
pyautogui.hotkey('ctrl', 'w')
print("tab closed")

lyricdata = pyperclip.paste()
z = open("lyrics.txt", "w", encoding="utf-8")
z.write(lyricdata)
z.close()

print(cover)

#cover # album cover link
artistdirectory = artist_line
artistdirectory = artistdirectory.replace('"name": "', '')
artistdirectory = artistdirectory.replace('"\n', '')
artistdirectory = artistdirectory.replace('\\u0027', '\'')
artistdirectory = artistdirectory.replace('"', '')
artistdirectory = artistdirectory.replace('\\u2018', "\\u2019")
artistdirectory = artistdirectory.replace('\\u2019', "'")
artistdirectory = artistdirectory.replace('\\u2022', '•')
albumdirectory = album_cover_line
albumdirectory = albumdirectory.replace('"name": "', '')
albumdirectory = albumdirectory.replace('"name": "', '')
albumdirectory = albumdirectory.replace(')\n', ')')
albumdirectory = albumdirectory.replace('"', '')
albumdirectory = albumdirectory.replace('\\n', '')
albumdirectory = albumdirectory.replace('\\u2018', "\\u2019")
albumdirectory = albumdirectory.replace('\\u2019', "'")
albumdirectory = albumdirectory.replace('\\u0027', '\'')
albumdirectory = albumdirectory.replace('\\u2022', '•')
songname = title_line
songname = songname.replace('"name": "', '')
songname = songname.replace('"name": "', '')
songname = songname.replace('\\u0027', '\'')
songname = songname.replace('\\u2018', "'")
songname = songname.replace('\\u2019', "'")
songname = songname.replace('"', '')

size = len(albumdirectory)
# Slice string to remove last 2 characters from string
mod_string = albumdirectory[:size - 1]
print(mod_string)

size1 = len(songname)
# Slice string to remove last 2 characters from string
mod_string_1 = songname[:size1 - 1]
print(mod_string_1)

#sorts lyric file
artist = artistdirectory
album = mod_string
song = songname
lyrics = "Lyrics"
host_dir = os.getcwd()
print("Host Directory: \n" + host_dir)

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
