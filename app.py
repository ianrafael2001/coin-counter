import cv2
import numpy as np

'''
    Aplica técnicas de melhoria de qualidade da imagem, como 
    redimensionamento, correção de iluminação e filtragem de ruído, 
    visando obter uma imagem mais adequada para a detecção das moedas.
'''
def pre_process(image):
    
    # Redimensionamento da imagem
    resized_image = cv2.resize(image, (800, 600))

    # Correção de iluminação
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    enhanced_image = clahe.apply(gray_image)

    # Filtragem de ruído
    denoised_image = cv2.fastNlMeansDenoising(enhanced_image, h=10)

    return denoised_image

'''
    Utiliza algoritmos de detecção de bordas, 
    como o operador de Sobel ou o algoritmo de Canny, para identificar
    as bordas das moedas na imagem pré-processada.
'''
def edge_detection(image):
    # Aplica o algoritmo de Canny para detectar as bordas
    edges_canny = cv2.Canny(image, 50, 150)

    return edges_canny

'''
    Calcula características relevantes das moedas segmentadas,
    como diâmetro, área ou perímetro. Essas características
    são utilizadas para distinguir as diferentes moedas.
'''
def coin_segmentation(edges):    
    # Aplica a limiarização para segmentar as moedas
    _, threshold = cv2.threshold(edges, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Aplica a segmentação baseada em regiões para separar as moedas
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Cria uma máscara para destacar as moedas
    mask = cv2.drawContours(np.zeros_like(edges), contours, -1, (255), thickness=cv2.FILLED)

    # Aplica a máscara na imagem original para obter somente as moedas
    segmented_image = cv2.bitwise_and(edges, edges, mask=mask)
    return segmented_image

'''
    Calcula características relevantes das moedas segmentadas,
    como diâmetro, área ou perímetro. Essas características
    são utilizadas para distinguir as diferentes moedas.
'''
def feature_extraction():
    pass

'''
    Com base nas características extraídas,
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
def coin_counter(segmented_image):
    # Encontra os contornos das moedas na imagem segmentada
    contours, _ = cv2.findContours(segmented_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Desenha os contornos das moedas na imagem original
    coins_image = cv2.cvtColor(segmented_image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(coins_image, contours, -1, (0, 255, 0), 2)

    # Conta o número de moedas
    num_coins = len(contours)

    # Exibe a imagem com as áreas das moedas
    cv2.imshow("Coins", coins_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return num_coins

''' 
    Os resultados da contagem das moedas são apresentados
    na imagem original ou em uma nova imagem, destacando
    as moedas identificadas.
'''
def show_result():
    pass



image = cv2.imread('./assets/image.jpg')

preprocessed_image = pre_process(image)

cv2.imshow("preprocessed_image", preprocessed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

edges_canny = edge_detection(preprocessed_image)

cv2.imshow("preprocessed_image", edges_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

segmented_image = coin_segmentation(edges_canny)

cv2.imshow("segmented_image", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# feature_extraction()

# coin_classification()

num_coins = coin_counter(segmented_image)

print("Número de moedas encontradas:", num_coins)


# while True:
#     pass