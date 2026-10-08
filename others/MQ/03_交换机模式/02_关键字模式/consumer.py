import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

#声明交换机(两边都声明以保证其存在)
channel.exchange_declare(exchange="logs2", #交换机名称
                         exchange_type="direct") #交换机模式 direct:关键字模式

#创建队列(由消费者自己创建)
result = channel.queue_declare("",exclusive=True) #exclusive=True 随机创建名字
queue_name = result.method.queue

#将队列绑定交换机
channel.queue_bind(exchange='logs2',
                   queue=queue_name,
                   routing_key="error" #绑定关键字(绑定多个需重复写)
                   )

channel.queue_bind(exchange='logs2',
                   queue=queue_name,
                   routing_key="info"
                   )

channel.queue_bind(exchange='logs2',
                   queue=queue_name,
                   routing_key="warning"
                   )

#设置回调函数
def callback( ch, method, properties, body):
    print(" [x] Received %r" % body)

#确定监听队列
channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)

print(" [*] waiting for messages. To exit press CTRL+C")
channel.start_consuming()
