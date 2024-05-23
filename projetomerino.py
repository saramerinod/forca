from pathlib import Path
caminho ="./rank.txt"
import random

def escolher_palavra():
    with open("word.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()
    return random.choice(palavras)

def iniciar_jogo():
    palavra = escolher_palavra()
    letras_usuario = []
    chances = 5
    pontuacao = 0
    ganhou = False

    nome=str(input("digite seu nome: "))

    with open("rank.txt", "r+") as ranklist:
        cont_ranklist = ranklist.readlines()

        if len(cont_ranklist) == 0:
            ranklist.write(f"{nome} {pontuacao}")

    while True:
        for letra in palavra:
            if letra.lower() in letras_usuario:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print(f"Você tem {chances} chances.")
        tentativa = input("Escolha uma letra para adivinhar: ")
        letras_usuario.append(tentativa.lower())
        if tentativa.lower() not in palavra.lower():
            chances -= 1
        ganhou = True
        for letra in palavra:
            if letra.lower() not in letras_usuario:
                ganhou = False
        if chances == 0 or ganhou:
            break

    if ganhou:
        print(f"Você ganhou. A palavra era: {palavra}")
        pontuacao += 1
        with open(caminho, "r+") as rank:
            conteudo_rank = rank.readlines()

            encontrado = False
            for i, linha in enumerate(conteudo_rank):
                nick, pontos = linha.strip().split()

                if nick == nome:
                    encontrado = True
                    pontos = int(pontos) + pontuacao
                    conteudo_rank[i] = f"{nick} {pontos}\n"

            if not encontrado:
                conteudo_rank.append(f"{nome} {pontuacao}\n")

            rank.seek(0)
            rank.writelines(conteudo_rank)
            rank.truncate()
    else:
        print(f"Você perdeu. A palavra era: {palavra}")

def mostrar_creditos():
    print("Jogo da Forca")
    print("Desenvolvido por [Merino]")

def menu():
    while True:
        print("\nMenu:")
        print("1. Iniciar Jogo")
        print("2. Créditos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            iniciar_jogo()
        elif escolha == "2":
            mostrar_creditos()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()