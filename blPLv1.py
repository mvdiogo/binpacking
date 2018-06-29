#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Disciplina de Projeto e Análise de Algoritmos
#
# Professor: Valdisio
#
# Autores: Marcus
#
# Metaheurística Busca Local - bin packing
#
# Objetivo: menor quantidade de cestos possível
# exemplo: python bl.py nomedoarquivoaimportar.txt
# começo da programação
#Importantando sys para importação e conversão dos dados
import time
inicio = time.time()
import sys
import itertools
import random
from random import randint
#Criação das variaveis
peso = []
bolsa = [] #soma de itens
bolsa_otima=[]
tempo = 0 #duração  código
tamanho_bolsa = 9999999 #flag para comparar antigo com novo
lista_bolsa =[[]] #itens em cada bolsa
lista_bolsa_otima =[[]] 
nb=1 #adicionar novas bolsas
somar = 0  #soma dos valores na bolsa
somar1 = 0 #soma dos valores totais
i=0 #index peso
j = 0#index bolsa
quant_bolsa=0
# codificação para importação dos arquivos de texto dependendo do argumento
print('Para rodar o algorítimo da forma correta digite: ')
print('python3 bl.py nomearquivo.txt')
nome_arquivo=sys.argv[1]
with open(sys.argv[1]) as file:
	lines = file.read().splitlines()
	capacidade = (int(lines[0].split(" ")[1].rstrip()))
	itens = (int(lines[0].split(" ")[0].rstrip()))
	lines = lines[1:]#cortar primeira linha
	for line in lines:#range(len(lines)): for i in range(itens):
		peso.append((lines[i].split(" "))) #atribuir a variavel os valores dos pesos extend?
		i +=1
	peso = list(itertools.chain(*peso)) #arrumar para apenas uma lista
	peso = filter(None,peso) #eliminar os vazios
	peso = list(map(int,peso)) #converter para inteiro
file.close()

for element in peso:
	quant_bolsa+=element
quant_bolsa = quant_bolsa//capacidade

itens = len(peso)

w=0
m=[]
bolsa=[]
lista_bolsa = []
bolsa.append(0)
lista_bolsa.append([])
i=0

minimo=0
laco =0
s=0 #
j=0#teto bolsa
n=0

peso = sorted(peso, reverse=True)

top=1
for w in range(0,top):#top):
	m=random.sample(range(0,itens),itens)
	s=0
	bolsa=[]
	bolsa.append(0)
	lista_bolsa = [[]]
	i=0
	j=0
	k = (m[i])
	while capacidade <int(peso[i]): #nao cabe
		i+=1

	while i<itens:

		while capacidade*.51 <= (int(peso[i])): #enche a mochila
			bolsa[j] +=peso[i]
			lista_bolsa[j].append(peso[i])
			j+=1
			bolsa.append(0)
			lista_bolsa.append([])
			i+=1
		laco=0
		while laco == 0:
			for s in range(0,j+1): #procura bolsa
				if peso[i] == (capacidade - bolsa[s]) and laco ==0:
					bolsa[s] += peso[i]
					lista_bolsa[s].append(peso[i])
					#print("best fit")
					laco =1
				elif peso[i] < (capacidade - bolsa[s])and laco ==0:
					bolsa[s] += peso[i]
					lista_bolsa[s].append(peso[i])
					#print("tem vaga bolsa")
					laco =1
				elif peso[i] > (capacidade - bolsa[s])and laco ==0:
					if j == s:
						#print("add bolsa")
						j+=1
						s+=1
						bolsa.append(peso[i])
						lista_bolsa.append([])
						lista_bolsa[s].append(peso[i])
						laco=1	
		i+=1
	if len(lista_bolsa) < tamanho_bolsa:
		bolsa_otima = bolsa
		bolsa_otima_guloso = bolsa
		lista_bolsa_otima_guloso = lista_bolsa 
		lista_bolsa_otima = lista_bolsa 
		tamanho_bolsa = len(lista_bolsa_otima)
		print('Tamanho bolsa Best Fit= {}'.format(len(lista_bolsa_otima)))
		print('Teto minimo= {}'.format(quant_bolsa))
		fim=time.time()
		print('Tempo total em segundos= {}'.format(fim-inicio))


