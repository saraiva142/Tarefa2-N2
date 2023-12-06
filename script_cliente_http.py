#import docker

#client = docker.from_env()

#Máquinas que irão rodar :
#NUM_CONTAINERS = 5

#for i in range(NUM_CONTAINERS):
    #client.containers.run('minha-imagem-dicker', detach=True)
#    try:
#        container = client.containers.run('minha-imagem-dicker', detach=True)
#        print(f"Container {i} iniciado com sucesso!")
#    except Exception as e:
#        print(f"Erro ao iniciar o container {i}: {e}")

import requests 
import time

FREQUENCIA = 1

URL = 'https://g1.globo.com/go/goias/'

while True:
    response = requests.get(URL)
    print(f'Status Code: {response.status_code}. Response Time: {response.elapsed.total_seconds}')
    time.sleep(FREQUENCIA)

