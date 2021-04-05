#!/usr/bin/python3

filename = "data2.txt"
outputLog = open ('unreadData2.txt', 'a')

with open(filename) as f:
	content = f.readlines()

for line in content:
	data = line[1:-6]
	outputLog.write(data + "\n")
outputLog.flush()
