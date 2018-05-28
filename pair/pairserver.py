import zmq
import time

port = "3333"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

count = 0
while True:
    socket.send_string("Send info to my peer {}".format(count))
    count += 1
    msg = socket.recv()
    print(msg)
    time.sleep(5)
