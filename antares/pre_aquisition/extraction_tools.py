import numpy as np
import os
import cv2

def extract_moving_elements(images):
    """
    Remove noise from a set of images by computing the median image,
    followed by a sharpening filter.
    """
    # Calcular a imagem mediana
    images_stack = np.stack(images, axis=0)
    median_image = np.median(images_stack, axis=0).astype('uint8')
    
    # Definindo o kernel de nitidez
    sharpening_kernel = np.array([[ 0, -1,  0],
                                  [-1,  5, -1],
                                  [ 0, -1,  0]])

    smoothed_image = cv2.filter2D(median_image, -1, sharpening_kernel)

    return smoothed_image


def process_single_video(video, image_output, remove_rats, number_of_frames):
    """
    Processa um único vídeo para extrair frames com base no FPS e na variação de pixels.
    """
    if not os.path.exists(video):
        print(f"O vídeo '{video}' não existe.")
        return

    vidcap = cv2.VideoCapture(video)
    
    if not vidcap.isOpened():
        print(f"Falha ao abrir o vídeo '{video}'.")
        return

    fps = vidcap.get(cv2.CAP_PROP_FPS)  # Obter FPS do vídeo
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_diffs = []
    images = []
    frame_indices = []
    
    frame_interval = 2 * fps  # Pega um frame a cada 2 segundos (em número de frames)

    prev_frame = None
    for i in range(0, 1400, int(frame_interval)):
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, i)
        success, frame = vidcap.read()
        if not success:
            break

        # Calcular a diferença com o frame anterior
        if prev_frame is not None:
            diff = cv2.absdiff(cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY),
                               cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
            frame_diffs.append((i, np.sum(diff)))
        
        prev_frame = frame

    vidcap.release()

    # Selecionar os frames mais diferentes
    frame_diffs.sort(key=lambda x: x[1], reverse=True)  # Ordenar por diferença (decrescente)
    selected_indices = [idx for idx, _ in frame_diffs[:number_of_frames]]

    # Ler e salvar os frames selecionados
    vidcap = cv2.VideoCapture(video)
    for idx in sorted(selected_indices):
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        success, frame = vidcap.read()
        if success:
            images.append(frame)
            frame_indices.append(idx)

    vidcap.release()

    if images:
        if remove_rats == 1:
            result = extract_moving_elements(images)
        else:
            result = images
        file_name = os.path.basename(video).split('DLC')[0]
        output_path = os.path.join(image_output, f"{file_name}.jpg")
        cv2.imwrite(output_path, result)
        print(f"Salvo: {file_name}")
        print(f"Frames selecionados: {frame_indices}")