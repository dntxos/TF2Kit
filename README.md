# TFKIT201 (Ubuntu 18.04LTS)
Conjunto de ferramentas, receitas e scripts voltado ao Tensorflow 2.0.1

## Por que não no Windows?
Nvidia-docker não suporta sistema operacional Windows. Além do Hyper-V não suportar GPU Passthrough, o docker no modo 'native' também não suporta.

[Leia mais aqui(Em inglês)](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#is-microsoft-windows-supported) / [(Traduzido automaticamente)](https://translate.google.com.br/translate?hl=pt-BR&sl=auto&tl=pt&u=https%3A%2F%2Fgithub.com%2FNVIDIA%2Fnvidia-docker%2Fwiki%2FFrequently-Asked-Questions%23is-microsoft-windows-supported)

[Discussão(Em inglês)](https://github.com/NVIDIA/nvidia-docker/issues/665) / [(Traduzido automaticamente)](https://translate.google.com/translate?sl=auto&tl=pt&u=https%3A%2F%2Fgithub.com%2FNVIDIA%2Fnvidia-docker%2Fissues%2F665)

---

## Preparando o ambiente (Ubuntu 18.04LTS)

### [Configure os drivers NVidia (GPU)](GPU_nvidia_setup.md)
Comece instalando os drivers da placa de video

### [Instalando o Docker](docker_setup.md)
Adicione os repositorios oficiais DOCKER e instale a versao mais recente.

## [Instalando Nvidia-Docker](GPU_nvidia_docker_setup.md)
Adicione os repositórios de pacotes 'nvidia-docker', instale o nvidia-docker, reinicie o serviço docker e teste um container com acesso a GPU com o 'nvidia-smi' baseado na última imagem oficial do CUDA.



