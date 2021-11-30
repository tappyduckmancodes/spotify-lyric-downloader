# spotify-lyrics-to-lrc
Converts between Spotify's new lyrics (and their proprietary format) to an LRC file for local playback.

---------------------------------------------------------------------
How to use:

Open Spotify web player

Choose desired song

Open Chrome dev tools, open Network tab

Click lyric button

find the link in Network Tools that starts with "https://spclient.wg.spotify.com/color-lyrics/v2/track" and open it

Copy and paste entire chunk of text into "lyrics.txt" and save it

Run "converter.py"

Done! Rename output.lrc file to desired filename.

