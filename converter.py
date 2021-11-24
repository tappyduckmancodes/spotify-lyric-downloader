# Read in the file
with open('lyrics.txt', 'r') as file :
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('},', '} \n')
filedata = filedata.replace('{"lyrics":{"syncType":"LINE_SYNCED","lines":[', '')
filedata = filedata.replace('\\u0027', '\'')
filedata = filedata.replace('{"startTimeMs":"', '[')
filedata = filedata.replace(',"syllables":[]} ', '')
filedata = filedata.replace('","words":', ']')
filedata = filedata.replace('"', '')
filedata = filedata.replace('hasVocalRemoval:false}', '')
filedata = filedata.replace(']', '] ')

# Write the file out again
with open('lyricsfixed.lrc', 'w') as file:
    file.write(filedata)

# remove leftover shit from spotify that doesnt apply to lrc files
with open("lyricsfixed.lrc", "r") as f:
    lines = f.readlines() 
with open("lyricsfixed.lrc", "w") as new_f:
    for line in lines:
        if not line.startswith("colors:{background"):
            new_f.write(line)

# remove last line 
import os, sys, re
readFile = open("lyricsfixed.lrc")
lines = readFile.readlines()
readFile.close()
w = open("lyricsfixed.lrc",'w')
w.writelines([item for item in lines[:-1]])
w.close()

import os, re
with open('lyricsfixed.lrc', 'r') as file :
    filedata = file.read()
# initializing string
test_str = filedata

# Extract Numbers in Brackets in String
# Using regex
res = re.findall(r"\[\s*\+?(-?\d+)\s*\]", test_str)
# saving to timings.txt
file = open("timings.txt", "w")


corrected_times = []
for time in res:
  corrected_times.append((int(time)) / 1000)

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

# Replace the target string
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

s1 = filedata
s2 = "]"
filedatawithlastbracket = (s1 + s2)

with open('timingsfixed.txt', 'w') as file:
    file.write(filedatawithlastbracket)

os.remove("timings.txt")
os.rename('timingsfixed.txt', 'timingsfixed.lrc')

with open('lyricsfixed.lrc', 'r') as file :
    filedata = file.read()
# initializing string
test_str = filedata
a_string = test_str
modified_string = re.sub(r"\[\s*\+?(-?\d+)\s*\]", "", a_string)
#print(modified_string) should be just song lyrics no timecodes

with open('lyricstimingsremoved.txt', 'w') as file:
    file.write(modified_string)

import os, re, itertools
from itertools import zip_longest
with open('timingsfixed.lrc', 'r') as file :
    filedata = file.read()
with open('lyricstimingsremoved.txt', 'r') as file1:
    test_str = file1.read()

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

with open('output.lrc') as f:
    all_lines = f.readlines()
    all_lines = [x.strip() for x in all_lines if x.strip()]
    two_lines = " ".join(x for x in all_lines[:2])
    lines_left = " ".join(x for x in all_lines[2:])

oneline = (two_lines + lines_left)

print(oneline)

# Replace the target string
oneline = oneline.replace(' [', '\n[')
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

with open('output.lrc', 'w') as file:
    file.write(oneline)
os.remove("lyrics.txt")
os.remove("lyricsfixed.lrc")
os.remove("lyricstimingsremoved.txt")
os.remove("timingsfixed.lrc") 
os.remove("timingsfixed.txt")

with open('lyrics.txt', 'w') as file:
    file.write("Lyrics go here")
