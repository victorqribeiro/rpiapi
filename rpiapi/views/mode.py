import json
from RPi import GPIO


def mode(environ, response, parameter = None):

	pin_modes = {
		1: "GPIO.IN", 
		0: "GPIO.OUT", 
		41: "GPIO.SPI", 
		42: "GPIO.I2C", 
		43: "GPIO.HARD_PWM", 
		40: "GPIO.SERIAL", 
		-1: "GPIO.UNKNOWN"
	}
	
	status = "200 OK"
	
	header = [
		("Content-Type", "application/json"),
		("Cache-Control", "no-store, no-cache, must-revalidate"),
		("Expires", "0")
	]
	
	try:
	
		result = pin_modes[ GPIO.gpio_function(int(parameter[0])) ]
	
	except Exception as e:

		status = "400 Bad Request"

		result = str(e)

	response(status, header)

	return [json.dumps(result).encode()]
