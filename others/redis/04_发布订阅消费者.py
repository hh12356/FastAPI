import redis

r = redis.Redis(host="127.0.0.1",protocol=2)

pub = r.pubsub()

pub.subscribe("room_101")
#先取出订阅首次响应
pub.parse_response()

while 1:
    print("waiting...")
    res = pub.parse_response()
    print(res)
