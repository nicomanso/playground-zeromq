import random
import zmq

def consumer():
    consumer_id = random.randrange(1, 100)
    print('Consumer: {}'.format(consumer_id))
    context = zmq.Context()
    socket_pull = context.socket(zmq.PULL)
    socket_pull.connect("tcp://127.0.0.1:5557")

    socket_push = context.socket(zmq.PUSH)
    socket_push.connect("tcp://127.0.0.1:5558")

    while True:
        work = socket_pull.recv_json()
        data = work['num']
        result = {'consumer': consumer_id, 'num': data}
        print('RESULT: {}'.format(result))
        if data % 2 == 0:
            socket_push.send_json(result)
            print('SEND RESULT')

consumer()
