import random
import time

import Pyro5.api
import multiprocessing

def producer(queue):
    req_count = 0
    while True:
        time.sleep(random.randint(5, 10))
        req_count += 1
        queue.put(req_count)
    

def consumer(queue, matrix_processor):
    while True:
        item = queue.get()
        print(item)
        #TODO check cpu usage
        if item is not None:
            print("Processing input...")
            matrix_processor.process_input(item)            
            print("Processing done. Saving output files")


if __name__ == '__main__':
    uri = input("Insert server uri: ").strip()

    matrix_processor = Pyro5.api.Proxy(uri)

    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,matrix_processor))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
