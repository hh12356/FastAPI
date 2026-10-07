import redis

r = redis.Redis(host="127.0.0.1",protocol=2)

r.publish("room_101","Hello Miles")
