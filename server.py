import json
import Pyro5.api

from algorithm import execute_algorithm


@Pyro5.api.expose
class MatrixProcessor(object):
    def process_input(self, random_params) -> str:
        execute_algorithm(random_params)
        return "Algorithm executed"

    """
    def average_cpu_usage_by_matrix(self):
        cpu_list_1 = []
        cpu_list_2 = []
        with open("results/report_cgne.json") as file:
            dict_data = json.load(file)
            for value in dict_data:
                if (value.get('matrix')=="1"):
                    cpu_list_1.append(value["cpu (%)"])                    
                else:                    
                    cpu_list_2.append(value["cpu (%)"])
            average_m1_cgne = sum(cpu_list_1) / len(cpu_list_1)
            average_m2_cgne = sum(cpu_list_2) / len(cpu_list_2)
        
        with open("results/report_cgnr.json") as file:
            dict_data = json.load(file)
            for value in dict_data:
                if (value.get('matrix')=="1"):                    
                    cpu_list_1.append(value["cpu (%)"])
                else:                    
                    cpu_list_2.append(value["cpu (%)"])
            average_m1_cgnr = sum(cpu_list_1) / len(cpu_list_1)
            average_m2_cgnr = sum(cpu_list_2) / len(cpu_list_2)

        result = {
            "average_cpu_m1": (average_m1_cgne+average_m1_cgnr)/2,
            "average_cpu_m2": (average_m2_cgne+average_m2_cgnr)/2,
        }
        return result
    

    def average_ram_usage_by_matrix(self):
        ram_list_1 = []
        ram_list_2 = []
        with open("results/report_cgne.json") as file:
            dict_data = json.load(file)
            for value in dict_data:
                if (value.get('matrix', "0")=="1"):                    
                    ram_list_1.append(value["ram_usage (GB)"])
                else:                    
                    ram_list_2.append(value["ram_usage (GB)"])
            average_m1_cgne = sum(ram_list_1) / len(ram_list_1)
            average_m2_cgne = sum(ram_list_2) / len(ram_list_2)
        
        with open("results/report_cgnr.json") as file:
            dict_data = json.load(file)
            for value in dict_data:
                if (value.get('matrix', "0")=="1"):                    
                    ram_list_1.append(value["ram_usage (GB)"])
                else:                    
                    ram_list_2.append(value["ram_usage (GB)"])
            average_m1_cgnr = sum(ram_list_1) / len(ram_list_1)
            average_m2_cgnr = sum(ram_list_2) / len(ram_list_2)

        result = {
            "average_ram_m1": (average_m1_cgne+average_m1_cgnr)/2,
            "average_ram_m2": (average_m2_cgne+average_m2_cgnr)/2,
        }
        return result
    """

daemon = Pyro5.api.Daemon()
uri = daemon.register(MatrixProcessor)

print("Ready. Object uri =", uri)
daemon.requestLoop()

