##this file has been provided by SigSci - thank you! - with a few modifications


import sys, requests, os

# Initial setup
ApiHost = 'https://dashboard.signalsciences.net/api/v0'
CorpName = '<corpname>'
SiteName = '<sitename>'


def SigSciAuth():
	endpoint = 'https://dashboard.signalsciences.net/api/v0'
	email = '<useraccout_apienabled>'
	password = '<password>'

	# Authenticate

	auth = requests.post(
		endpoint + '/auth',
		data = {"email": email, "password": password}
	)

	if auth.status_code == 401:
		print 'Invalid login.'
		sys.exit()
	elif auth.status_code != 200:
		print 'Unexpected status: %s response: %s' % (auth.status_code, auth.text)
		sys.exit()

	parsed_response = auth.json()
	token = parsed_response['token']

	# Fetch list of corps

	SigHeaders = {
		'Content-type': 'application/json',
		'Authorization': 'Bearer %s' % token
	}
	#print SigHeaders
	#corps = requests.get(endpoint + '/corps', headers=headers)
	#print corps.text
	#print token

	#agents = requests.
	return SigHeaders;

SigSciAuth()
