# **spotify-lyric-downloader**
Rips lyrics from currently playing song on Spotify, converts to LRC format for offline playback (e.g Plex, Kodi, MusicBee)

---------------------------------------------------------------------
# Requisites:

> pip install os re sys spotipy itertools json requests base64 linecache webbrowser bs4 time pyautogui pyperclip urllib3 pprint datetime shutil platform subprocess

---------------------------------------------------------------------
# How to set up:

· Go to the [Spotify API Dashboard](https://developer.spotify.com/dashboard/applications)

· Create an app and enter "example.com/example" as the Redirect URI in the settings

· copy client ID, secret, and "example.com/example" from Spotify API Dashboard and put them into lyricdownloader.py

· Run converter.py

· Sign into Spotify

· It will redirect you to a link based off your URI, copy everything but "example.com/example" from the url and paste it into the console

· Close it out
  
---------------------------------------------------------------------

# How to use:

· Listen to a song on Spotify web player (and be signed in on the normal https://open.spotify.com/ site)

· open converter.py in a cmd or git-bash terminal

· Wait about 10 seconds

· Once complete, check "Lyrics" folder for grouping by artist, album, and track number and title.
