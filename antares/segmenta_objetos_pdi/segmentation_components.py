'''
As funções presentes nesse codigo são responsaveis por extrair caracteristicas de formas geometricas presentes nas imagens
através dos cortornos dessas formas;
'''

import cv2
import numpy as np
import pandas as pd
import os

def find_contours(image_address):
     # Ler a imagem
    image = cv2.imread(image_address, cv2.IMREAD_GRAYSCALE)  # Lê diretamente como escala de cinza

    # Certifique-se de que a imagem é binária
    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Encontrar os contornos
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours

def contour_properties(contour):
    # Calculate moments of the contour
    M = cv2.moments(contour)

    # Calculate area of the contour
    area = cv2.contourArea(contour)

    # Calculate perimeter of the contour
    perimeter = cv2.arcLength(contour, True)

    # Calculate bounding box dimensions and aspect ratio
    x, y, w, h = cv2.boundingRect(contour)

    # Calculate minimum enclosing rectangle and circle
    rect = cv2.minAreaRect(contour)

    # Calculate rectangle coordinates and area
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    # Calculate centroid using different methods
    center_x = int(M["m10"] / M["m00"]) if M["m00"] != 0 else 0
    center_y = int(M["m01"] / M["m00"]) if M["m00"] != 0 else 0

    # Calculate circularity of the contour
    circularity = 4 * np.pi * area / (perimeter ** 2) if perimeter > 0 else 0

    # Calculate circle properties
    (_, _), radius = cv2.minEnclosingCircle(contour)
    center_circle = (int(center_x), int(center_y))

    return (area, circularity, radius, x, y, w, h, center_circle, center_x, center_y)
    
def process_contours(image_address, contours):
    image = cv2.imread(image_address)
    
    object_count = 0
    contour_data = {}  # Dictionary to store data of identified objects
    list_contours = []

    previous_contour = None  # Variável para armazenar o contorno anteriormente escolhido
    previous_contour_area = 0  # Variável para armazenar a área do contorno anteriormente escolhido

    for contour in contours:
        # Calculate contour properties
        area, circularity, radius, x, y, w, h, center_circle, cx_circle, cy_circle = contour_properties(contour)

        # Obtém as dimensões da imagem
        height, width = image.shape[:2]

        # Define as proporções para os intervalos de x e y
        x_min = int(0.2 * width)  # 20% da largura
        x_max = int(0.625 * width) # 62.5% da largura
        y_min = int(0.2 * height)  # 20% da altura
        y_max = int(0.55 * height) # 55% da altura

        # Atualiza a condição
        if area > 2000 and circularity > 0.425 and x_min < x < x_max and y_min < y < y_max and 50 < w < 160:
            # Limit the radius to a maximum value
            max_radius = 100
            radius = min(radius, max_radius)
            radius = int(radius)

            if radius < 80:
                radius += 30

            # Draw a circular contour
            cv2.circle(image, center_circle, radius, (255, 0, 0), 2)

            # Draw the central point
            cv2.circle(image, (cx_circle, cy_circle), 3, (255, 0, 0), -1)

            # Increment object count
            object_count += 1
            
            file_name = os.path.splitext(os.path.basename(image_address))[0]
            id, _ = file_name.split("_process")

            # Capture data
            contour_data = {
                "id" : id,
                "object": object_count,
                "Area": area,
                "Circularity": circularity,
                "Width": w,
                "Height": h,
                "X": cx_circle,
                "Y": cy_circle,
                "Radius": radius,
            }

            # Verifica se o contorno atual contém o contorno anteriormente escolhido
            if previous_contour is not None and area > previous_contour_area:
                # Define o contorno atual como o contorno anteriormente escolhido
                previous_contour = contour
                previous_contour_area = area
            elif previous_contour is None:
                # Define o contorno atual como o contorno anteriormente escolhido
                previous_contour = contour
                previous_contour_area = area
    
            list_contours.append(contour_data)
    
    # Adicionar um dicionário com valores 0 se nenhum contorno atender às condições
    if not list_contours:
        file_name = os.path.splitext(os.path.basename(image_address))[0]
        id, _ = file_name.split("_process")

        no_data = {
            "id": id,
            "object": 0,
            "Area": 0,
            "Circularity": 0,
            "Width": 0,
            "Height": 0,
            "X": 0,
            "Y": 0,
            "Radius": 0,
        }
        list_contours.append(no_data)

    # Criar um DataFrame
    df_contour = pd.DataFrame(list_contours)

    return image, df_contour
