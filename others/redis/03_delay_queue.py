import redis
import uuid
import time
import threading

#decode_responses=True 自动将返回字符串解码成str字符串
pool = redis.ConnectionPool(host="127.0.0.1",port=6379,db=3,decode_responses=True,protocol=2)
r = redis.Redis(connection_pool=pool)

def delayTask(name, task_time):
    #生成随机字符串
    task_id = str(uuid.uuid4())

    processTime = time.time() + task_time
    r.zadd("delay_queue",{name+task_id:processTime})

def loop():
    while 1:
        task_list = r.zrangebyscore("delay_queue",0,time.time())
        if not task_list:
            print("cost 1s")
            time.sleep(1)
            continue

        for task in task_list:
            #添加并发锁
            ok = r.zrem("delay_queue",task)
            if ok:
                print(f"执行{task}完毕")

t = threading.Thread(target=loop)
t.start()

delayTask("1",5)
delayTask("2",2)
delayTask("3",8)
delayTask("4",1)
