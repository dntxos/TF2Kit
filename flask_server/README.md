![IMG](../images/flask_tit.png)

# Tensorflow-Serving Flask Template
Utilize esse template 'App Flask' para servir uma API RestFul de alto nível como interface para consumir seus modelos no Tensorflow/Serving.

## Por que utilizar Flask se o Tensorflow/Serving já oferece suporte RestFul?
Embora o Tensorflow/Serving ofereça APIs REST, ainda é uma interface de baixo nível, recebendo como NDArray (Tensors) como INPUT e retornando o último layer do modelo. Sendo necessário então decodificar a imagem e tranformar em vetor de números flutuantes (Float32), e decodificar o retorno do último layer de acordo com nosso modelo.
Essa aplicação Flask intermediará a comunicação com o Tensorflow/Serving com requisições Http POST simplificadas, aceitando imagens no FORM_DATA, tanto tipo FILE quanto B64.

## Requisitos
* Numpy >=1.18
* Tensorflow >=1.14
* Keras 2.3.1
* Flask 1.1.1
* Flask-Cors 3.0.8

## Intalando o Flask
```
pip3 install flask
pip3 install flask_cors
sudo apt install python3-flask
```

## Iniciando o FLASK
```
export FLASK_ENV=development && export FLASK_APP=app.py && flask run --host=0.0.0.0
```
