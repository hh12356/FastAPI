import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

#声明交换机
channel.exchange_declare(exchange="logs2", #交换机名称
                         exchange_type="direct") #交换机模式 direct:关键字模式

#向logs交互机插入数据
message = "info : Hello World!"
channel.basic_publish(exchange='logs2',
                      routing_key='info',
                      body=message)

print(" [x] Sent %r" % message)
connection.close()

