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
#Valores das cartas
E2= 2
E3=3 
E4=4 
E5=5 
E6=6 
E7=7 
E8=8 
E9=9 
E10=0
EJ=0 
EQ=0 
EK=0 
EA=1
P2=2 
P3=3
P4=4
P5=5
P6=6
P7=7
P8=8
P9=9
P10=0
PJ=0
PQ=0
PK=0
PA=1
C2=2
C3=3
C4=4
C5=5
C6=6
C7=7
C8=8
C9=9
C10=0
CJ=0
CQ=0
CK=0
CA=1
O2=2
O3=3
O4=4
O5=5
O6=6
O7=7
O8=8
O9=9
O10=0
OJ=0
OQ=0
OK=0
OA=1
