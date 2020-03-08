# TFKIT201 (Ubuntu 18.04LTS)
Conjunto de ferramentas, receitas e scripts voltado ao Tensorflow 2.0.1

---

## Preparando o ambiente (Ubuntu 18.04LTS)

### [Máquinas-virtuais com acesso a GPU é possível com VmWare ESXi (Somente para configurações com VM e GPU)](GPU_vmware_passthrough.md)
Habilite o Passthrough no ESXi, adicione o dispositivo PCIe na sua VM e desabilite o parâmetro 'Hypervisor.CPUID.v0'.

### [Configure os drivers NVidia (Somente para configurações com GPU)](GPU_nvidia_setup.md)
Comece instalando os drivers da placa de video

### [Instalando o Docker](docker_setup.md)
Adicione os repositorios oficiais DOCKER e instale a versao mais recente.

### [Instalando Nvidia-Docker (Somente para configurações com GPU)](GPU_nvidia_docker_setup.md)
Adicione os repositórios de pacotes 'nvidia-docker', instale o nvidia-docker, reinicie o serviço docker e teste um container com acesso a GPU com o 'nvidia-smi' baseado na última imagem oficial do CUDA.

>## Não há suporte para GPUs do nvidia-docker para Windows
>Esses scripts são baseados no docker e atualmente Nvidia-docker não suporta sistema operacional Windows. Além do Hyper-V não suportar GPU Passthrough, o docker no modo 'native' também não suporta.
>
>[Leia mais aqui(Em inglês)](https://github.com/NVIDIA/nvidia-docker/wiki/Frequently-Asked-Questions#is-microsoft-windows-supported) / [(Traduzido automaticamente)](https://translate.google.com.br/translate?hl=pt-BR&sl=auto&tl=pt&u=https%3A%2F%2Fgithub.com%2FNVIDIA%2Fnvidia-docker%2Fwiki%2FFrequently-Asked-Questions%23is-microsoft-windows-supported)
>
>[Discussão(Em inglês)](https://github.com/NVIDIA/nvidia-docker/issues/665) / [(Traduzido automaticamente)](https://translate.google.com/translate?sl=auto&tl=pt&u=https%3A%2F%2Fgithub.com%2FNVIDIA%2Fnvidia-docker%2Fissues%2F665)

## Utilizando containers oficiais do Tensorflow 2.0.1
O projeto TensorFlow possui imagens oficiais no DockerHub já configuradas para executar o Tensorflow. Um container docker roda em um ambiente virtual e é a maneira mais fácil de configurar suporte a GPU, já que todo o conjunto de bibliotecas (Cuda, Cudnn, TensorRT, etc) vem instaladas e configuradas na imagem pública.

### [Docker - Tensorflow 2.0.1 Cheats (Somente para configurações com GPU)](GPU_docker_tensorflow_cheats.md)
### [Docker - Tensorflow 2.0.1 Cheats (Somente para configurações com CPU)](CPU_docker_tensorflow_cheats.md)

> Utilize 'Tensorflow 2.0.1 Cheats' acima para iniciar seus containeres de acordo com suas necessidades.


