#!/usr/bin/python3

#File from where to read
filename = "data.txt"
#File to write to
outputLog = open ('unreadableData.txt', 'a')

with open(filename) as f:
	content = f.readlines()

for line in content:
	data = line[1:-6]
	outputLog.write(data + "\n")
outputLog.flush()
