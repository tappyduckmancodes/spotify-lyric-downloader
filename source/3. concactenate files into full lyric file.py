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
