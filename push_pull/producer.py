import zmq

def producer():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://127.0.0.1:5557")

    for num in range(20000):
        msg = {'num': num}
        socket.send_json(msg)
        print('SEND {}'.format(msg))

producer()
