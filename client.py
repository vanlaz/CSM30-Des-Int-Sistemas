import random
import time

import Pyro5.api

uri = input("Insert server uri: ").strip()

matrix_processor = Pyro5.api.Proxy(uri)


def process_by_random():
    while True:
        time.sleep(random.randint(8, 15))
        print("Processing input...")
        matrix_processor.process_input()
        print("Processing done. Saving output files")


process_by_random()
