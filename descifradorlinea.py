import pynmea2
from time import sleep
#file = "/home/samu/Documents/pruebagps/prueba.txt"
'''
outputLog = open ('dato1.txt', 'a+')
with open(file) as f:
    separar = f.readlines()
for line in separar:
    data = line.split('*')
    StrA = "".join(data)
    content = StrA
for line in content:
    data2 = line[1:-6]
    outputLog.write(data2 + "\n")
outputLog.flush()
#sleep(5)
#filename = "c:/Users/Samu/Documents/CanSat2021/gpsDataAnalyzer\datos1.txt"
#outputlog = open ('datos_preparados.txt', 'a')
 
#with open(filename) as f:
 #   content = f.readlines()
#for line in content:
 #   data2 = line[1:-6]
  #  outputlog.write(data2 + "\n")
#outputlog.flush()
sleep(4)
'''
#filename = open('/home/samu/Documents/pruebagps/prueba.txt', encoding='utf-8')
filename = open('gpsData.txt')
salida = open ('decode.txt', 'w+')
for line in filename.readlines():
	msg = pynmea2.parse(line)
	salida.write(repr(msg))
	salida.write(str(msg.latitude))
	salida.write(str(msg.longitude))


salida.flush()
'''
filedef = open('/home/samu/Documents/pruebagps/decode.txt')
salidadef = open ('decodedef.txt', 'w+')
while True:
	defi = line.split(',')
	1tiempo = defi[0].split('(')
	2latitud = defi[1].split('=')
	3latitud_direccion = defi[2]('=')
	4longitud = defi[3]('=')
	5longitud_direcion = defi[4]('=')
	6calidadgps = defi[5]('=')
	7numerosatelites = defi[6]('=')
	8horizontal_dil = defi[7]('=')
	9altitud_en_m = defi[8]('=')
	10geo_sep_en_m = defi[10]('=')
	tiempo =  1tiempo[2]
	latitudx = 2latitud[1]
	latitud_direccion = 3latitud_direccion[1]
	longitudx = 4longitud[1]
	longitud_direccion = 5longitud_direccion[1]
	calidadgps = 6calidadgps[1]
	numerosatelites = 7numerosatelites[1]
	horizontal_dil = 8horizontal_dil[1]
	altitud_en_m = 9altitud_en_m[1]
	geo_sep_en_m = 10geo_sep_en_m[1]
'''	
	 
	
	

	
	
	
	

