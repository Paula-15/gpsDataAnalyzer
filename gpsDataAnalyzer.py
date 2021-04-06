#!/usr/bin/python3

#File to read from
filename = "unreadableData.txt"
#File to write to
outputLog = open ('readableData.txt', 'a')

def is_valid_NMEA_command(line):
        return line[:3] == "$GP"

def parse_NMEA_line (line):
	NMEA_data = line.split('*')
	NMEA_fields = NMEA_data[0].split(',')

	if NMEA_fields[0] == "$GPGGA":
		outputLog.write(NMEA_fields[0] + ":\n")
		outputLog.write ("\tTime: " +  NMEA_fields[1] + "\n")
		outputLog.write ("\tLat: " + NMEA_fields[2] + " " + NMEA_fields[3] + "\n")
		outputLog.write ("\tLon: " + NMEA_fields[4] + " " + NMEA_fields[5] + "\n")
		outputLog.write ("\tQuality: " + NMEA_fields[6] + "\n")
		outputLog.write ("\tSatélites: " + NMEA_fields[7] + "\n")
		outputLog.write ("\tAltitud: " + NMEA_fields[9] + " " + NMEA_fields[10] + "\n")

	elif NMEA_fields[0] == "$GPGLL":
		outputLog.write (NMEA_fields[0] + ":\n")
		outputLog.write ("\tLat: " + NMEA_fields[1] + " " + NMEA_fields[2] + "\n")
		outputLog.write ("\tLon: " + NMEA_fields[3] + " " + NMEA_fields[4] + "\n")
		outputLog.write ("\tTime: " + NMEA_fields[5] + "\n")
		outputLog.write ("\t" + NMEA_fields[6] + "\n")

	elif NMEA_fields[0] == "$GPRMC":
		outputLog.write (NMEA_fields[0] + ":\n")
		outputLog.write ("\tTime: " + NMEA_fields[1] + "\n")
		outputLog.write ("\tStatus: " + NMEA_fields[2] + "\n")
		outputLog.write ("\tLat: " + NMEA_fields[3] + "\n")
		outputLog.write ("\tLon: " + NMEA_fields[5] + "\n")
		outputLog.write ("\tSpeed: " + NMEA_fields[7] + " knots\n")
		outputLog.write ("\tDate: " + NMEA_fields[9] + "\n")

	elif NMEA_fields[0] == "$GPGSA":
		outputLog.write (NMEA_fields[0] + ":\n")
		outputLog.write ("\tFix type: " + NMEA_fields[2] + "\n")

	elif NMEA_fields[0] == "$GPGSV":
		outputLog.write (NMEA_fields[0] + ":\n")
		outputLog.write ("\tMessage " + NMEA_fields[2] + "\n")

	elif NMEA_fields[0] == "$GPVTG":
		outputLog.write (NMEA_fields[0] + "\n")


	else:
		print (NMEA_fields[0])





#lineCount = 1

with open(filename) as f:
        content = f.readlines()

for line in content:
#	print(lineCount)
#	lineCount += 1
	if is_valid_NMEA_command(line):
		parse_NMEA_line(line)
