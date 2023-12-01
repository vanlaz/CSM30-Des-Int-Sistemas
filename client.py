import random
import time
import json
import Pyro5.api
import multiprocessing

#sends new matrix to queue every second
def producer(queue):
    req_count = 0
    while True:
        #time.sleep(random.randint(0, 1))
        req_count += 1
        queue.put(req_count)

 #gets average value for CPU usage from the reports   
def average_cpu_usage_by_reports():
    with open("results/report_cgne.json") as file:
        dict_data = json.load(file)
        for value in dict_data:
            cpu_list = []
            cpu_list.append(value["cpu"])
        average = sum(cpu_list) / len(cpu_list)
    
    with open("results/report_cgnr.json") as file:
        dict_data = json.load(file)
        for value in dict_data:
            cpu_list = []
            cpu_list.append(value["cpu"])
        average_cgnr = sum(cpu_list) / len(cpu_list)

    return (average+average_cgnr)/2

#consumes from queue based on CPU usage
def consumer(queue, matrix_processor):
    while True:
        item = queue.get()
        print(item)
        average_cpu = average_cpu_usage_by_reports()
        print (f"Uso médio de CPU: {average_cpu}(%)")
        if item is not None and ((100-10-average_cpu) > 0):
            print("Processing input...")
            print(matrix_processor.process_input(item))            
            print("Processing done. Saving output files")


if __name__ == '__main__':
    uri = input("Insert server uri: ").strip()

    #calls server function to process the matrix
    matrix_processor = Pyro5.api.Proxy(uri)

    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,matrix_processor))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
