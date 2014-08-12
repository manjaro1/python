import sys
import urllib
import urllib2

def enviopush(json_data):

	url = 'https://android.googleapis.com/gcm/send'
	apiKey="AIzaSyAGW4D5BWfxk7kJLsyedhez-j9XQfMZdm4"
	myKey = "key=" + apiKey

	json_data =json_data
	
	headers = {'Content-Type': 'application/json', 'Authorization': myKey}
	data = urllib.urlencode(json_data)               
	req = urllib2.Request(url, data)
	req.add_header("Authorization", myKey)               

	f = urllib2.urlopen(req)
	response = f.read()
	f.close()