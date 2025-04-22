from gravar_arquivo import gravar_arquivo
from gravar_arquivo import gravar_arquivo_teclado
from ler_arquivo import ler_arquivo
from ler_arquivo import ler_arquivo_desestruturado

def menu():
    print("=== Menu de Opções ===")
    print("1. Criação e inicialização do arquivo")
    print("2. Leitura do arquivo gravado")
    print("3. Leitura dos dados desestruturados")
    print("4. Gravar dados do teclado no arquivo")
    print("5. Sair")
    escolha = input("Escolha uma opção (1-5): ")

    return escolha

def opcao_1():
    print("Gravando arquivo com dados em formato JSON.")
    gravar_arquivo("arquivo.json", {"title":"Opção 1"})

def opcao_2():
    print("Lendo arquivo e apresentando na tela.")
    dados_arquivo = ler_arquivo("arquivo.json")
    print(dados_arquivo)

def opcao_3():
    print("Lendo arquivo com dados desestruturados.")
    dados_arquivo = ler_arquivo_desestruturado("arquivo.json")
    print(dados_arquivo['title'])
    if 'dados' in dados_arquivo:3
        print(dados_arquivo['dados'])

def opcao_4():
    dados_teclado = input("Digite algum texto para ser gravado no arquivo: ")
    print("Gravando arquivo com dados em formato JSON...")
    gravar_arquivo_teclado("arquivo.json", {"dados": dados_teclado})

def main():
    while True:
        escolha = menu()

        if escolha == "1":
            opcao_1()
        elif escolha == "2":
            opcao_2()
        elif escolha == "3":
            opcao_3()
        elif escolha == "4":
            opcao_4()
        elif escolha == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        


if __name__ == "__main__":
    main()