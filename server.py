import json
import Pyro5.api

from algorithm import execute_algorithm


@Pyro5.api.expose
class MatrixProcessor(object):
    def process_input(self, random_params) -> str:
        execute_algorithm(random_params)
        return "Algotithm executed"


    def average_cpu_usage_by_reports(self):
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


daemon = Pyro5.api.Daemon()
uri = daemon.register(MatrixProcessor)

print("Ready. Object uri =", uri)
daemon.requestLoop()

