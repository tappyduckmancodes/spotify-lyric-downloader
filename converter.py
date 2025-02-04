# coding:utf-8
import os, re, sys, itertools, json, requests, base64, linecache, time, requests, bs4, time, pyautogui, pyperclip, pprint, shutil, platform, subprocess
import downloader
from pathlib import Path #using this module to solve difference path syntax between Mac OS and Windows
host_folder = downloader.host_dir #get work path
os.chdir(host_folder) #change path to work path
lyrics_url = downloader.lyrics_url

# Read in the jumbled Spotify lyric text
with open('lyrics.txt', 'r', encoding='UTF-8') as file:
    filedata = file.read()
    fullstring = filedata
substring_403 = "HTTP ERROR 403"
substring_401 = '"status": 401,'
substring_success = "lyrics"

print("Searching for valid lyrics...")
# exception for songs with no lyrics
if substring_403 in fullstring:
    os.remove("lyrics.txt")
    print("Lyrics not available for this song, sorry!")
    if len(os.listdir(downloader.albumdir)) == 0: # Check if the album folder is empty
        shutil.rmtree(downloader.albumdir) # If so, delete it
        if len(os.listdir(downloader.artistdir)) == 0: # Check if the artist folder is empty
            shutil.rmtree(downloader.artistdir) # If so, delete it
            quit()
# exception with no token, just redownloads it based on lyrics_url
elif substring_401 in fullstring:
    print("Error, token has been expired, please open the browser to get a new one and restart the program")
    os._exit(0)
    
#exception for successful lyric grab
elif substring_success in fullstring:
    print("Lyric grab was success, converting now...")
    with open('lyrics.txt', 'r', encoding='UTF-8') as file:
        filedata = file.read()
        fullstring = filedata

# Remove some of the Spotify formatting
filedata = filedata.replace('},', '} \n')
filedata = filedata.replace('{"lyrics":{"syncType":"LINE_SYNCED","lines":[', '')
filedata = filedata.replace('\\u0027', '\'')
filedata = filedata.replace('{"startTimeMs":"', '[')
filedata = filedata.replace(',"syllables":[]} ', '')
filedata = filedata.replace('","words":', ']')
filedata = filedata.replace('"', '')
filedata = filedata.replace('hasVocalRemoval:false}', '')
filedata = filedata.replace(']', '] ')
filedata = filedata.replace('\\', '*')
filedata = filedata.replace(',syllables:[] ,endTimeMs:0}', '')

# Write the file out
with open('lyricsfixed.lrc', 'w', encoding='UTF-8') as file:
    file.write(filedata)

# remove leftover shit from Spotify that doesnt apply to lrc files
with open("lyricsfixed.lrc", "r", encoding='UTF-8') as f:
    lines = f.readlines()
with open("lyricsfixed.lrc", "w", encoding='UTF-8') as new_f:
    for line in lines:
        if not line.startswith("colors:{background"):
            new_f.write(line)

# removes last line of gibberish
import os, sys, re
readFile = open("lyricsfixed.lrc", 'r', encoding='UTF-8')
lines = readFile.readlines()
readFile.close()
w = open("lyricsfixed.lrc",'w', encoding='UTF-8')
w.writelines([item for item in lines[:-1]])
w.close()

with open('lyricsfixed.lrc', 'r', encoding='UTF-8') as file:
    filedata = file.read()
# I keep initializing it the same way and just reassigning the filedata string because i am idiot brain (stop doing this!)
test_str = filedata

# Extracts all regions in ms into a string
# Using regex which i do not get at all
res = re.findall(r"\[\s*\+?(-?\d+)\s*\]", test_str)
# saving timings to timings.txt
file = open("timings.txt", "w")

formatted_times = [] #timing conversion
for time in res:
  millis = int((int(time) % 1000) / 10)
  secs = int(int(time) / 1000)
  mins = int(secs / 60)
  secs = secs % 60
  formatted_times.append(f"{mins}:{secs}.{millis}")

text = '] \n'.join(formatted_times) # line breaks
file.write(text)
file.close()

# Read in the file
with open('timings.txt', 'r', encoding='UTF-8') as file:
    filedata = file.read()

