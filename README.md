# Contador de Moedas

Por:
 - Bernardo Ragonezi Silva Lopes
 - Ian Rafael de Souza Oliveira
 - Pedro Henrique Ramos Loura

Professor:
 - Felipe Augusto Lima Reis

Este é um código que utiliza técnicas de processamento de imagem e aprendizado de máquina para realizar a contagem e classificação de moedas em uma imagem ou vídeo capturado pela câmera.

## Descrição do problema

O objetivo desse código é automatizar a contagem de moedas em uma imagem ou vídeo, bem como identificar o valor das moedas encontradas. Essa funcionalidade pode ser útil em várias aplicações, como caixas registradoras automáticas, sistemas de pagamento automatizados, sistemas de controle de estoque, entre outros.

## Descrição da base de dados e/ou das imagens

A base de dados utilizada, foi uma base disponilizada no git: https://github.com/WellingtonDev25/contagemMoedas, o modelo foi treinado na ferramenta teachablemachine (https://teachablemachine.withgoogle.com/). Ele utiliza técnicas de processamento de imagem para segmentar e extrair características das moedas presentes na imagem.

Foi disponibilizada 654 imagens para treinamento:
 - 25 centavos: 244 imagens
 - 50 centavos: 198 imagens
 - 1 real: 212 imagens

O modelo e as imagens estão disponibilizado nos arquivos do repositório.

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

- Função `coin_classification(coin_image)`: Realiza a classificação das moedas com base nas características extraídas. Utiliza um modelo de classificação carregado a partir de um arquivo (Keras_model.h5) e a biblioteca Keras.

- Função `show_result()`: Captura imagens da câmera em tempo real e aplica os passos de pré-processamento, detecção de bordas, segmentação e classificação das moedas. Os resultados são exibidos na imagem original ou em uma nova imagem, destacando as moedas identificadas e apresentando a contagem, a classe e a porcentagem de confiança da classificação para cada moeda.

- Função `filterByArea(cnt)`: Função auxiliar para filtrar os contornos das moedas com base em sua área.

Para executar o código, basta chamar a função `show_result()`. Certifique-se de ter o arquivo `Keras_model.h5` presente no mesmo diretório do código para carregar o modelo de classificação.

Observação: É necessário ter as bibliotecas OpenCV, NumPy e Keras instaladas para executar o código corretamente.


# Tutorial: Executando o Contador de Moedas

Este tutorial irá orientá-lo sobre como executar o script do Contador de Moedas em seu ambiente. Certifique-se de seguir os passos abaixo para garantir que todas as dependências estejam instaladas corretamente.

## Pré-requisitos

Antes de prosseguir, verifique se você tem o Python e o pip instalados em seu sistema. Você pode verificar a versão do Python digitando o seguinte comando no terminal:

```
python --version
```

Certifique-se de ter o Python 3.x instalado. Caso não o tenha, faça o download e a instalação do Python a partir do site oficial: https://www.python.org/downloads/

O pip é o gerenciador de pacotes do Python e é necessário para instalar as bibliotecas de terceiros utilizadas pelo script. Verifique se você tem o pip instalado digitando o seguinte comando no terminal:

```
pip --version
```

Se o comando não for reconhecido, você pode instalá-lo seguindo as instruções em: https://pip.pypa.io/en/stable/installing/

## Passo 1: Instalando as dependências

O script do Contador de Moedas depende das seguintes bibliotecas:

- OpenCV: biblioteca de processamento de imagem
- NumPy: biblioteca para manipulação de arrays multidimensionais
- Keras: biblioteca para construção e treinamento de redes neurais
- Tensorflow: biblioteca para construção e treinamento de redes neurais

Para instalar as bibliotecas, execute os seguintes comandos no terminal:

```
pip install opencv-python
pip install numpy
pip install keras==2.6.0
pip install tensorflow==2.9.1
```

## Passo 2: Preparando o modelo de classificação

O script utiliza um modelo de classificação pré-treinado para identificar as moedas. Certifique-se de ter o arquivo `Keras_model.h5` no mesmo diretório do script. Se você não possui um modelo de classificação personalizado, pode utilizar o modelo de exemplo fornecido pelo script.

## Passo 3: Executando o script

Após instalar as dependências e preparar o modelo de classificação, você pode executar o script do Contador de Moedas. Certifique-se de ter a câmera disponível em seu sistema.

Navegue até o diretório onde o script está localizado e execute o seguinte comando no terminal:

```
python app.py
```

O script irá capturar imagens da câmera em tempo real e exibirá os resultados na imagem original e em uma imagem segmentada, destacando as moedas identificadas e apresentando a contagem, a classe e a porcentagem de confiança da classificação para cada moeda.

## Observações

- Certifique-se de que a câmera esteja funcionando corretamente e seja acessível pelo OpenCV. Se necessário, verifique as configurações da câmera em seu sistema.

- Se você estiver usando um ambiente virtual do Python, verifique se o ambiente virtual está ativado antes de executar os comandos de instalação e execução do script.

- Se você deseja personalizar o modelo de classificação, você pode treinar seu próprio modelo ou utilizar técnicas de transferência de aprendizado. No entanto, esse processo está além do escopo deste tutorial.

Agora você pode executar o script do Contador de Moedas e experimentar a contagem e classificação de moedas em tempo real!
