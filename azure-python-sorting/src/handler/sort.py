import json
import azure.functions as func
from random import randint
import time

class Sorter:
    def __init__(self):
        initialize_time = time.time()
        self.__list = [randint(0, 1000) for _ in range(1000000)]
        self.__init_time = time.time()-initialize_time

    def sort(self):
        start_time = time.time()
        sorted(self.__list)
        end_time = time.time()

        return {
            "sortTime": end_time - start_time,
            "initTime": self.__init_time
        }

def main(req: func.HttpRequest) -> func.HttpResponse:
    sorter = Sorter()
    times = sorter.sort()

    return func.HttpResponse(json.dumps(times))
