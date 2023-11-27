import Pyro5.api

from algorithm import execute_algorithm


@Pyro5.api.expose
class MatrixProcessor(object):
    def process_input(self, req_count):
        execute_algorithm(req_count)
         

daemon = Pyro5.api.Daemon()
uri = daemon.register(MatrixProcessor)

print("Ready. Object uri =", uri)
daemon.requestLoop()
