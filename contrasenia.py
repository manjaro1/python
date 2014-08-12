import hmac,hashlib

def encript(val):
	return hmac.new('fleetelligent', val, hashlib.md5).hexdigest()