# Configure os drivers NVidia (GPU)

## Adicionar repositorios de pacote NVIDIA
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804_10.0.130-1_amd64.deb
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
sudo apt-get update
wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt install ./nvidia-machine-learning-repo-ubuntu1804_1.0.0-1_amd64.deb
sudo apt-get update
```

## Instalando NVIDIA Driver (checar capabilities 418)
```
sudo apt-get install -y --no-install-recommends nvidia-driver-418
```

Em seguida, reinicie o PC e verifique se o driver esta' funcionando com o comando `nvidia-smi`

[VOLTAR](README.md)