bolsa = bolsa_otima
lista_bolsa = lista_bolsa_otima
#	começa reorganizar
j=0
pl=1

interacoes = 1000000
while pl < interacoes:
	j=randint(0,len(bolsa)-1)	#bolsa inicio
	y=randint(0,len(bolsa)-1)#bolsa fim ver ordenar o tirar o min
	z=randint(0,len(lista_bolsa[j])-1)	#item inicio
	w=randint(0,len(lista_bolsa[y])-1)	#item fim
	if  bolsa[j] == capacidade:
		j+=1
	else:
		if lista_bolsa[y][w]  <= capacidade - bolsa[j]:#inserssão ulti -item>cap-bolsa
			bolsa[j] += lista_bolsa[y][w]
			bolsa[y] -= lista_bolsa[y][w]
			lista_bolsa[j].append(lista_bolsa[y][w])
			lista_bolsa[y].remove(lista_bolsa[y][w])
			if 0 in bolsa:
				#print(bolsa)
				#print(lista_bolsa)
				print("--------------Diminuiu o tamanho da bolsa ----------------------")
				bolsa = [x for x in bolsa if x is not 0]

				lista_bolsa = [x for x in lista_bolsa if x != []]
		elif lista_bolsa[y][w] - lista_bolsa[j][z] <= capacidade - bolsa[j]:#substituição ulti -item>cap-bolsa
			if  lista_bolsa[j][z] - lista_bolsa[y][w]  <= capacidade - bolsa[y]:
				bolsa[j] += lista_bolsa[y][w]
				bolsa[y] -= lista_bolsa[y][w]
				bolsa[j] -= lista_bolsa[j][z]
				bolsa[y] += lista_bolsa[j][z]
				lista_bolsa[j].append(lista_bolsa[y][w])
				lista_bolsa[y].remove(lista_bolsa[y][w])
				lista_bolsa[y].append(lista_bolsa[j][z])
				lista_bolsa[j].remove(lista_bolsa[j][z])
	pl+=1


bolsa_otima = bolsa
lista_bolsa_otima = lista_bolsa

for item in peso:
	somar1 += int(item)

#exibir os resultados

with open('rep_bestfitcominteações', 'a') as arq:
	arq.write('Guloso best fit com interação de troca de itens para diminuir bolsa ')
	arq.write('\n') 
	arq.write('Nome do arquivo ={}'  .format(nome_arquivo))
	arq.write('\n') 
	arq.write('Capacidade do bin = {}'  .format(capacidade) )
	arq.write('\n') 
	arq.write('Quantidade de interações = {}'  .format(interacoes))
	arq.write('\n') 
	arq.write('Teto mínimo= {}'  .format(quant_bolsa))
	arq.write('\n') 
	arq.write('Quant bolsas ótimo guloso = {}' .format(len(bolsa_otima_guloso)))
	arq.write('\n') 
	arq.write( 'Quant bolsas ótimo  = {}' .format(len(bolsa_otima)))
	arq.write('\n') 
	arq.write('Quantidade de itens = {}' .format(len(peso)))
	arq.write('\n') 
	arq.write('Soma itens = {}' .format(somar1))
	fim=time.time()
	arq.write('\n') 
	arq.write('Tempo total em segundos= {}'.format(fim-inicio))
	arq.write('\n') 
	arq.write('Peso dos itens das bolsas= {}'.format(bolsa))
	arq.write('\n') 
	arq.write('Lista itens bolsa= {}'.format(lista_bolsa))
	arq.write('\n') 
	arq.write('----------------------------------')

#para rodar varios bins python3 blPLv1.py n50C1000A.txt&&python3 blPLv1.py n50C1000B.txt&&python3 blPLv1.py n100C1000A.txt&&python3 blPLv1.py n100C1000B.txt&&python3 blPLv1.py n200C1000A.txt&&python3 blPLv1.py n200C1000B.txt&&python3 blPLv1.py n500C1000.txt&&python3 blPLv1.py n750c1000.txt&&python3 blPLv1.py n1500c500.txt&&n500C1000
