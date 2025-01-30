import cv2
import os
import glob

from . import segmentation_components as mtds_seg
  
def segmentation_all_objects(images_adress):
    
    image_package = glob.glob(f"{images_adress}/*process.jpg")
    
    # Processar as imagens
    for image_addres in image_package:
        dir_name, file_name = os.path.split(image_addres)
        base_name, ext = os.path.splitext(file_name)
        
        # Obter contornos usando a função apropriada
        contours = mtds_seg.find_contours(image_addres)
        
        # Processar os contornos e gerar a imagem segmentada
        tagged_image, contours_data = mtds_seg.process_contours(image_addres, contours)
        
        # Criar o nome do arquivo segmentado
        processed_image_name = f"{base_name}_segmentaded{ext}"
        processed_image_path = os.path.join(dir_name, processed_image_name)
        cv2.imwrite(processed_image_path, tagged_image)
        print(f"Imagem segmentada salva em: {processed_image_path}")
    
        processed_csv_name = f"{base_name}_segmentaded.csv"
        processed_csv_path = os.path.join(dir_name, processed_csv_name)
        contours_data.to_csv(processed_csv_path, index=False)
        print(f"csv das posições do objeto: {processed_csv_path}")