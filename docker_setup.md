# Instalando Docker-CE em Ubuntu 18.04(LTS)

## Desinstalando versoes antigas:
```
$ sudo apt-get remove docker docker-engine docker.io containerd runc
```

## Adicionar o repositorio Docker

Antes de qualquer coisa, atualize o apt-get:
```
$ sudo apt-get update
```

Instale os pacotes para que o apt aceite repositorios sobre HTTPS:
```
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```

Adiciona a chave GPG oficial do Docker:
```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Adicione o repositorio oficial Docker X86_64/amd64:
```
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

Atualize o apt-get novamente:
```
$ sudo apt-get update
```

Instale a ultima versao do Docker:
```
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```