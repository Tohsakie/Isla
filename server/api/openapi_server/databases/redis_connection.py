import redis

def init():
	r = redis.Redis(host='localhost', port=6379, decode_responses=True)


def write(key, value):
	r.set(key, value)


def read(key):
	return r.get(key)