def contour_properties(contour):
  import cv2
  import numpy as np

  # Calculate moments of the contour
  M = cv2.moments(contour)

  # Calculate area of the contour
  area = cv2.contourArea(contour)

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

  # Calculate circle properties
  (_, _), radius = cv2.minEnclosingCircle(contour)
  center_circle = (int(center_x), int(center_y))

  return (area, radius, x, y, w, center_circle, center_x, center_y)
  
def process_contours(frame, contours, background):
  import cv2

  object_count = 0
  contour_data = {}  # Dictionary to store data of identified objects
  result = {}

  previous_contour = None  # Variável para armazenar o contorno anteriormente escolhido
  previous_contour_area = 0  # Variável para armazenar a área do contorno anteriormente escolhido

  for contour in contours:

    # Calculate contour properties
    area, radius, x, y, w, center_circle, cx_circle, cy_circle = contour_properties(contour)

    if background == 1:
      w += 20

    # Check if the contour matches a circular pattern
    if area > 2000 and 20 < radius < 100 and  100 < x < 800 and 150 < y < 400 and 80 < w < 160:
      # Limit the radius to a maximum value
      max_radius = 100
      radius = min(radius, max_radius)
      radius = int(radius)

      if radius < 80:
          radius += 30

      # Draw a circular contour
      cv2.circle(frame, center_circle, radius, (255, 0, 0), 2)

      # Draw the central point
      cv2.circle(frame, (cx_circle, cy_circle), 3, (255, 0, 0), -1)

      # Increment object count
      object_count += 1

      # Capture data
      contour_data = [{
        "object": object_count,
        "eixo_X": cx_circle,
        "eixo_Y": cy_circle,
        "Radius": radius,
      }]

      # Verifica se o contorno atual contém o contorno anteriormente escolhido
      if previous_contour is not None and area > previous_contour_area:
        # Define o contorno atual como o contorno anteriormente escolhido
        previous_contour = contour
        previous_contour_area = area
      elif previous_contour is None:
        # Define o contorno atual como o contorno anteriormente escolhido
        previous_contour = contour
        previous_contour_area = area

      for idx, contour in enumerate(contour_data, start=1):
        for key, value in contour.items():
            result[f"{key}_{idx}"] = value

  # Transformando o resultado em uma lista de um único dicionário para manter a estrutura original
  result_objects = [result]

  return frame, result_objects

