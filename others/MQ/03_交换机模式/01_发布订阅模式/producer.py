import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

#声明交换机
channel.exchange_declare(exchange="logs", #交换机名称
                         exchange_type="fanout") #交换机模式 fanout:发布订阅

#向logs交互机插入数据
message = "info : Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print(" [x] Sent %r" % message)
connection.close()

