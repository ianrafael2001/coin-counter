# import cv2
# from keras.models import load_model
# import numpy as np

'''
    Aplica técnicas de melhoria de qualidade da imagem, como 
    redimensionamento, correção de iluminação e filtragem de ruído, 
    visando obter uma imagem mais adequada para a detecção das moedas.
'''
def pre_process():
    pass


'''
    Utiliza algoritmos de detecção de bordas, 
    como o operador de Sobel ou o algoritmo de Canny, para identificar
    as bordas das moedas na imagem pré-processada.
'''
def edge_detection():
    pass

'''
    Calcula características relevantes das moedas segmentadas,
    como diâmetro, área ou perímetro. Essas características
    são utilizadas para distinguir as diferentes moedas.
'''
def coin_segmentation():
    pass

'''
    Calcula características relevantes das moedas segmentadas,
    como diâmetro, área ou perímetro. Essas características
    são utilizadas para distinguir as diferentes moedas.
'''
def feature_extraction():
    pass


'''
    Classificação das moedas: Com base nas características extraídas,
    é criado um modelo de classificação capaz de identificar as moedas.
    Essa etapa utiliza técnicas como classificação por máquina de vetores
    de suporte (SVM), árvores de decisão ou redes neurais.
'''
def coin_classification():
    pass

'''
    O modelo de classificação é aplicado para
    classificar cada moeda e contar quantas vezes cada classe de
    moeda aparece na imagem.
'''
def coin_counter():
    pass


''' 
    Os resultados da contagem das moedas são apresentados
    na imagem original ou em uma nova imagem, destacando
    as moedas identificadas.
'''
def show_result():
    pass

while True:
    pass