import json
from RPi import GPIO

def index(environ, response):

	modes = {
		-1: "MODE_UNKNOWN",
		10: "BOARD",
		11: "BCM",
		40: "SERIAL",
		41: "SPI",
		42: "I2C",
		43: "PWM"
	}
	
	status = "200 OK"
	
	header = [("Content-Type", "application/json")]
	
	result = {
		"GPIO.RPI_INFO": GPIO.RPI_INFO,
		"GPIO.VERSION": GPIO.VERSION,
		"MODE": modes[ GPIO.getmode() ]
	}
	
	response(status, header)
	
	return [json.dumps(result).encode()]
