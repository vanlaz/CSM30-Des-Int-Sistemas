# S - Número de amostras do sinal,  N - Número de elementos sensores
import numpy as np

#TODO: transform entry sign in vector
def signal_gain(matrix_type):
    N = 64
    S1 = 794
    S = 436

    if matrix_type == '1':
        S = S1

    gl = 0
    for i in range(0, S):
        for j in range(0, N):
            gamma = 100 + (1 / 20) * j * (j ** 0.5)
            vector[i][j] *= gamma 
    return S


def image_reshape(image, matrix_type):
    image = image - image.min()
    image = image / image.max()
    image = image * 255
    if matrix_type == '1':
        image = image.reshape((60, 60), order='F')
    else:
        image = image.reshape((30, 30), order='F')
    return image


def processing_requirements(matrix_type, signal_type):
    model_path = "model_2"
    if matrix_type == "1":
        model_path = "model_1"
    print(f"Model path: {model_path}")
    print(f"Signal type: {signal_type}")
    file = open(f'./input/{model_path}/{signal_type}.csv', 'rb')
    entry_sign = np.loadtxt(file, delimiter=',')
    matrix = open(f'./input/{model_path}/H.csv', 'rb')
    matrix = np.loadtxt(matrix, delimiter=',')

    return entry_sign, matrix
