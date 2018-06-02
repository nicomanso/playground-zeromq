import sys
import time
import zmq

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:{}".format(port))

while True:
    message = socket.recv()
    print("Receive request: {}".format(message))
    time.sleep(1)
    socket.send_string("Word from {}".format(port))
