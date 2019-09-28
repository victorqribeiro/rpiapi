import re
from views import *


routes = [
	(r'\/?$', index),
	(r'\/activate\/?([0-9]*)$', status),
	(r'\/deactivate\/?([0-9]*)$', status),
	(r'\/status\/?([0-9]*)$', status),
	(r'\/toggle\/?([0-9]*)$', status)
]

def application(environ, start_response):

	for path, app in routes: 
	
		parameter = re.match(path, environ['PATH_INFO'])
		
		if parameter:
		
			if parameter.groups():
			
				return app(environ, start_response, parameter.group(1))
				
			else:
			
				return app(environ, start_response)
				
	return not_found(environ, start_response)
