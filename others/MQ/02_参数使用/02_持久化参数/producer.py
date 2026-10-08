import pika

#连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
#获取频道
channel = connection.channel()

#创建可持久化队列
channel.queue_declare(queue="hello3",durable=True)

#向指定队列插入数据
channel.basic_publish(exchange='', #简单模式交换机参数为空
                      routing_key="hello3", #指定队列
                      body="Hello World!",
                      properties=pika.BasicProperties(
                          delivery_mode=2 #数据持久化
                      )
                      )

print(" [x] Sent 'Hello World!'")

