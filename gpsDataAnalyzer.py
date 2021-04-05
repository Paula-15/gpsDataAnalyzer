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
		print (NMEA_fields[0] + ":")
		print ("\tTime: " +  NMEA_fields[1])
		print ("\tLat: " + NMEA_fields[2] + " " + NMEA_fields[3])
		print ("\tLon: " + NMEA_fields[4] + " " + NMEA_fields[5])
		print ("\tQuality: " + NMEA_fields[6])
		print ("\tSatélites: " + NMEA_fields[7])
		print ("\tAltitud: " + NMEA_fields[9] + " " + NMEA_fields[10] + "\n")

	elif NMEA_fields[0] == "$GPGLL":
		print (NMEA_fields[0] + ":")
		print ("\tLat: " + NMEA_fields[1] + " " + NMEA_fields[2])
		print ("\tLon: " + NMEA_fields[3] + " " + NMEA_fields[4])
		print ("\tTime: " + NMEA_fields[5])
		print ("\t" + NMEA_fields[6])

	elif NMEA_fields[0] == "$GPRMC":
		print (NMEA_fields[0] + ":")
		print ("\tTime: " + NMEA_fields[1])
		print ("\tStatus: " + NMEA_fields[2])
		print ("\tLat: " + NMEA_fields[3])
		print ("\tLon: " + NMEA_fields[5])
		print ("\tSpeed: " + NMEA_fields[7] + " knots")
		print ("\tDate: " + NMEA_fields[9])

	elif NMEA_fields[0] == "$GPGSA"

	else:
		print (NMEA_fields[0])

	'''
	value = line.split(',')
	if value[1] is "$GPGGA":
		print ("Time: %s" % value[2])
		print ("Lat: %s" % value[3])
		print (value[4])
		print ("Lon: %s" % value[5])
		print (value[6])
		print ("Quality: %s" % value[7])
		print ("Satélites: %s" % value[8])
		print ("HDOP: %s" % value[9])
		print ("Altitud: %s" % value[10])
		print (value[11])
		print ("Geoidal separation: %s" % value[12])
		print (value[13])
		print ("Age of correction: %s" % value[14])
		print ("Correction station ID: %s" % value[15])
		print ("Checksum: %s" % value[16])
	else:
		print (value[1])
	'''



with open(filename) as f:
        content = f.readlines()

for line in content:
        if is_valid_NMEA_command(line):
                parse_NMEA_line(line)

