import os, re, sys, spotipy, itertools, json, requests, base64, linecache, webbrowser, bs4, time, pyautogui, pyperclip, urllib3, pprint, datetime
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

with open('currentsong.txt', 'r') as handle:
    parsed = json.load(handle)
    parsed2 = (json.dumps(parsed, indent=0, sort_keys=True))

with open('currentsong.txt', 'w') as file: # line breaks
    file.write(parsed2)
    file.close()

#reading for short line removal
with open('currentsong.txt', 'r')  as f:
    lines = f.readlines()
# Removes region codes by removing all short lines
filtered_lines = [line for line in lines if len(line) > 10]
# writing out file w no 2-character country codes
with open('filtered.txt', 'w') as f:
    for line in filtered_lines:
        f.write(line)

database = "currentsong.txt"
def search_string_in_file(database, string_to_search):
    #    Search for the given string in file and return lines containing that string,
#    along with line numbers
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(database, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results

def replace_line(database, line_num, text):
    lines = open(database, 'r').readlines()
    lines[line_num] = text
    out = open(database, 'w')
    out.writelines(lines)
    out.close()

#i dont know how to make tables so this finds text and finds the line below which is the string needed
song_uri_link = search_string_in_file(database, 'spotify:track:')
song_name = search_string_in_file(database, '"preview_url": "https://p.scdn.co/mp3-preview/')
cover_link = search_string_in_file(database,'"width": 640')
release_date = search_string_in_file(database,'"release_date":')
album_name = search_string_in_file(database,'"release_date":')
artist_name = search_string_in_file(database,'"artists": [')
track_number = search_string_in_file(database,'"track_number":')
album_uri_link = search_string_in_file(database, 'spotify:album:')

#song name
for elem in song_name:
    song_name = elem[0] - 3
    f = open("currentsong.txt","r")
    lines = f.readlines()
    # logic for finding song name, and assigning it to some variable
    x = lines[song_name]
    x = x.replace('"name": "', '')
    x = x.replace('\\u00e9', 'é')
    x = x.replace('\\u00e0', 'à')
    x = x.replace('\\u2019', "'")
    x = x.replace('\\u0027', '\'')
    x = x.replace('\\u2022', '·')
    x = x.replace('?', '')
    x = x.replace('"', '')
    x = x.replace('/', '-')
    x = x.replace('|', '-')
    x = x.replace('\\', '')
    x = x.replace(':', ' =')
    x = x.replace(';', '-')
    size = len(x)
    minus_quote_and_comma = x[:size - 2]
    song_name = minus_quote_and_comma

#cover URL
for elem in cover_link:
    cover_link = elem[0] - 2
    f = open("currentsong.txt","r")
    lines = f.readlines()
    # logic for finding song name, and assigning it to some variable
    x = lines[cover_link]
    x = x.replace('"url": "https:', 'https:')
    size = len(x)
    minus_quote_and_comma = x[:size - 3]
    cover_link = minus_quote_and_comma

# Song URI
for elem in song_uri_link:
    song_uri_link = elem[0] - 1
    f = open("currentsong.txt","r")
    lines = f.readlines()
    # logic for finding song name, and assigning it to some variable
    x = lines[song_uri_link]
    x = x.replace('"uri": "spotify:track:', '')
    size = len(x)
    minus_quote = x[:size - 2]
    song_uri_link = minus_quote

# Album URI
for elem in album_uri_link:
    album_uri_link = elem[0] - 1
    f = open("currentsong.txt","r")
    lines = f.readlines()
    # logic for finding song name, and assigning it to some variable
    x = lines[album_uri_link]
    x = x.replace('"uri": "spotify:album:', 'spotify:album:')
    size = len(x)
    minus_quote = x[:size - 2]
    album_uri_link = minus_quote

# Track Number
for elem in track_number:
    track_number = elem[0] - 1
    f = open("currentsong.txt","r")
    lines = f.readlines()
    # logic for finding song name, and assigning it to some variable
    x = lines[track_number]
    x = x.replace('"track_number": ', '')
    size = len(x)
    minus_quote = x[:size - 2]
    track_number = minus_quote

# Release Date
for elem in release_date:
    release_date = elem[0] - 1
    f = open("currentsong.txt","r")
    lines = f.readlines()
    # logic for finding song name, and assigning it to some variable
    x = lines[release_date]
    x = x.replace('\\u00e9', 'é')
    x = x.replace('\\u00e0', 'à')
    x = x.replace('\\u2019', "'")
    x = x.replace('\\u0027', '\'')
    x = x.replace('\\u2022', '·')
    x = x.replace('"name": "', '')
    x = x.replace('?', '')
    x = x.replace('"', '')
    x = x.replace('/', '')
    x = x.replace('|', '-')
    x = x.replace('\\', '')
    x = x.replace(':', ' -')
    x = x.replace(';', '-')
    x = x.replace('release_date - ', '')
    size = len(x)
    minus_quote_and_comma = x[:size - 2]
    release_date = minus_quote_and_comma

# Album Name
for elem in album_name:
    album_name = elem[0] - 2
    f = open("currentsong.txt","r")
    lines = f.readlines()
    # logic for finding song name, and assigning it to some variable
    x = lines[album_name]
    x = x.replace('\\u00e9', 'é')
    x = x.replace('\\u00e0', 'à')
    x = x.replace('\\u2019', "'")
    x = x.replace('\\u0027', '\'')
    x = x.replace('\\u2022', '·')
    x = x.replace('"name": "', '')
    x = x.replace('?', '')
    x = x.replace('"', '')
    x = x.replace('/', '')
    x = x.replace('|', '-')
    x = x.replace('\\', '')
    x = x.replace(':)', ' =)')
    x = x.replace(': ', ' - ')
    x = x.replace(';', '-')
    x = x.replace(',\n', '')
    album_name = x

# Artist Name
for elem in artist_name:
    artist_name = elem[0] + 6
    f = open("currentsong.txt","r")
    lines = f.readlines()
    # logic for finding song name, and assigning it to some variable
    x = lines[artist_name]
    x = x.replace('\\u00e9', 'é')
    x = x.replace('\\u00e0', 'à')
    x = x.replace('\\u2019', "'")
    x = x.replace('\\u0027', '\'')
    x = x.replace('\\u2022', '·')
    x = x.replace('"name": "', '')
    x = x.replace('?', '')
    x = x.replace('"', '')
    x = x.replace('/', '')
    x = x.replace('|', '-')
    x = x.replace('\\', '')
    x = x.replace(':', ' -')
    x = x.replace(';', '-')
    x = x.replace(':)', ' =)')
    size = len(x)
    minus_quote_and_comma = x[:size - 2]
    artist_name = minus_quote_and_comma
    f.close()

# generate lyrics link
original_link = cover_link
a = cover_link
a = a.replace("/", "%2F")
a = a.replace(":", "%3A")
cover_link = a
link_start = "https://spclient.wg.spotify.com/color-lyrics/v2/track/"
lyrics_url = (link_start + song_uri_link + "/image/" + cover_link + "?format=json&vocalRemoval=false&market=from_token")
lyrics_url_no_access = (link_start + song_uri_link + "/image/" + cover_link)

#see if song is playing
filesize = os.path.getsize("currentsong.txt")
if filesize == 4:
    print("No song detected, make sure you're actively playing a song!")
    os.remove("currentsong.txt")
    quit()
else:
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

link_for_cookie = "https://open.spotify.com/lyrics"
lyrics = webbrowser.open(link_for_cookie, new=0, autoraise=True)
time.sleep(10)
lyrics = webbrowser.open(lyrics_url, new=0, autoraise=True)
time.sleep(1.2)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.1)
pyautogui.hotkey('ctrl', 'w')
pyautogui.hotkey('ctrl', 'w')
print("Tab closed and lyrics copied! \n")
lyricdata = pyperclip.paste()
z = open("lyrics.txt", "w", encoding="utf-8")
z.write(lyricdata)
z.close()
print("Successfully saved page text, will verify...")
