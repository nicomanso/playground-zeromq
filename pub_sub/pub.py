import random
import sys
import time
import zmq

port = 3333
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

while True:
    topic = random.randrange(1895, 1905)
    messagedata = random.randrange(1,215) - 80
    print("{} {}".format(topic, messagedata))
    socket.send_string("{} {}".format(topic, messagedata))
    time.sleep(1)
