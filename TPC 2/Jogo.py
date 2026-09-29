
# Modalidade 1: Computador pensa num número (0 a 100) e o utilizador tenta adivinhar

import random

def mod1():
    x = random.randint(0, 100)
    palpite = int(input("Advinha o número (0-100): "))
    tentativas = 0

    while palpite != x:
        if palpite > x:
            print("O número que pensei é menor")
        else:
            print("O número que pensei é maior")
        
        palpite = int(input("Tenta outra vez: "))
        tentativas = tentativas + 1

    print("Acertou")
    print(f"Usaste {tentativas} tentativas para acertar")




# Modalidade 2: O utilizador pensa num número (0 a 100) e o computador tenta adivinhar

def mod2():
 
 palpite= random.randint (0,100)

 resposta= input(f"O meu {palpite} é maior, menor ou certo?")
 tentativas= 1

 while resposta != "certo":
    if resposta == "maior":
      palpite= palpite - 1

    else:
      palpite= palpite + 1

   
      
    resposta= input(f"O meu {palpite} é maior, menor ou certo?")
    tentativas= tentativas + 1


 print(f"Acertei, usei {tentativas} para acertar.")


# Modo principal: Para escolher qual modalidade queremos

print("Escolhe a modalidade do jogo:")
print("1- O computador pensa num número, tu adivinhas")
print("2- Tu pensas num número, o computador adivinha")

escolha= input("Escreve 1 ou 2: ")

if escolha=="1":
   mod1 ()
else:
   mod2()






