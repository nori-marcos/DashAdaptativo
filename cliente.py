"""
===============================
Cliente DASH (A ser desenvolvido pelos alunos)
===============================

Objetivo:
Implementar um cliente DASH que:

1. Baixe o manifesto do servidor
2. Liste as representações disponíveis
3. Meça a largura de banda atual da rede
4. Escolha a melhor qualidade de vídeo com base na largura de banda
5. Baixe o segmento de vídeo da qualidade escolhida
6. Mostre os dados coletados e salve o segmento localmente

💡 Dica: Utilize Wireshark para capturar os pacotes da execução e observar:
   - A requisição ao manifesto
   - O segmento de vídeo baixado
   - O tempo da transferência para calcular a largura de banda

"""

# Exemplo de biblioteca útil:
# import requests
# import time

# URL do manifesto (use 127.0.0.1 em vez de localhost para evitar erros de permissão)
MANIFEST_URL = "http://127.0.0.1:5000/manifest.mpd"

def baixar_manifesto():
    """
    Função 1: Fazer uma requisição GET ao manifesto
    - Obter o JSON com as representações de vídeo
    - Retornar o dicionário com as informações do manifesto
    """
    pass  # implementar

def medir_largura_de_banda(url_segmento_teste):
    """
    Função 2: Medir a largura de banda
    - Baixar um segmento pequeno (ex: 360p)
    - Medir o tempo da transferência
    - Calcular a largura de banda em Mbps: (tamanho_bytes * 8) / (tempo * 1_000_000)
    - Retornar a largura de banda medida
    """
    pass  # implementar

def selecionar_qualidade(manifesto, largura_banda_mbps):
    """
    Função 3: Escolher a melhor representação
    - Percorrer as representações disponíveis no manifesto
    - Comparar a largura de banda exigida por cada uma com a medida
    - Retornar a melhor representação suportada
    """
    pass  # implementar

def baixar_video(representacao):
    """
    Função 4: Baixar o segmento de vídeo escolhido
    - Fazer uma requisição GET para a URL da representação escolhida
    - Salvar o conteúdo em um arquivo local (ex: video_720p.mp4)
    """
    pass  # implementar

def main():
    """
     Função principal:
    - Chamar as funções na ordem correta
    - Exibir os dados na tela
    - Salvar o vídeo com a qualidade selecionada
    """
    pass  # implementar

if __name__ == '__main__':
    main()
