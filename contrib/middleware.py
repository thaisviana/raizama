import time
import math

import requests
from django.db import connections


class PerfMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response
        self.log_entry = None

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        response = self.process_response(request, response)
        return response

    def process_request(self, request):
        self.start_time = time.time()

    def process_response(self, request, response):
        elapsed_time = math.floor((time.time() - self.start_time) * 1000)

        data = {
            "start_time": self.start_time,
            "elapsed_time": elapsed_time,
            "method": request.method,
            "path": request.path,
            "queries": []
        }

        for c in connections.all():
            for q in c.queries:
                data['queries'].append(q)

        # if self.log_entry is not None:
        #     requests.patch('https://127.0.0.1:8001/log/' + self.log_entry + '/', data)
        # else:
        #     requests.post('https://127.0.0.1:8001/log/', data)
        print(data)

        return response

    def process_exception(self, request, exception):
        import traceback
        elapsed_time = math.floor((time.time() - self.start_time) * 1000)
        data = {
            "start_time": self.start_time,
            "elapsed_time": elapsed_time,
            "method": request.method,
            "path": request.path,
            "exception": str(exception),
            "traceback": traceback.format_exc()
        }

        # requests.post('https://127.0.0.1:8001/log/', data)
        self.log_entry = 1

        print('exception ocorreu', data)
