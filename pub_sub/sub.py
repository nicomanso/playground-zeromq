import zmq

port0 = 3333
port1 = 3334

context = zmq.Context()
socket = context.socket(zmq.SUB)
print("Collecting updates...")
socket.connect("tcp://localhost:{}".format(port0))
socket.connect("tcp://localhost:{}".format(port1))

# Filter msg by CP LaPlata 1900
topic_filter = "1900"
socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

total = 0

for update_nbr in range(5):
    string = socket.recv()
    topic, messagedata = string.split()
    total += int(messagedata)
    print("{} {}".format(topic, messagedata))

print("Average messagedata value for topic {} was {}".format(topic_filter, total / update_nbr))
