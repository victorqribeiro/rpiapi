import json
from RPi import GPIO


def read(environ, response, parameter = None):
	
	status = "200 OK"
	
	header = [
		("Content-Type", "application/json"),
		("Cache-Control", "no-store, no-cache, must-revalidate"),
		("Expires", "0")
	]
	
	try:
	
		pin = int(parameter[0])
		
		mode = GPIO.PUD_UP
		
		if len(parameter) > 1 and parameter[1] == "down" :
		
			mode = GPIO.PUD_DOWN
	
		GPIO.setup(pin, GPIO.IN, pull_up_down=mode)
		
		result = GPIO.input(pin)
	
	except Exception as e:

		status = "400 Bad Request"

		result = str(e)

	response(status, header)

	return [json.dumps(result).encode()]
