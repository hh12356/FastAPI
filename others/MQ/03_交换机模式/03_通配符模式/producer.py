import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

#声明交换机
channel.exchange_declare(exchange="logs3", #交换机名称
                         exchange_type="topic") #交换机模式

#向logs交互机插入数据
message = "info : Hello World!"
channel.basic_publish(exchange='logs3',
                      routing_key='usa.news',
                      body=message)

print(" [x] Sent %r" % message)
connection.close()

