'''
As funções presentes nesse codigo são responsaveis por realçar as formas dos objetos presentes em uma imagem.'''

import cv2
import numpy as np

# Forma os contornos dos objetos
def apply_filters(image):
    # Equalize the histogram of the input image
    # equalized_image = cv2.equalizeHist(image)

    # Convert the equalized image to float32 format
    image32f = np.float32(image)

    # Compute mean and variance using a 3x3 kernel
    mu = cv2.blur(image32f, (3, 3))
    mu2 = cv2.blur(image32f * image32f, (3, 3))

    sigma = cv2.sqrt(mu2 - mu * mu)

    # Scale sigma for better visualization
    sigma = sigma * 10

    # Convert sigma to unsigned 8-bit integer
    sigma = sigma.astype("uint8")

    # Suppress edges by setting a border region to zero
    sigma[:20, :] = 0
    sigma[-20:, :] = 0
    sigma[:, :20] = 0
    sigma[:, -20:] = 0

    return sigma

# Destaca esses objetos da area de fundo da imagem
def apply_threshold(image):
    # Compute the gradients using Sobel operators
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate the magnitude of the gradient
    gradient_magnitude = cv2.magnitude(sobelx, sobely)

    # Normalize the gradient magnitude
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # Apply thresholding using the Otsu method
    _, gradient_threshold = cv2.threshold(gradient_magnitude, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return gradient_threshold

# Aumenta a área ocupada pela forma dos objetos para formar uma area em volta (terreno de exploração)
def apply_morphological_operations(image):
    # Define a kernel with a slightly larger size
    kernel = np.ones((7, 7), np.uint8)  # Tamanho maior para manipulações mais amplas

    # Aplica fechamento (closing) para preencher buracos
    closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Aplica dilatação para destacar os objetos
    dilated_image = cv2.dilate(closed_image, kernel, iterations=3)

    # Reduz o ruído ou pequenos artefatos com erosão
    eroded_image = cv2.erode(dilated_image, kernel, iterations=2)

    # Refina as bordas com abertura (opening)
    refined_image = cv2.morphologyEx(eroded_image, cv2.MORPH_OPEN, kernel, iterations=1)

    # Opcional: Aplica um GaussianBlur para suavizar a imagem (ideal antes de detectar contornos)
    smoothed_image = cv2.GaussianBlur(refined_image, (5, 5), 0)
    
    return smoothed_image


def process_pipeline(frame):
  """
  Objetivo: 
      Realiza o processamento para aumentar o contrate das regiões alvo

  Args:
      frame (str): Recebe um quadro (Matriz 2D)

  Returns:
      Imagem resultante do processo.
  """

  # Read the image from the specified path
  image = cv2.imread(frame)

  # Convert the image to grayscale
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply filters to the grayscale image
  filtered_image = apply_filters(gray_image)

  # Apply thresholding to the filtered image
  thresholded_image = apply_threshold(filtered_image)
  
  # Apply morphological operations
  modified_image = apply_morphological_operations(thresholded_image)

  # Return contours
  return modified_image

