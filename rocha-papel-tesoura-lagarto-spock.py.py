# Scprit feito por Matheus Silva
# 09/02/2018 Hs 22:30
# Rocha,papel,tesoura,com implementação largato,spock
# Implementado ! ! !  ... Só Design para dar vida no projeto agora... ! ! !
# codigo no meu Git-hub.

import random

escolha = ["rocha","papel","tesoura","lagarto","spock"]

print("Rocha esmaga Tesoura,Tesoura corta Papel, Papel cobre Rocha ")
print("Rocha esmaga Lagarto, Lagarto envenena Spock, Spock esmaga Rocha")
print("Tesoura decapita Lagarto, Lagarto come Papel, Papel refuta Spock, Spock refuta Rocha")

jogador = input("Escolha sua jogada , ROCHA , PAPEL , TESOURA , LAGARTO , SPOCK ou press [ENTER]:")
while jogador != "":
    jogador = jogador.lower()
    computador = random.choice(escolha)
    print("Voce jogou: " +jogador+ ". O computador jogou: " +computador+ ".")

    if jogador == computador:
        print("Oou ouve empate.")

 # JOGADA 1 rocha contra tesoura tesoura contra rocha
    elif jogador == "rocha":
        if computador == "tesoura":
            print("Voce ganhou:")
        else:
            print("computador ganhou de voce seu noob !!! ")
 # JOGADA 2 papel contra rocha rocha contra papel
    elif jogador == "papel":
        if computador == "rocha":
            print("Voce ganhou:")
        else:
            print("computador ganhou de voce seu noob !!! ")
 # JOGADA 3 tesoura contra papel papel contra tesoura
    elif jogador == "tesoura":
        if computador == "papel":
            print("Voce ganhou:")
        else:
            print("computador ganhou de voce seu noob !!! ")
 # JOGADA 4
    elif jogador == "rocha":
        if computador == "lagarto":
            print("Voce ganhou:")
        else:
            print("computador ganhou de voce seu noob !!! ")
 # JOGADA 5
    elif jogador == "lagarto":
        if computador == "spock":
            print("Voce ganhou:")
        else:
            print("computador ganhou de voce seu noob !!! ")
 # JOGADA 6
    elif jogador == "spock":
        if computador == "tesoura":
            print("Voce ganhou:")
        else:
            print("computador ganhou de voce seu noob !!! ")
 # JOGADA 7
    elif jogador == "tesoura":
        if computador == "lagarto":
            print("Voce ganhou:")
        else:
            print("computador ganhou de voce seu noob !!! ")
 # JOGADA 8
    elif jogador == "lagarto":
        if computador == "papel":
            print("Voce ganhou:")
        else:
            print("computador ganhou de voce seu noob !!! ")
  # JOGADA 9
    elif jogador == "papel":
        if computador == "spock":
            print("Voce ganhou:")
        else:
            print("computador ganhou de voce seu noob !!! ")
  # JOGADA 10
    elif jogador == "spock":
        if computador == "rocha":
            print("Voce ganhou:")
        else:
            print("computador ganhou de voce seu noob !!! ")
    else:
        print("Ajuste o codigo:")
    print()
    jogador = input("Escolha sua jogada ROCHA < PAPEL > TESOURA:")
