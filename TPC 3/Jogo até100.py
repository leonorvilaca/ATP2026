import random

META = 100
MAXIMO = 10


def ler_inteiro(mensagem):
    """Pede um inteiro ao utilizador até o valor ser válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido! Tens de escrever um número inteiro.")


def escolher_modo():
    print("--- Jogo: Corrida para o 100 ---")
    print("(1) O computador joga primeiro")
    print("(2) Tu jogas primeiro")

    modo = 0
    while modo not in (1, 2):
        modo = ler_inteiro("Escolhe o modo (1 ou 2): ")
        if modo not in (1, 2):
            print("Modo inválido! Tenta novamente.")
    return modo


def jogada_humano(total):
    """Lê a jogada do utilizador (nunca pode ultrapassar o 100)."""
    limite = min(MAXIMO, META - total)
    while True:
        valor = ler_inteiro(f"A tua vez! Escolhe um número de 1 a {limite}: ")
        if 1 <= valor <= limite:
            return valor
        print(f"Jogada inválida! Tem de estar entre 1 e {limite}.")


def jogada_computador(total):
    """
    Estratégia vencedora: deixar sempre o total num valor que dê resto 1
    na divisão por 11 (1, 12, 23, ..., 89, 100).
    Se já estiver numa posição "perdida", joga ao acaso.
    """
    if total % 11 == 1:
        return random.randint(1, min(MAXIMO, META - total))
    return (1 - total) % 11


def jogar(computador_comeca):
    total = 0
    vez_do_computador = computador_comeca

    print("\nO total começa em 0. Quem chegar exatamente a 100 vence!\n")

    while total < META:
        if vez_do_computador:
            jogada = jogada_computador(total)
            total += jogada
            print(f"O computador joga {jogada} -> Total: {total}")
        else:
            jogada = jogada_humano(total)
            total += jogada
            print(f"Jogaste {jogada} -> Total: {total}")

        if total == META:
            if vez_do_computador:
                print("\nO computador venceu!")
            else:
                print("\nParabéns, venceste!")

        vez_do_computador = not vez_do_computador


def main():
    continuar = "s"
    while continuar == "s":
        modo = escolher_modo()
        jogar(computador_comeca=(modo == 1))
        continuar = input("\nQueres jogar outra vez? (s/n): ").strip().lower()
    print("Obrigado por jogares!")


main()
