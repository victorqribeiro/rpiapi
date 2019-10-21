import json
import requests
import socket
from uuid import getnode as get_mac

def network(environ, response, parameter=None):
	status = "200 OK"
	
	header = [
		("Content-Type", "application/json"),
		("Cache-Control", "no-store, no-cache, must-revalidate"),
		("Expires", "0")
	]

	result = {
		"hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "ipv4": requests.get('https://api.ipify.org').text,
        "ipv6": requests.get('https://api6.ipify.org').text,
        "mac_address": get_mac()
	}

	response(status, header)
	return [json.dumps(result).encode()]
