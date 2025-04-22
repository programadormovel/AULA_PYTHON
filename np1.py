from gravar_arquivo import gravar_arquivo
from ler_arquivo import ler_arquivo
from ler_arquivo import ler_arquivo_desestruturado

def menu():
    print("=== Menu de Opções ===")
    print("1. Opção 1")
    print("2. Opção 2")
    print("3. Opção 3")
    print("4. Sair")
    escolha = input("Escolha uma opção (1-4): ")

    return escolha

def opcao_1():
    print("Gravando arquivo com dados em formato JSON.")
    gravar_arquivo("arquivo.json", {"title":"Opção 1"})

def opcao_2():
    print("Lendo arquivo e apresentando na tela.")
    dados = ler_arquivo("arquivo.json")
    print(dados)

def opcao_3():
    print("Lendo arquivo com dados desestruturados.")
    dados = ler_arquivo_desestruturado("arquivo.json")
    print(dados['title'])

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
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        


if __name__ == "__main__":
    main()