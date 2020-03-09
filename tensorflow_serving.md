![IMG](images/tfx-hero.svg)
# TFX/Tensorflow Serving

## Introdução
O TensorFlow Serving é um sistema servidor flexível e de alto desempenho para modelos de aprendizado de máquina, 
projetado para ambientes de produção. O TensorFlow Serving facilita a implantação de novos algoritmos e experimentos, 
mantendo a mesma arquitetura de servidor e APIs. 
O TensorFlow Serving fornece integração imediata com os modelos TensorFlow, mas pode ser facilmente estendido 
para atender outros tipos de modelos e dados.

## Instalando o ModelServer

A maneira mais fácil e direta de usar o TensorFlow Serving é com imagens do Docker. É altamente recomendável essa rota, a menos que você tenha necessidades específicas que não são atendidas executando em um contêiner.

> DICA: Essa também é a maneira mais fácil de obter o TensorFlow Serving trabalhando com suporte a GPU.

### Utilizando imagens públicas do TensorflowServing no DockerHub

O comando abaixo carrega uma imagem pública preparada para utilizar GPU:
```
sudo docker run --gpus all -p 8501:8501 -v /localpath/to/models_folder:/models/flowers -e MODEL_NAME=flowers -it tensorflow/serving:latest-gpu bash
```

O comando abaixo carrega uma imagem pública para 'somente CPU':
```
sudo docker run -p 8501:8501 -v /localpath/to/models_folder:/models/flowers -e MODEL_NAME=flowers -it tensorflow/serving:latest bash
```

---

## Compilando uma versão otimizada para o hardware empregado
Para aproveitar o máximo possível dos recursos disponíveis na máquina, é recomendado compilar o software otimizando para utilizar instruções específicas da sua plataforma (como SSE4 e AVX).
A abordagem recomendada para compilar a partir dos 'fontes' é utilizando o Docker. As imagens de desenvolvimento do TensorFlow Serving Docker encapsulam todas as dependências necessárias para criar sua própria versão do TensorFlow Serving.

> Nota: Atualmente, TensorflowServing oferece suporte apenas à compilação de binários executados no Linux.

### Clone o projeto utilizando GIT

Com o Docker já instalado, usaremos o Git para clonar o branch principal do TensorFlow Serving:
```
git clone https://github.com/tensorflow/serving.git
cd serving
```

### Compile utilizando o script 'run_in_docker.sh':
Para criar em um ambiente hermético com todas as dependências atendidas, usaremos o script run_in_docker.sh. 
Esse script transmite comandos de construção para um contêiner do Docker. Por padrão, o script será construído com a imagem de desenvolvimento noturna mais recente do Docker. O TensorFlow Serving usa o Bazel como sua ferramenta de construção. Você pode usar os comandos do Bazel para criar destinos individuais ou toda a árvore de origem. Para construir a árvore inteira, execute:
```
tools/run_in_docker.sh bazel build -c opt tensorflow_serving/...

# Para compilar utilizando conjuntos de instruções específicos (ex. AVX), 
# adicione FLAGS correspondentes a sua arquitetura:
#
# AVX	--copt=-mavx
# AVX2	--copt=-mavx2
# FMA	--copt=-mfma
# SSE 4.1	--copt=-msse4.1
# SSE 4.2	--copt=-msse4.2
# All supported by processor	--copt=-march=native
```

Os binários são colocados no diretório bazel-bin e podem ser executados usando um comando como:
```
bazel-bin/tensorflow_serving/model_servers/tensorflow_model_server
```

Para testar sua nova compilação, execute:
```
tools/run_in_docker.sh bazel test -c opt tensorflow_serving/...
```



