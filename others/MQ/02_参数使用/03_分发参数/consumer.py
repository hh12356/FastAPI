import pika

#连接rabbitmq并获取频道
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

#创建队列(两边都创建，保证队列存在)
channel.queue_declare(queue="hello4",durable=True)

#设置回调函数
def callback( ch, method, properties, body):
    import time
    time.sleep(3)
    print(" [x] Received %r" % body)
    channel.basic_ack(delivery_tag=method.delivery_tag)

#公平分发
channel.basic_qos(prefetch_count=1)

#确定监听队列
channel.basic_consume(queue="hello4",
                      auto_ack=False, #默认应答改为手动应答
                      on_message_callback=callback)

print(" [*] waiting for messages. To exit press CTRL+C")
#运行监听队列
channel.start_consuming()
