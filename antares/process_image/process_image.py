''' 
Esse código possui a função de realizar todos as funções de forma encadeada. Tornando mais acessivel
o uso da biblioteca pelo usuário.
'''

import cv2
import glob
from . import components
import os

def process_all_image(images_adress):
    
    image_package = glob.glob(f"{images_adress}/*.jpg")
    
    print(f"Quantidade de imagens para processamento: {len(image_package)}")
    
    # Processar os vídeos
    for image in image_package:
        dir_name, file_name = os.path.split(image)
        base_name, ext = os.path.splitext(file_name)
        
        modified_image = components.process_pipeline(image)
        
        processed_name = f"{base_name}_process{ext}"
        processed_path = os.path.join(dir_name, processed_name)
        
        cv2.imwrite(processed_path, modified_image)
        print(f"Imagem processada salva em: {processed_path}")