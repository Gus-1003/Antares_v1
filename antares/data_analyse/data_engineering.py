import pandas as pd
import os
import glob

def data_engineering(dir_input, dir_output):
    """
    Lê e concatena todos os arquivos CSV de uma pasta em um único DataFrame e salva o resultado.

    Args:
        dir_input (str): Caminho do diretório contendo os arquivos CSV.
        dir_output (str): Caminho do diretório onde o CSV final será salvo.

    Returns:
        None
    """
    dados_gerais = []

    # Encontrar todos os arquivos CSV no diretório de entrada
    data_pack = glob.glob(os.path.join(dir_input, '*_process_segmentaded.csv'))
  
    print("Quantidade de arquivos CSV´s encontrados:", len(data_pack))

    # Ler e armazenar cada CSV em uma lista de DataFrames
    for frame_data in data_pack:
        try:
            df = pd.read_csv(frame_data)  # Lê o CSV como DataFrame
            dados_gerais.append(df)  # Adiciona o DataFrame à lista
        except Exception as e:
            print(f"Erro ao ler o arquivo {frame_data}: {e}")

    # Concatenar todos os DataFrames da lista
    if dados_gerais:
        all_data = pd.concat(dados_gerais, ignore_index=True)

        # Criar o diretório de saída, se não existir
        os.makedirs(dir_output, exist_ok=True)

        # Caminho do arquivo CSV de saída
        csv_file_path = os.path.join(dir_output, 'all_objects.csv')

        # Ordenar os dados, se as colunas 'id' e 'day' existirem
        if 'id' in all_data.columns:
            all_data_sorted = all_data.sort_values(by=['id'])
        else:
            print("Coluna 'id' não encontrada. Salvando sem ordenação.")
            all_data_sorted = all_data

        # Salvar o DataFrame final como CSV
        all_data_sorted.to_csv(csv_file_path, index=False)

        print(f'DataFrame mesclado salvo como CSV em {csv_file_path}.')
    else:
        print("Nenhum dado encontrado para processar.")