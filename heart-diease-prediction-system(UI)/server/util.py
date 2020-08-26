import pickle
import json
import numpy as np


__restecg = None
__thal = None
__slope = None
__cp = None
__data_columns = None
__model = None


def get_heart_diease_status(age, sex, trestbps, chol, fbs, thalach, exang, oldpeak, ca, restecg, thal, slope, cp):
    try:
        restecg_index = __data_columns.index(restecg.lower())
        thal_index = __data_columns.index(thal.lower())
        slope_index = __data_columns.index(slope.lower())
        cp_index = __data_columns.index(cp.lower())

    except:
        restecg_index = -1
        thal_index = -1
        slope_index = -1
        cp_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = age
    x[1] = sex
    x[2] = trestbps
    x[3] = chol
    x[4] = fbs
    x[5] = thalach
    x[6] = exang
    x[7] = oldpeak
    x[8] = ca

    if restecg_index >= 0:
        x[restecg_index] = 1

    if thal_index >= 0:
        x[thal_index] = 1

    if slope_index >= 0:
        x[slope_index] = 1

    if cp_index >= 0:
        x[cp_index] = 1
    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __restecg
    global __thal
    global __slope
    global __cp

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __restecg = __data_columns[9:12]
        print(__restecg)
        __thal = __data_columns[12:16]
        print(__thal)
        __slope = __data_columns[16:19]
        print(__slope)
        __cp = __data_columns[19:23]
        print(__cp)

    global __model
    if __model is None:
        with open('./artifacts/heart_diease_prediction_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_restecg_names():
    return __restecg

def get_thal_names():
    return  __thal


def get_slope_names():
    return __slope


def get_cp_names():
    return __cp


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_data_columns())
    print(get_restecg_names())
    print(get_thal_names())
    print(get_slope_names())
    print(get_cp_names())
    print(get_heart_diease_status(63, 1, 145, 233, 1, 150, 0, 2.3, 0, "restecg_0", "thal_1", "slope_0", "cp_3"))
