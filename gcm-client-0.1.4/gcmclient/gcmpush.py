import sys
import urllib
import urllib2


regid="APA91bHduv1fmnrEAEvED1bAh82MkTYjCWS0JB2kb_UZ7U60eL-6iifMywWmz1lz2g0tyKaBHNuE5D9My4bRGLNlnahWq7lhR_rvoU_7DHD6Q8YKHDgvAHSpl9ivDw7XAB2SpzFP53B3fRj0Bkmt9sxkHMksKL8TwA"
url = 'https://android.googleapis.com/gcm/send'
apiKey="AIzaSyAGW4D5BWfxk7kJLsyedhez-j9XQfMZdm4"
myKey = "key=" + apiKey

json_data = { "registration_id": regid, "data" : {
	"reg_id": regid,
	 "tipo": 1,
	 "mensaje":'Tienes una nueva medicion'
	        },
	    }
 ### Get regids
registration_data = {"registration_ids": [regid]}

headers = {'Content-Type': 'application/json', 'Authorization': myKey}
data = urllib.urlencode(json_data)               
req = urllib2.Request(url, data)
req.add_header("Authorization", myKey)               

f = urllib2.urlopen(req)
response = f.read()
f.close()