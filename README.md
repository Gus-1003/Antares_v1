# Antares
Sistema para Reconhecimento de Objetos em Contexto de Campo Aberto para Estudo da Memória Declarativa Espacial.

## Justificativa do Desenvolvimento
* A necessidade da identificação automática de objetos utilizados em gravações do teste de reconhecimento de objetos em campo aberto de forma rápida e simples, que possa ser utilizada em diferentes contextos, e que possibilite a contagem automatica da exploração desses objetos.

## Funcionalidades Principais
* Reconhecimento automático de objetos: Identifica e monitora objetos em vídeos experimentais.
* Adaptabilidade: Funciona em condições variadas de iluminação e com objetos de diferentes formatos e colorações.

## Entradas do Sistema
* Endereço da pasta: Caminho para a pasta onde estão armazenados os arquivos de vídeo do experimento.

## Metodologia
<p align="center">
  <img src="https://github.com/Gus-1003/Antares/blob/main/Fluxograma.png">
</p>

## Possibilidades dos videos:
* Podem ou não conter animais.
* O campo pode possuir diferentes graus de iluminação.
* Os objetos podem possuir diferentes formatos geométricos.
* Os objetos podem possuir diferentes colorações.

## Validação
O sistema foi validado com vídeos contendo:

* Caixa de 60x60x60 cm.
* Câmera do modelo "Microsoft Lifecam Cinema" posicionada a 90 cm do fundo da caixa em um ângulo de 90º.
* Vídeos com e sem animais.
* Diferentes graus de iluminação nas caixas.
* Objetos de formas circulares e quadriláteras.
* Objetos feitos de metal, plástico e vidro.

## Pré-requisitos
* Python 3.x
* Bibliotecas necessárias: opencv-python, numpy, pandas, scikit-learn, matplotlib.

## Instalação das Dependências (Caso use nativo no Desktop)
* pip install opencv-python numpy pandas scikit-learn matplotlib

## Como utilizar:
* Baixar o código: Faça o download do código "antares_test".
* Salvar o código: Salve o código na conta do Google Drive que possui acesso aos vídeos.
* Configurar o caminho: Insira no código o endereço dos vídeos e o local onde serão armazenados os dados de saída.
* Executar o código: Rode o código com o comando: python antares_test.py (Caso use nativo no Desktop)

## Resultados Esperados
O sistema gera um relatório contendo:

* A posição do centro de cada objeto e seus respectivos raios e áreas.
* Imagens com as áreas dos objetos demarcadas

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

## Informações Adicionais
Projeto realizado no Instituto Santos Dumont (ISD) com a colaboração da Escola Agrícola de Jundiaí (EAJ) - Universidade Federal do Rio Grande do Norte (UFRN).

- Autor: G.G. Maciel
- Colaboradores: A. M. Pacheco, M. C. Gonzalez
- Ano: 2025
