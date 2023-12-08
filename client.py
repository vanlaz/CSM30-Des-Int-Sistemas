import random
import Pyro5.api
import time

from queue_handler import consumer, handle_queue


def random_params_to_execute(req_count):
    algorithms = ['cgne', 'cgnr']
    algorithm = random.choice(algorithms)

    matrices = ['1', '2']
    matrix_type = random.choice(matrices)

    signals = ['G-1', 'G-2', 'G-3']
    signal_type = random.choice(signals)

    users = ['user a', 'user b', 'user c']
    user = random.choice(users)

    random_params = {
        "algorithm": algorithm,
        "matrix_type": matrix_type,
        "signal_type": signal_type,
        "user": user,
        "req_count": req_count
    }

    return random_params

#sends new matrix to queue
def producer(queue):
    req_count = 0
    while True:
        random_params = random_params_to_execute(req_count)
        req_count += 1
        queue.put(random_params)

if __name__ == '__main__':
    uri = input("Insert server uri: ").strip()

    #calls server function to process the matrix
    server = Pyro5.api.Proxy(uri)

    handle_queue(producer, consumer, server)