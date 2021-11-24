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
