import zmq
import time

port = 3333
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

count = 0
while True:
    msg = socket.recv()
    print(msg)
    socket.send_string("{} Your peer reporting".format(count))
    count += 1
    time.sleep(5)
