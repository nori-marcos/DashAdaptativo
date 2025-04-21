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
import requests
import time

# URL do manifesto (use 127.0.0.1 em vez de localhost para evitar erros de permissão)
MANIFEST_URL = "http://127.0.0.1:5000/manifest.mpd"

def baixar_manifesto():
    """
    Função 1: Fazer uma requisição GET ao manifesto
    - Obter o JSON com as representações de vídeo
    - Retornar o dicionário com as informações do manifesto
    """
    try:
        resposta = requests.get(MANIFEST_URL)
        resposta.raise_for_status()
        manifesto = resposta.json()
        return manifesto["video"]["representations"]
    except Exception  as e:
        print(f"Erro ao baixar o manifesto: {e}")
        return None

def medir_largura_de_banda(url_segmento_teste):
    """
    Função 2: Medir a largura de banda
    - Baixar um segmento pequeno (ex: 360p)
    - Medir o tempo da transferência
    - Calcular a largura de banda em Mbps: (tamanho_bytes * 8) / (tempo * 1_000_000)
    - Retornar a largura de banda medida
    """
    try:
        inicio = time.perf_counter()
        resposta = requests.get(url_segmento_teste)
        fim = time.perf_counter()
        tempo = fim - inicio
        tamanho_bytes = len(resposta.content)
        largura_banda_mbps = (tamanho_bytes * 8) / (tempo * 1_000_000)
        print(f"Largura de banda estimada: {largura_banda_mbps:.2f} Mbps")
        return largura_banda_mbps
    except Exception as e:
        print(f"Erro ao medir largura de banda: {e}")
        return 0

def selecionar_qualidade(manifesto, largura_banda_mbps):
    """
    Função 3: Escolher a melhor representação
    - Percorrer as representações disponíveis no manifesto
    - Comparar a largura de banda exigida por cada uma com a medida
    - Retornar a melhor representação suportada
    """
    melhor = None
    for rep in manifesto:
        if rep["bandwidth"] <= largura_banda_mbps:
            melhor = rep
    if melhor:
        print(f"Qualidade selecionada: {melhor['id']} ({melhor['bandwidth']} Mbps)")
    else:
        melhor = manifesto[0]
        print(f"Nenhuma qualidade compatível. Selecionado padrão: {melhor['id']}")
    return melhor

def baixar_video(representacao):
    """
    Função 4: Baixar o segmento de vídeo escolhido
    - Fazer uma requisição GET para a URL da representação escolhida
    - Salvar o conteúdo em um arquivo local (ex: video_720p.mp4)
    """
    try:
        resposta = requests.get(representacao["url"])
        nome_arquivo = f"video_{representacao['id']}.mp4"
        with open(nome_arquivo, "wb") as f:
            f.write(resposta.content)
        print(f"Vídeo salvo como: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao baixar vídeo: {e}")

def main():
    """
     Função principal:
    - Chamar as funções na ordem correta
    - Exibir os dados na tela
    - Salvar o vídeo com a qualidade selecionada
    """
    print("Baixando manifesto...")
    representacoes = baixar_manifesto()
    if not representacoes:
        return

    print("\nMedição de largura de banda...")
    url_360p = next((rep["url"] for rep in representacoes if rep["id"] == "360p"), None)
    if not url_360p:
        print("Erro: representação 360p não encontrada.")
        return

    largura_banda = medir_largura_de_banda(url_360p)

    print("\nSelecionando melhor qualidade...")
    melhor_rep = selecionar_qualidade(representacoes, largura_banda)

    print("\nBaixando segmento final...")
    baixar_video(melhor_rep)

if __name__ == '__main__':
    main()
