#!/usr/bin/python3

#File from where to read
filename = "data.txt"
#File to write to
outputLog = open ('unreadData2.txt', 'a')

with open(filename) as f:
	content = f.readlines()

for line in content:
	data = line[1:-6]
	outputLog.write(data + "\n")
outputLog.flush()
