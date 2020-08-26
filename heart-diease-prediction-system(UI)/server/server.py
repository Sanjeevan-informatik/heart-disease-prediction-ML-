from flask import Flask, request, jsonify

import util

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hi"

@app.route('/get_restecg_names', methods=['GET'])
def get_restecg_names():
    response = jsonify({
        'restecg': util.get_restecg_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_thal_names', methods=['GET'])
def get_thal_names():
    response = jsonify({
        'thal': util.get_thal_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



@app.route('/get_slope_names', methods=['GET'])
def get_slope_names():
    response = jsonify({
        'slope': util.get_slope_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_cp_names', methods=['GET'])
def get_cp_names():
    response = jsonify({
        'cp': util.get_cp_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/heart_diease_prediction', methods=['GET', 'POST'])
def heart_diease_prediction():
    age = int(request.form['age'])
    sex = int(request.form['sex'])

    trestbps = int(request.form['trestbps']),
    chol = int(request.form['chol'])
    thalach = int(request.form['thalach'])
    oldpeak = float(request.form['oldpeak'])
    ca = int(request.form['ca'])
    restecg =request.form['restecg']
    thal = request.form['thal']
    response = jsonify({
        'heart_diease_status': util.get_heart_diease_status(age , sex,  trestbps,  chol,  thalach,oldpeak, ca , restecg ,  thal , "slope_0", "cp_3" )
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For heart_diease_prediction...")
    util.load_saved_artifacts()
    print("this is ", util.get_heart_diease_status(23, 1, 22, 1, 1, 2, 1, 2, 1, "restecg_1", "thal_1", "slope_0", "cp_3"))

    app.run()
