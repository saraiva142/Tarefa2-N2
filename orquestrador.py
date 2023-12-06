# ORQUESTRADOR
import docker
client = docker.from_env()

#Máquinas que irão rodar :
NUM_CONTAINERS = 5

for i in range(NUM_CONTAINERS):
    client.containers.run('teste', detach=True)