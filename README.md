# TFKIT201 (Ubuntu 18.04LTS)
Conjunto de ferramentas, receitas e scripts voltado ao Tensorflow 2.0.1

## Por que não no Windows?
Nvidia-docker não dá suporte ao sistema operacional Windows. Além do Hyper-V não suportar GPU Passthrough, o docker no modo 'native' tambem não suporta.

[Leia mais aqui](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#is-microsoft-windows-supported)

[Discussão](https://github.com/NVIDIA/nvidia-docker/issues/665)

---

## Preparando o ambiente (Ubuntu 18.04LTS)

### [Configure os drivers NVidia (GPU)](GPU_nvidia_setup.md)
Comece instalando os drivers da placa de video

### [Instalando o Docker](docker_setup.md)
Adicione os repositorios oficiais DOCKER e instale a versao mais recente.

## [Instalando Nvidia-Docker](GPU_nvidia_docker_setup.md)
Adicione os repositórios de pacotes 'nvidia-docker', reinicie o serviço docker e teste um container com acesso a GPU com o 'nvidia-smi' baseado na última imagem oficial do CUDA.



