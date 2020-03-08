# Docker - Tensorflow 2.0.1 Cheats (Suporte GPU)

## Iniciar container Tensorflow 2.0.1:
```
sudo docker run --gpus all -v $PWD:/tmp -w /tmp -it tensorflow tensorflow:2.0.1-gpu bash
```

## Iniciar container Tensorflow 2.0.1 com suporte ao jupyter note (HEADLESS):
```
sudo docker run --gpus all -it -p 8888:8888 -v $PWD:/tmp -w /tmp tensorflow/tensorflow:2.0.1-gpu-py3-jupyter &
```

## Iniciar container Tensorflow 2.0.1 com suporte ao jupyter note (BASH):
```
sudo docker run --gpus all -it -p 8888:8888 -v $PWD:/tmp -w /tmp tensorflow/tensorflow:2.0.1-gpu-py3-jupyter bash
```

### Para carregar o Jupyter Note no BASH com CORS habilitado para COLAB:
```
jupyter notebook \
  --NotebookApp.allow_origin='https://colab.research.google.com' \
  --port=8888 \
  --NotebookApp.port_retries=0 \
  --ip=0.0.0.0 \
  --allow-root
```

## Iniciar container TFX/Tensorflow_Serving e servir modelo:
```
sudo docker run --gpus all -p 8501:8501 -v /localpath/to/models_folder:/models/flowers -e MODEL_NAME=flowers -it tensorflow/serving:latest-gpu bash
```
