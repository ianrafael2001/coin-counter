import cv2
import numpy as np
from keras.models import load_model


video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

model = load_model('Keras_model.h5',compile=False)
data = np.ndarray(shape=(1,224,224,3),dtype=np.float32)
classes = ["1 real","25 centavos","50 centavos"]

'''
    Aplica técnicas de melhoria de qualidade da imagem, como 
    redimensionamento, correção de iluminação e filtragem de ruído, 
    visando obter uma imagem mais adequada para a detecção das moedas.
'''
def pre_process(image):
    # Correção de iluminação
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    enhanced_image = clahe.apply(gray_image)

    # Filtragem de ruído
    denoised_image = cv2.fastNlMeansDenoising(enhanced_image, h=10)

    return denoised_image

'''
    Utiliza algoritmos de detecção de bordas, o algoritmo de Canny, 
    para identificar as bordas das moedas na imagem pré-processada.
'''
def edge_detection(image):
    # Aplica o algoritmo de Canny para detectar as bordas
    edges_canny = cv2.Canny(image, 50, 150)

    return edges_canny

'''
    Com base nas bordas detectadas, aplique algoritmos de segmentação 
    para separar as moedas do plano de fundo. Isso pode ser feito usando 
    técnicas de limiarização ou segmentação baseada em regiões.
'''
def coin_segmentation(edges):
    # Aplica a limiarização para segmentar as moedas
    _, threshold = cv2.threshold(edges, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Aplica a segmentação baseada em regiões para separar as moedas
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Cria uma máscara para destacar as moedas
    mask = cv2.drawContours(np.zeros_like(edges), contours, -1, (255), thickness=cv2.FILLED)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=3)
    segmented_image = cv2.erode(mask, kernel, iterations=2)

    return segmented_image

'''
    Com base nas características extraídas,
    é criado um modelo de classificação capaz de identificar as moedas.
    Essa etapa utiliza técnicas como classificação por máquina de vetores
    de suporte (SVM), árvores de decisão ou redes neurais.
    # Base função pega no repositorio: https://github.com/WellingtonDev25/contagemMoedas
'''
def coin_classification(coin_image):
    coin_image = cv2.resize(coin_image,(224,224))
    coin_image = np.asarray(coin_image)
    coin_image_normalize = (coin_image.astype(np.float32)/127.0)-1
    data[0] = coin_image_normalize
    prediction = model.predict(data)
    index = np.argmax(prediction)
    percent = prediction[0][index]
    classe = classes[index]
    return classe,percent


''' 
    Os resultados da contagem das moedas são apresentados
    na imagem original ou em uma nova imagem, destacando
    as moedas identificadas.
'''
def show_result():
    while True:
        _,image = video.read()
        image = cv2.resize(image,(640,480))
        image_original = image
        preprocessed_image = pre_process(image)
        edges_canny = edge_detection(preprocessed_image)
        segmented_image = coin_segmentation(edges_canny)
        
        # Encontra os contornos das moedas na imagem segmentada
        contours, _ = cv2.findContours(segmented_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        #filtra o contorno pelo tamanho da area
        contoursFilter = list(filter(filterByArea, contours))    
        
        # Desenha os contornos filtrados na imagem segmentada
        coins_image = cv2.cvtColor(segmented_image, cv2.COLOR_GRAY2BGR)
        cv2.drawContours(coins_image, contoursFilter, -1, (0, 255, 0), 2)
        
        # Conta o número de moedas    
        num_coins = len(contoursFilter)
        
        cv2.putText(image,f'Quantidade de moedas: {num_coins}',(0,30),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,255,255),2)
        
        for cnt in contoursFilter:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
            recorte = image_original[y:y +h,x:x+ w]
            
            # faz a classificação da moeda
            classe, accuracy = coin_classification(recorte)
            
            accuracy_form = float("{:.2f}".format(accuracy))
            
            cv2.putText(image,str(classe),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
            cv2.putText(image,f'{int(accuracy_form*100)}%',(x ,y - 25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0),2)
                
        cv2.imshow('Imagem resultado',image)
        cv2.imshow('Imagem Pre-Processada', preprocessed_image)
        cv2.imshow('Imagem da borda', edges_canny)
        cv2.imshow('Imagem segmentada',segmented_image)
        cv2.waitKey(1)
        pass

def filterByArea(cnt):
   area = cv2.contourArea(cnt)
   return area > 2000

show_result()