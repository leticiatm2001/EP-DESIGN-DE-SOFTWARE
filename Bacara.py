import random
#PERGUNTA AO JOGADOR EM QUEM APOSTA E QUANTO APOSTA
aposta = input('Qual a sua aposta? (Jogador/Banco/Empate):  ')
if aposta=="Jogador" or aposta=="Banco" or aposta=="Empate":
    print("Você realizou sua escolha")
else:
    print("Você ainda não fez a sua escolha")
    aposta = input('Qual a sua aposta? (Jogador/Banco/Empate):  ')  
fichas = 100
apostaficha = int(input('Quanto você quer apostar? Voce tem 100 fichas no momento'))
if apostaficha > fichas:
    print ('Me desculpe mas você não tem todas essas fichas')
    apostaficha = int(input('Quanto você quer apostar? Voce tem 100 fichas no momento'))


#CARTAS 
espada = [2,3,4,5,6,7,8,9,0,0,0,0,1]
paus = [2,3,4,5,6,7,8,9,0,0,0,0,1]
copas = [2,3,4,5,6,7,8,9,0,0,0,0,1]
ouros = [2,3,4,5,6,7,8,9,0,0,0,0,1]
cartas = [espada, paus, copas, ouros]

#Começo do jogo
random.shuffle(cartas)
