import re
from views import *
from RPi import GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

routes = [
	(r'\/?$', index),
	(r'\/activate\/?([0-9]*)$', activate),
	(r'\/deactivate\/?([0-9]*)$', deactivate),
	(r'\/mode\/?([0-9]*)$', mode),
	(r'\/read\/?([0-9]*)\/?(up|down)?$', read),
	(r'\/serial\/?([0-9]*)$', serial_view),
	(r'\/toggle\/?([0-9]*)$', toggle),
	(r'\/network\/?$', network)
]

def application(environ, start_response):

	for path, app in routes: 
	
		parameter = re.match(path, environ['PATH_INFO'])
		
		if parameter:
		
			if parameter.groups():
			
				return app(environ, start_response, parameter.groups())
				
			else:
			
				return app(environ, start_response)
				
	return not_found(environ, start_response)
