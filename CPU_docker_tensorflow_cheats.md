# Docker - Tensorflow 2.0.1 Cheats (Suporte CPU)

## Iniciar container Tensorflow 2.0.1:
```
sudo docker run -v $PWD:/tmp -w /tmp -it tensorflow tensorflow:2.0.1 bash
```

## Iniciar container Tensorflow 2.0.1 com suporte ao jupyter note (HEADLESS):
```
sudo docker run -it -p 8888:8888 -v $PWD:/tmp -w /tmp tensorflow/tensorflow:2.0.1-py3-jupyter &
```

## Iniciar container Tensorflow 2.0.1 com suporte ao jupyter note (BASH):
```
sudo docker run -it -p 8888:8888 -v $PWD:/tmp -w /tmp tensorflow/tensorflow:2.0.1-py3-jupyter bash
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
sudo docker run -p 8501:8501 -v /localpath/to/models_folder:/models/flowers -e MODEL_NAME=flowers -it tensorflow/serving:latest bash
```
