# TF2Kit (Ubuntu 18.04LTS)
Conjunto de ferramentas, receitas e scripts voltado ao Tensorflow 2.0.1

## Por que nao Windows?
Nvidia-docker nao suporta o sistema operacional Windows. Alem do Hyper-V nao suportar GPU Passthrough, o docker no modo native tambem nao suporta.
[Leia mais aqui](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#is-microsoft-windows-supported)
[Discussao](https://github.com/NVIDIA/nvidia-docker/issues/665)

## Preparando o ambiente (Ubuntu 18.04LTS)

### [Configure os drivers NVidia (GPU)](GPU_nvidia_setup.md)
Comece instalando os drivers da placa de video

### [Instalando o Docker](docker_setup.md)
Adicione os repositorios oficiais DOCKER e instale a versao mais recente.

## [Instalando Nvidia-Docker]

