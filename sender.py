import paho.mqtt.publish as publish

while True:
    msg = input("Message:")

    # connects to server, sends message and disconnects
    publish.single("testtopic", msg, hostname="localhost")
