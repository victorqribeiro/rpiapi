import json


def not_found(environ, response):
	status = "404 Not Found"
	header = [("Content-Type", "application/json")]
	result = "Page not found"
	response(status, header)
	return [json.dumps(result).encode()]
