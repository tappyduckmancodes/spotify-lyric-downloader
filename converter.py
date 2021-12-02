import os, re, sys, itertools, json, requests, base64, linecache, time, requests
import urllib.request
import lyricdownloader, shutil

host_folder = lyricdownloader.host_dir
os.chdir(host_folder)
# Read in the jumbled Spotify lyric text
with open('lyrics.txt', 'r') as file :
    filedata = file.read()

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

# Write the file out
with open('lyricsfixed.lrc', 'w') as file:
    file.write(filedata)

# remove leftover shit from Spotify that doesnt apply to lrc files
with open("lyricsfixed.lrc", "r") as f:
    lines = f.readlines() 
with open("lyricsfixed.lrc", "w") as new_f:
    for line in lines:
        if not line.startswith("colors:{background"):
            new_f.write(line)

# removes last line of gibberish
import os, sys, re
readFile = open("lyricsfixed.lrc")
lines = readFile.readlines()
readFile.close()
w = open("lyricsfixed.lrc",'w')
w.writelines([item for item in lines[:-1]])
w.close()

with open('lyricsfixed.lrc', 'r') as file :
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
with open('timings.txt', 'r') as file :
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
with open('timingsfixed.txt', 'w') as file:
    file.write(filedata)

with open('timingsfixed.txt', 'r') as file :
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

with open('timingsfixed.txt', 'w') as file:
    file.write(filedatawithlastbracket)

os.remove("timings.txt")
os.rename('timingsfixed.txt', 'timingsfixed.lrc')

with open('lyricsfixed.lrc', 'r') as file :
    filedata = file.read()
# doing what i did earlier, very janky and very backwards, to extract whats *not* in the brackets to get the words to apply the new times to
test_str = filedata
a_string = test_str
modified_string = re.sub(r"\[\s*\+?(-?\d+)\s*\]", "", a_string)
print(modified_string)

with open('lyricstimingsremoved.txt', 'w') as file:
    file.write(modified_string)

from itertools import zip_longest
with open('timingsfixed.lrc', 'r') as file :
    filedata = file.read()
with open('lyricstimingsremoved.txt', 'r') as file1:
    test_str = file1.read()
#combines new timing and lyric files, A/B/A/B style, no AA/BB
with open('timingsfixed.lrc', 'r') as src1, open('lyricstimingsremoved.txt', 'r') as src2, open('output.lrc', 'w') as dst:
    for line_from_first, line_from_second in itertools.zip_longest(src1, src2):
        if line_from_first is not None:
            dst.write(line_from_first)
        if line_from_second is not None:
            dst.write(line_from_second)

with open('output.lrc', 'r') as file :
    filedata = file.read()
filedata = filedata.replace('   ', '')
with open('output.lrc', 'w') as file:
    file.write(filedata)
#combines into one line where line breaks can be added
with open('output.lrc') as f:
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

with open('output.lrc', 'w') as file:
    file.write(oneline)
os.remove("lyricsfixed.lrc")
os.remove("lyricstimingsremoved.txt")
os.remove("timingsfixed.lrc") 
os.remove("corrected.txt")
os.remove("lyrics.txt")

host_folder = lyricdownloader.host_dir
album_folder = lyricdownloader.albumdir
song = lyricdownloader.mod_string_1
cover = lyricdownloader.cover

originallyricsfile = (host_folder + "\\output.lrc")
movedlyricsfile = (album_folder + "\\" + song + ".lrc")
movedcoverjpg = (album_folder + "\\" + "cover.jpg")

#puts folder 
print("Moved Lyric To:")
print(movedlyricsfile)
newPath = shutil.move(originallyricsfile, movedlyricsfile)

# downloads cover to folder
image_url = cover
f = open(movedcoverjpg,'wb')
f.write(urllib.request.urlopen(cover).read())
f.close()

os.chdir(album_folder)

if os.path.isfile("cover.jpg"):
    print("Cover already downloaded, skipping download")
    
else:
# downloads cover to folder
    print("No cover.jpg detected, downloading now")
    image_url = cover
    f = open(movedcoverjpg,'wb')
    f.write(urllib.request.urlopen(cover).read())
    f.close()
    print("Cover downloaded to:")
    print(movedcoverjpg)