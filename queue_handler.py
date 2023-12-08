import multiprocessing
import psutil

#consumes from queue based on CPU usage
def consumer(queue, server):
    #ram_available = 0
    cpu_available = 0

    while True:
        random_params = queue.get()
        print(random_params)

        #cpu_data_by_matrix = server.average_cpu_usage_by_matrix()
        #ram_data_by_matrix = server.average_ram_usage_by_matrix()

        matrix_type = random_params["matrix_type"]

        average_cpu_m1 = (17.40+17.75)/2
        average_cpu_m2 = (13.20+12.25)/2

        average_ram_m1 = (12.83+14.10)/2
        average_ram_m2 = (9.79+12+43)/2

        #ram_available = round(psutil.virtual_memory().free / (1024.0 ** 3), 2)
        cpu_available = 100 - psutil.cpu_percent(interval=3)    

        if matrix_type == "1":
            if cpu_and_ram_available(cpu_available, average_cpu_m1, average_ram_m1):
                print("Processing input from matrix 1...")
                print(server.process_input(random_params))            
                print("Processing matrix 1 done. Saving output files")
        else:
            if cpu_and_ram_available(cpu_available, average_cpu_m2, average_ram_m2):
                print("Processing input from matrix 2...")
                print(server.process_input(random_params))            
                print("Processing matrix 2 done. Saving output files")

def cpu_and_ram_available(cpu_available, average_cpu, average_ram):
    print(f' cpu available: {cpu_available}')
    print(f' average_cpu usage: {average_cpu}')
    print(f' average_ram usage: {average_ram}')

    resources_are_available = (average_cpu + 10) < cpu_available and average_ram < 16
    print(f'Resources available: {resources_are_available}')

    return resources_are_available

def handle_queue(producer, consumer, server):
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q, server))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
