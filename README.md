# Contador de Moedas

Este é um código que utiliza técnicas de processamento de imagem e aprendizado de máquina para realizar a contagem e classificação de moedas em uma imagem ou vídeo capturado pela câmera.

## Descrição do problema

O objetivo desse código é automatizar a contagem de moedas em uma imagem ou vídeo, bem como identificar o valor das moedas encontradas. Essa funcionalidade pode ser útil em várias aplicações, como caixas registradoras automáticas, sistemas de pagamento automatizados, sistemas de controle de estoque, entre outros.

## Descrição da base de dados e/ou das imagens

Esse código não depende de uma base de dados prévia. Ele utiliza técnicas de processamento de imagem para segmentar e extrair características das moedas presentes na imagem ou vídeo fornecido.

## Descrição do método utilizado

O código utiliza os seguintes passos para realizar a contagem e classificação de moedas:

1. Pré-processamento da imagem: Aplica técnicas de melhoria de qualidade da imagem, como redimensionamento, correção de iluminação e filtragem de ruído, visando obter uma imagem mais adequada para a detecção das moedas.

2. Detecção de bordas: Utiliza algoritmos de detecção de bordas, como o algoritmo de Canny, para identificar as bordas das moedas na imagem pré-processada.

3. Segmentação das moedas: Com base nas bordas detectadas, aplica algoritmos de segmentação para separar as moedas do plano de fundo. Isso pode ser feito usando técnicas de limiarização ou segmentação baseada em regiões.

4. Classificação das moedas: Com base nas características extraídas, foi criado um modelo de classificação capaz de identificar as moedas. Neste código, é utilizado um modelo de classificação carregado a partir de um arquivo (Keras_model.h5) e a biblioteca Keras.

5. Contagem e exibição dos resultados: Os resultados da contagem das moedas são apresentados na imagem original ou em uma nova imagem, destacando as moedas identificadas. Além da contagem, é exibida a classe (valor) e a porcentagem de confiança da classificação para cada moeda identificada.

## Documentação geral do código

O código está estruturado da seguinte forma:

- Função `pre_process(image)`: Aplica técnicas de melhoria de qualidade da imagem, como correção de iluminação e filtragem de ruído, para preparar a imagem para detecção de bordas.

- Função `edge_detection(image)`: Utiliza o algoritmo de Canny para detectar as bordas nas moedas presentes na imagem.

- Função `coin_segmentation(edges)`: Realiza a segmentação das moedas com base nas bordas detectadas, utilizando técnicas de limiarização e segmentação baseada em regiões.

- Função `coin_classification(coin_image)`: Realiza a classificação das moedas com base nas características extraídas. Utiliza um modelo de classificação carregado a partir de um arquivo (Keras_model.h5) e

 a biblioteca Keras.

- Função `show_result()`: Captura imagens da câmera em tempo real e aplica os passos de pré-processamento, detecção de bordas, segmentação e classificação das moedas. Os resultados são exibidos na imagem original ou em uma nova imagem, destacando as moedas identificadas e apresentando a contagem, a classe e a porcentagem de confiança da classificação para cada moeda.

- Função `filterByArea(cnt)`: Função auxiliar para filtrar os contornos das moedas com base em sua área.

Para executar o código, basta chamar a função `show_result()`. Certifique-se de ter o arquivo `Keras_model.h5` presente no mesmo diretório do código para carregar o modelo de classificação.

Observação: É necessário ter as bibliotecas OpenCV, NumPy e Keras instaladas para executar o código corretamente.