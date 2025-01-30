import sys
import os
import time
import cv2

# Adiciona a pasta 'libs' ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'libs')))

from antares.process_image import process_image as psi # type: ignore

# Início do contador de tempo
start_time = time.time()

name_amostra = "CCM247-TR-Contexto2_adaptative"

# Diretórios e vídeos
image_test = f'C:/Users/ariog/Downloads/test_Antares/{name_amostra}.jpg'

# Armazenamento do processo
image = psi.process_frame(image_test)

# Exibe a imagem em uma janela
cv2.imshow(f'Imagem teste "{name_amostra}', image)

# Espera até que uma tecla seja pressionada para fechar a janela
cv2.waitKey(0)

# Fecha todas as janelas abertas após pressionar uma tecla
cv2.destroyAllWindows()

# Fim do contador de tempo
end_time = time.time()

# Calcular e imprimir o tempo total
print(f"Tempo de execução: {end_time - start_time} segundos")