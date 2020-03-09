import os
import base64
import json
import io
from io import BytesIO
import numpy as np
import requests
import tensorflow as tf
from flask import Flask, request, jsonify
from keras.preprocessing import image
from flask_cors import CORS


app = Flask(__name__)
labels_cache = {}

tensorflow_serving_url = "http://localhost:8501/"
tensorflow_serving_model_version = "v1"
labels_directory_path = "./labels/"

# Descomente essa linha caso precise realizar chamadas CROSS ORIGIN (CORS)
CORS(app)

@app.route('/<string:model>/predict/', methods=['POST'])
def image_classifier(model):
    url = tensorflow_serving_url + tensorflow_serving_model_version + "/models/"+model+":predict"
    labels_filepath = labels_directory_path + "" + model +".txt"
    if not model in labels_cache:
        if (os.path.exists(labels_filepath)):
            labels = _load_labels(labels_filepath)
            labels_cache[model]=labels
        else:
            labels_cache[model]= None

    if request.files and 'image' in request.files:
        # Decodifica e pre-processa uma imagem recebida por FORM_DATA.
        image_file = request.files['image']
        img = image.img_to_array(image.load_img(BytesIO(image_file.read()),target_size=(224, 224))) / 255.
    elif 'b64' in request.form:
        # Decodifica e pre-processa uma imagem no formato Base64
        img = image.img_to_array(image.load_img(BytesIO(base64.b64decode(request.form['b64'])),target_size=(224, 224))) / 255.
    else:
        return

    # Preparando o PAYLOAD para a requisição Tensorflow/Serving
    payload = {
        "instances": [img.tolist()]
    }

    # Realiza o POST
    r = requests.post(url, json=payload)

    # Decodificando os resultados do TensorFlow Serving server
    pred = json.loads(r.content.decode('utf-8'))
    predictions = np.array(pred["predictions"])
    label_id = np.argmax(predictions, axis=-1)[0]

    top=50
    results = []
    for p in predictions:
        top_indices = p.argsort()[-top:][::-1]
        if labels_cache[model]!=None:
            results = [ {'label':(labels_cache[model][(i)]),'prob':(p[i])} for i in top_indices ]
        else:
            results =  p.tolist() 

    # Retornando JSON rpara o frontend
    return jsonify(results)


def _load_labels(filename):
    with tf.io.gfile.GFile(filename, "r") as f:
        return [label.strip("\n") for label in f]
