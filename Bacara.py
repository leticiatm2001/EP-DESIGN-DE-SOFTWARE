import random
#PERGUNTA AO JOGADOR EM QUEM APOSTA E QUANTO APOSTA
aposta = input('Qual a sua aposta? (Jogador/Banco/Empate)')
fichas = 100
apostaficha = int(input('Quanto você quer apostar? Voce tem 100 fichas no momento'))
#CARTAS 
espada = [E2,E3,E4,E5,E6,E7,E8,E9,E10,EJ,EQ,EK,EA]
paus = [P2,P3,P4,P5,P6,P7,P8,P9,P10,PJ,PQ,PK,PA]
copas = [C2,C3,C4,C5,C6,C7,C8,C9,C10,CJ,CQ,CK,CA]
ouros = [O2,O3,O4,O5,O6,O7,O8,O9,O10,OJ,OQ,OK,OA]
cartas = [espada, paus, copas, ouros]
random.randint(cartas)