# Bad logic to add brackets and keep timing scheme consistent because im dumb
filedata = filedata.replace('0:', '[00:')
filedata = filedata.replace('1:', '[01:')
filedata = filedata.replace('2:', '[02:')
filedata = filedata.replace('3:', '[03:')
filedata = filedata.replace('4:', '[04:')
filedata = filedata.replace('5:', '[05:')
filedata = filedata.replace('6:', '[06:')
filedata = filedata.replace('7:', '[07:')
filedata = filedata.replace('8:', '[08:')
filedata = filedata.replace('9:', '[09:')
filedata = filedata.replace(':0.', ':00.')
filedata = filedata.replace(':1.', ':01.')
filedata = filedata.replace(':2.', ':02.')
filedata = filedata.replace(':3.', ':03.')
filedata = filedata.replace(':4.', ':04.')
filedata = filedata.replace(':5.', ':05.')
filedata = filedata.replace(':6.', ':06.')
filedata = filedata.replace(':7.', ':07.')
filedata = filedata.replace(':8.', ':08.')
filedata = filedata.replace(':9.', ':09.')
filedata = filedata.replace('.9]', '.90]')
filedata = filedata.replace('.8]', '.80]')
filedata = filedata.replace('.7]', '.70]')
filedata = filedata.replace('.6]', '.60]')
filedata = filedata.replace('.5]', '.50]')
filedata = filedata.replace('.4]', '.40]')
filedata = filedata.replace('.3]', '.30]')
filedata = filedata.replace('.2]', '.20]')
filedata = filedata.replace('.1]', '.10]')
filedata = filedata.replace('.0]', '.00]')
with open('timingsfixed.txt', 'w', encoding='UTF-8') as file:
    file.write(filedata)

with open('timingsfixed.txt', 'r', encoding='UTF-8') as file:
    filedata = file.read()
filedata = filedata.replace('1 ', '1]')
filedata = filedata.replace('2 ', '2]')
filedata = filedata.replace('3 ', '3]')
filedata = filedata.replace('4 ', '4]')
filedata = filedata.replace('5 ', '5]')
filedata = filedata.replace('6 ', '6]')
filedata = filedata.replace('7 ', '7]')
filedata = filedata.replace('8 ', '8')
filedata = filedata.replace('9 ', '9]')

# bad file editing to catch the last bracket not applying
s1 = filedata
s2 = "]"
filedatawithlastbracket = (s1 + s2) 

with open('timingsfixed.txt', 'w', encoding='UTF-8') as file:
    file.write(filedatawithlastbracket)

os.remove("timings.txt")
os.rename('timingsfixed.txt', 'timingsfixed.lrc')

with open('lyricsfixed.lrc', 'r', encoding='UTF-8') as file:
    filedata = file.read()
# doing what i did earlier, very janky and very backwards, to extract whats *not* in the brackets to get the words to apply the new times to
test_str = filedata
a_string = test_str
modified_string = re.sub(r"\[\s*\+?(-?\d+)\s*\]", "", a_string) # just the words from the song, prints without timecodes
# print(modified_string)

with open('lyricstimingsremoved.txt', 'w', encoding='UTF-8') as file:
    file.write(modified_string)

from itertools import zip_longest
with open('timingsfixed.lrc', 'r', encoding='UTF-8') as file:
    filedata = file.read()
with open('lyricstimingsremoved.txt', 'r', encoding='UTF-8') as file1:
    test_str = file1.read()
#combines new timing and lyric files, A/B/A/B style, no AA/BB
with open('timingsfixed.lrc', 'r', encoding='UTF-8') as src1, open('lyricstimingsremoved.txt', 'r', encoding='UTF-8') as src2, open('output.lrc', 'w', encoding='UTF-8') as dst:
    for line_from_first, line_from_second in itertools.zip_longest(src1, src2):
        if line_from_first is not None:
            dst.write(line_from_first)
        if line_from_second is not None:
            dst.write(line_from_second)

with open('output.lrc', 'r', encoding='UTF-8') as file:
    filedata = file.read()
