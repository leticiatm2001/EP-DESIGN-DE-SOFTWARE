#EP - DESING DE SOFTWARE
#EQUIPE: LETÍCIA TELES MACHADO
#DATA: 18/10/2020
import random
from random import randint
#PERGUNTA AO JOGADOR EM QUEM APOSTA E QUANTO APOSTA
aposta = input('Qual a sua aposta? (Jogador/Banco/Empate):  ')
if aposta=="Jogador" or aposta=="Banco" or aposta=="Empate":
    print("Você realizou sua escolha")
else:
    print("Você ainda não fez a sua escolha")
    aposta = input('Qual a sua aposta? (Jogador/Banco/Empate):  ')  
fichas = 100
apostaficha = int(input('Quanto você quer apostar? Voce tem 100 fichas no momento:  '))
if apostaficha > fichas or apostaficha <=0 :
    print ('Me desculpe mas você não tem todas essas fichas ou o valor colocado não é valido')
    apostaficha = int(input('Quanto você quer apostar? Voce tem 100 fichas no momento:  '))


#CARTAS 
espada = [2,3,4,5,6,7,8,9,0,0,0,0,1]
paus = [2,3,4,5,6,7,8,9,0,0,0,0,1]
copas = [2,3,4,5,6,7,8,9,0,0,0,0,1]
ouros = [2,3,4,5,6,7,8,9,0,0,0,0,1]
cartas = espada + paus + copas + ouros

#Embaralhando as cartas
random.shuffle(cartas)

#Sorteando as cartas para o jogador
c1j = random.randint(0,len(cartas))
carta1jogador = cartas[c1j]
c2j= random.randint(0, len(cartas)- carta1jogador)
carta2jogador= cartas[c2j]
somajogador= carta1jogador + carta2jogador

#Sorteando as cartas para o Banco
c1b = random.randint(0,len(cartas)-carta1jogador-carta2jogador)
carta1banco = cartas[c1b]
c2b= random.randint(0, len(cartas)- carta1jogador-carta2jogador-carta1banco)
carta2banco= cartas[c2b]
somabanco= carta1banco + carta2banco