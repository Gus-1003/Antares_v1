import os
import glob

from . import extraction_tools as ef

def frames_generate(videos_adrres, image_output, remove_rats=1, number_of_frames=5):
    """
    Processa uma lista de vídeos e salva as imagens resultantes em um diretório de saída.

    Args:
        videos_adrres (list): Lista de caminhos dos arquivos de vídeo.
        image_output (str): Diretório onde as imagens extraídas serão salvas.
        remove_rats (bool): 0 - usar imagem original, 1 - Para remover rato na imagem
        number_of_frames (int): Número de frames a serem extraídos de cada vídeo.
    Returns:
        None
    """
    video_package = glob.glob(f"{videos_adrres}/*.MP4")

    print(f"Começou. A quantidade de videos são {len(video_package)} extraindo {number_of_frames} quadros de cada video.")
    
    if not os.path.exists(image_output):
        try:
            os.makedirs(image_output)
        except OSError as e:
            print(f'Erro ao criar o diretório de saída: {e}')
            return

    # Processar os vídeos
    for video in video_package:
        ef.process_single_video(video, image_output, remove_rats, number_of_frames)