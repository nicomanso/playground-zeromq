import pprint
import zmq

def collect():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.bind("tcp://127.0.0.1:5558")

    collected_data = {}
    for x in range(1000):
        result = socket.recv_json()
        if collected_data.get(result['consumer'], None):
            collected_data[result['consumer']] = collected_data[result['consumer']] + 1
        else:
            collected_data[result['consumer']] = 1

    pprint.pprint(collected_data)

collect()
