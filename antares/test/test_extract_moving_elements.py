# test/extract_moving_elements.py

import time

from libs.antares.pre_aquisition.extract_frames import frames_generate

# Início do contador de tempo
start_time = time.time()

videos_directory = "G:/.shortcut-targets-by-id/1IS6JRRPTtFODpC4w7VjAxRfsFw2A_qCL/Lab eletrofisio ISD/COMPORTAMENTO/Object_Recognition/Exp_35_MRO_ contextos_dicas/Exp 35 - rodada 2 - analisados"
image_directory = "C:/Users/ariog/Downloads/test_Antares"
remove_rats = 1

frames_generate(videos_directory, image_directory, remove_rats)

# Fim do contador de tempo
end_time = time.time()

# Calcular e imprimir o tempo total
print(f"Tempo de execução: {end_time - start_time} segundos")
time = end_time - start_time