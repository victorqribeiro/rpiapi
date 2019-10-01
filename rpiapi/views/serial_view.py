import json
import serial
from RPi import GPIO


# Add here the USB port and the Baud you want the serial to comunicate with
# ('port', baud_rate)
ports = [
	('/dev/ttyUSB0', 9600)
]

def serial_view(environ, response, parameter = None):
	
	status = "200 OK"
	
	header = [
		("Content-Type", "application/json"),
		("Cache-Control", "no-store, no-cache, must-revalidate"),
		("Expires", "0")
	]
	
	try:
	
		port, baud = ports[ int(parameter[0]) ]
	
		arduino = serial.Serial(port, baud)
		
		result = arduino.readline()
	
	except Exception as e:

		status = "400 Bad Request"

		result = "Make sure to configure port and baud on views/serial.py \n {}".format(str(e))

	response(status, header)

	return [json.dumps(result).encode()]
