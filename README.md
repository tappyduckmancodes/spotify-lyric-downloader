# spotify-lyrics-to-lrc
Converts between Spotify's new lyrics (and their proprietary format) to an LRC file for local playback.

Open Spotify web player
Choose desired song
Open Chrome dev tools Network tab
Click lyric button
find the link in Network Tools that starts with "https://spclient.wg.spotify.com/color-lyrics/v2/track" and open it
Copy and paste entire chunk of text into "lyrics.txt" and save it
Run "clicktoconvert.bat"
Done! Rename output.lrc file to desired filename.