filedata = filedata.replace('   ', '')
with open('output.lrc', 'w', encoding='UTF-8') as file:
    file.write(filedata)
#combines into one line where line breaks can be added
with open('output.lrc', 'r', encoding='UTF-8') as f:
    all_lines = f.readlines()
    all_lines = [x.strip() for x in all_lines if x.strip()]
    two_lines = " ".join(x for x in all_lines[:2])
    lines_left = " ".join(x for x in all_lines[2:])

oneline = (two_lines + lines_left)
#everything put into one line, needed for line breaks

# Breaks multiple lines colliding making LRC file unreadable
oneline = oneline.replace(' [', '\n[')
oneline = oneline.replace('\\', '')
oneline = oneline.replace(')[', ')\n[')
oneline = oneline.replace('.[', '.\n[')
oneline = oneline.replace('![', '!\n[')
oneline = oneline.replace('?[', '?\n[')
oneline = oneline.replace('a[', 'a\n[')
oneline = oneline.replace('b[', 'b\n[')
oneline = oneline.replace('c[', 'c\n[')
oneline = oneline.replace('d[', 'd\n[')
oneline = oneline.replace('e[', 'e\n[')
oneline = oneline.replace('f[', 'f\n[')
oneline = oneline.replace('g[', 'g\n[')
oneline = oneline.replace('h[', 'h\n[')
oneline = oneline.replace('i[', 'i\n[')
oneline = oneline.replace('j[', 'j\n[')
oneline = oneline.replace('k[', 'k\n[')
oneline = oneline.replace('l[', 'l\n[')
oneline = oneline.replace('m[', 'm\n[')
oneline = oneline.replace('n[', 'n\n[')
oneline = oneline.replace('o[', 'o\n[')
oneline = oneline.replace('p[', 'p\n[')
oneline = oneline.replace('q[', 'q\n[')
oneline = oneline.replace('r[', 'r\n[')
oneline = oneline.replace('s[', 's\n[')
oneline = oneline.replace('t[', 't\n[')
oneline = oneline.replace('u[', 'u\n[')
oneline = oneline.replace('v[', 'v\n[')
oneline = oneline.replace('w[', 'w\n[')
oneline = oneline.replace('x[', 'x\n[')
oneline = oneline.replace('y[', 'y\n[')
oneline = oneline.replace('z[', 'z\n[')
oneline = oneline.replace('[00:00.00] {lyrics:{syncType:UNSYNCED,lines:[ ', '')
oneline = oneline.replace('[00:00.00] ', '')
oneline = oneline.replace('[00:00.0] ', '')
oneline = oneline.replace('.9]', '.90]')
oneline = oneline.replace('.8]', '.80]')
oneline = oneline.replace('.7]', '.70]')
oneline = oneline.replace('.6]', '.60]')
oneline = oneline.replace('.5]', '.50]')
oneline = oneline.replace('.4]', '.40]')
oneline = oneline.replace('.3]', '.30]')
oneline = oneline.replace('.2]', '.20]')
oneline = oneline.replace('.1]', '.10]')
oneline = oneline.replace('.0]', '.00]')

#writing final lines
with open('output.lrc', 'w', encoding='UTF-8') as file:
    file.write(oneline)
    print("Conversion complete!")

#remove leftover files
os.remove("lyricsfixed.lrc")
os.remove("lyricstimingsremoved.txt")
os.remove("timingsfixed.lrc")
os.remove("lyrics.txt")

print(downloader)
#set up variables for moving lyric and setting up cover.jpg location
host_folder = downloader.host_dir
lyrics = "Lyrics"
artist_name = downloader.artist_name
albumdir = downloader.albumdir
song = downloader.song
cover = downloader.lyrics_url
originallyricsfile = (Path(host_folder)/"output.lrc")
movedlyricsfile = (Path(albumdir)/(str(downloader.track_number) + ". " + str(song) + ".lrc"))
movedcoverjpg = (Path(albumdir)/"cover.jpg")

#prints folder where lyric went
print("\n")
print("Moved lyric to:")
print(movedlyricsfile, "\n")
newPath = shutil.move(originallyricsfile, movedlyricsfile)

def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])
        
open_file(albumdir)