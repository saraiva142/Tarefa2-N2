import requests
import time

FREQUENCIA = 1

URL = 'http://127.0.0.1:3000'

while True:
    response = request.get(URL)
    print(f'Status Code: {response.status_code}. Response Time: {response.elapsed.total_seconds()}')
    time.sleep(FREQUENCIA)
