import sys
import zmq

port0 = "5556"
if len(sys.argv) > 1:
    port0 = sys.argv[1]
    int(port0)

if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)

context = zmq.Context()
print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:{}".format(port0))
if len(sys.argv) > 2:
    socket.connect("tcp://localhost:{}".format(port1))

for request in range(10):
    print("Sending request {} ...".format(request))
    socket.send_string("Balance me!!!")
    # get the reply
    message = socket.recv()
    print("Received reply request {} {}".format(request, message))
    
