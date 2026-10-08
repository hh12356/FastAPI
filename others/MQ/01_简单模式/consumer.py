import pika

#连接rabbitmq并获取频道
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

#创建队列(两边都创建，保证队列存在)
channel.queue_declare(queue="hello")

#设置回调函数
def callback( ch, method, properties, body):
    print(" [x] Received %r" % body)

#确定监听队列
channel.basic_consume(queue="hello",
                      auto_ack=True, #默认应答
                      on_message_callback=callback)

print(" [*] waiting for messages. To exit press CTRL+C")
#运行监听队列
channel.start_consuming()
