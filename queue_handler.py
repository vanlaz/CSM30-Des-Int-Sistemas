import multiprocessing

#consumes from queue based on CPU usage
def consumer(queue, server):
    while True:
        item = queue.get()
        print(item)
        #average_m1 = server.average_cpu_usage_by_matrix()
        #print(f'CPU usage average for matrix 1: {average_m1}')
        average_cpu = server.average_cpu_usage_by_reports()
        print (f"Uso médio de CPU: {average_cpu}(%)")
        if item is not None and ((100-10-average_cpu) > 0):
            print("Processing input...")
            print(server.process_input(item))            
            print("Processing done. Saving output files")

def handle_queue(producer, consumer, server):
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q, server))
    p1.start()
    p2.start()
    p1.join()
    p2.join()