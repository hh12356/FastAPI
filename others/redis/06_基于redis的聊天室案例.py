import redis
import threading

r = redis.Redis(host="127.0.0.1",protocol=2)

def send_msg():
    msg = input(">>>")
    r.publish("room_101",msg)

def recv_msg():
    pub = r.pubsub()

    pub.subscribe("room_101")
    pub.parse_response()

    while 1:
        res_msg = pub.parse_response()
        print(">>>",res_msg)

t = threading.Thread(target=send_msg)
t.start()

recv_msg()