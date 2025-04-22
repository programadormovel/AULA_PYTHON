import json

def ler_arquivo(arquivo):
    # Gravando a string JSON em um arquivo
    with open("arquivo.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return dados

def ler_arquivo_desestruturado(arquivo):
    # Gravando a string JSON em um arquivo
    with open("arquivo.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return dados