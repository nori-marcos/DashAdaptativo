# Cliente DASH Adaptativo
Nome: Marcos Noriyuki Miyata

## Funcionamento do Cliente
1. O cliente acessa o manifesto que é dispobilizado pelo servidor pela URL: http://127.0.0.1:5000/manifest.mpd
2. O manifesto contém informações sobre as resoluções de vídeo disponíveis (360p, 480p, 720p e 1080p), cada um com banda estimada.
3. O cliente mede a largura de banda fazendo um download de teste da versão 360p e calcula a largura de banda estimada:
   largura_banda = (tamanho_bytes * 8) / (tempo_segundos * 1_000_000)
4. O cliente seleciona a representação com a maior qualidade que não ultrapasse a banda medida.
5. O cliente faz o download do segmento final da qualidade selecionada e salva o arquivo como `video_<qualidade>.mp4`.
6. O cliente exibe mensagens no terminal informando o progresso do download e a qualidade selecionada.

