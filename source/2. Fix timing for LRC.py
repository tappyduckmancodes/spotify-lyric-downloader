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
print(modified_string)

with open('lyricstimingsremoved.txt', 'w') as file:
    file.write(modified_string)
