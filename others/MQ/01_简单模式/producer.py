import pika

#连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
#获取频道
channel = connection.channel()

#创建队列
channel.queue_declare(queue="hello")

#向指定队列插入数据
channel.basic_publish(exchange='', #简单模式交换机参数为空
                      routing_key="hello", #指定队列
                      body="Hello World!")

print(" [x] Sent 'Hello World!'")

