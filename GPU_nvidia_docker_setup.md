# Instalando o Nvidia-docker

## 
## Adicione os repositórios de pacotes 'nvidia-docker':
```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
```

## Instale o nvidia-docker e em seguida reinicie o serviço docker:
````
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
````

## Teste um container com acesso a GPU com o 'nvidia-smi' baseado na última imagem oficial do CUDA
````
docker run --gpus all nvidia/cuda:10.0-base nvidia-smi
````

Retorno:
````
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 410.104      Driver Version: 410.104      CUDA Version: 10.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce RTX 208...  On   | 00000000:01:00.0 Off |                  N/A |
|  0%   53C    P8    24W / 260W |  10922MiB / 10989MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+
````

[VOLTAR](README.md)
