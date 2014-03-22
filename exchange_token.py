import requests

p = {
	'client_id': 'client_id',
	'client_secret': 'client_secret',
	'code': 'code',
	'redirect_uri': 'redirect_uri'
}

r = requests.post("http://join.agiliq.com/oauth/access_token/", params=p)
