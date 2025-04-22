import json

def gravar_arquivo(arquivo, dados):
    # Serializando o objeto em uma string JSON
    json_str = json.dumps(dados)

    # Gravando a string JSON em um arquivo
    with open("arquivo.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(json_str)
        arquivo.close()

def gravar_arquivo_teclado(arquivo, dados_adicionais):
    dados = {}

    with open("arquivo.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        arquivo.close()

    with open("arquivo.json", "w", encoding="utf-8") as arquivo:
        dados.update(dados_adicionais)
        json_str = json.dumps(dados)
        arquivo.write(json_str)
        arquivo.close()