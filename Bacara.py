#EP - DESING DE SOFTWARE
#EQUIPE: LETÍCIA TELES MACHADO
#DATA: 18/10/2020
import random
from random import randint
#PERGUNTA AO JOGADOR EM QUEM APOSTA E QUANTO APOSTA
fichas = 100
while fichas > 0:
    aposta = input('Qual a sua aposta? (Jogador/Banco/Empate):  ')
    while True:
        if aposta=="Jogador" or aposta=="Banco" or aposta=="Empate":
            print("Você realizou sua escolha")
            break
        else:
            print("Você ainda não fez a sua escolha")
        aposta = input('Qual a sua aposta? (Jogador/Banco/Empate):  ')  

    apostaficha = int(input('Quanto você quer apostar? Voce tem {0} fichas no momento:  '.format(fichas)))
    while True:
        if apostaficha > fichas or apostaficha <=0 :
            print ('Me desculpe mas você não tem todas essas fichas ou o valor colocado não é valido')
            apostaficha = int(input('Quanto você quer apostar? Voce tem {0} fichas no momento:  '.format(fichas)))
        else:
            break

#CARTAS 
    espada = [2,3,4,5,6,7,8,9,0,0,0,0,1]
    paus = [2,3,4,5,6,7,8,9,0,0,0,0,1]
    copas = [2,3,4,5,6,7,8,9,0,0,0,0,1]
    ouros = [2,3,4,5,6,7,8,9,0,0,0,0,1]
    cartas = espada + paus + copas + ouros

#Embaralhando as cartas
    random.shuffle(cartas)

#Sorteando as cartas para o jogador
    c1j = random.randint(0,len(cartas)- 1)
    carta1jogador = cartas[c1j]
    c2j= random.randint(0, len(cartas)-1- carta1jogador)
    carta2jogador= cartas[c2j]
    somajogador= carta1jogador + carta2jogador

#Sorteando as cartas para o Banco
    c1b = random.randint(0,len(cartas)-1-carta1jogador-carta2jogador)
    carta1banco = cartas[c1b]
    c2b= random.randint(0, len(cartas)-1- carta1jogador-carta2jogador-carta1banco)
    carta2banco= cartas[c2b]
    somabanco= carta1banco + carta2banco

#Sorteando as cartas extras
    c3j =random.randint(0, len(cartas)-1- carta1jogador-carta2jogador-carta1banco- carta2banco)
    carta3jogador = cartas[c3j]
    c3b = random.randint(0, len(cartas)-1- carta1jogador-carta2jogador-carta1banco- carta2banco - carta3jogador)
    carta3banco = cartas[c3b]

#Verificando soma
    if somajogador >=10:
        somajogador = somajogador-10
    if somabanco >=10:
        somabanco = somabanco - 10

#Adição da terceira carta se necessário
    if somajogador!=9 and somajogador!=8 and somajogador!=6 and somajogador!=7:
        somajogador += carta3jogador
    if somabanco!=9 and somabanco!=8 and somabanco!=7 and somabanco!=8:
        somabanco += carta3banco    

#Verificando a soma
    if somajogador >=10:
        somajogador = somajogador-10
    if somabanco >=10:
        somabanco = somabanco - 10       

#Mostrando a soma para o jogador
    print("A soma do jogador foi {0}".format(somajogador))
    print("A soma do banco foi {0}".format(somabanco))

#Verificação do resultado
    if somabanco!= somajogador:
        if somabanco > somajogador:
            print("A rodada acabou e o banco venceu")
            if aposta == 'Banco':
                apostaficha = apostaficha *0.95
                fichas = fichas + apostaficha
                print ("Voce acertou e agora está com {0}".format(fichas))
            else:
                fichas = fichas - apostaficha
                print("Você perdeu e agora está com {0}".format(fichas))
        if somajogador > somabanco:
            print("O jogo acabou e o Jogador venceu")
            if aposta == 'Jogador':
                apostaficha=  apostaficha 
                fichas = fichas + apostaficha
                print ("Voce acertou e agora está com {0}".format(fichas))
            else:
                fichas = fichas - apostaficha
                print("Você perdeu e agora está com {0}".format(fichas))

    if somabanco == somajogador:
        print("A rodada acabou e empatou")
        if aposta=='Empate':
            apostaficha = 8* apostaficha
            fichas = fichas + apostaficha
            print ("Voce acertou e agora está com {0}".format(fichas))
        else:
            fichas = fichas - apostaficha
            print("Você perdeu e agora está com {0}".format(fichas)) 
#Perguntar se ainda quer jogar (se tiver fichas)
    if fichas > 0:
        continuar = input("Deseja continuar jogando? (Sim/Nao). Você ainda possui {0} fichas:  ".format(fichas))
        while continuar != "Sim" and continuar!="Nao":
            print("Resposta invalida")
            continuar = input("Deseja continuar jogando? (Sim/Nao). Você ainda possui {0} fichas:  ".format(fichas))
        if continuar == "Nao":
            print ("Acabou, Obrigada por jogar!")
            break  
        else:
            True 
    elif fichas == 0:
        print ('Voce não possui mais fichas, Obrigada por Jogar!')