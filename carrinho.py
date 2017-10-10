import pygame
import math
import json

pygame.init()	#Inicia o pygame

Display = pygame.display.set_mode((1366, 768))	#Criando display
pygame.display.set_caption('Carrinho')	#Nome do display
clock = pygame.time.Clock()	#Criando contador



class carrinho:
	def __init__(self, imagem, pos, dire):
		self.carro_cima = pygame.image.load(r'.\Carro\{0}.png'.format(imagem))
		self.carro_baixo = pygame.transform.rotate(self.carro_cima, 180)
		self.carro_esquerda = pygame.transform.rotate(self.carro_cima, 90)
		self.carro_direita = pygame.transform.rotate(self.carro_cima, -90)
		if dire == 'Cima': self.carro = self.carro_cima
		if dire == 'Baixo': self.carro = self.carro_baixo
		if dire == 'Esquerda': self.carro = self.carro_esquerda
		if dire == 'Direita': self.carro = self.carro_direita
		self.pos = pos
		self.tamanho = self.carro.get_size()
		self.dire = dire
		self.parede = 'Nulo'
		self.municao = 1
		self.tiro1 = False

	def blit(self):

		self.move()
		self.naparede()

		if self.tiro1:
			Display.blit(self.disparo, self.pos_bala1)

		Display.blit(self.carro, (self.pos))

	def move(self):
		if self.dire ==  'Cima':
			self.pos[1] -= 5
			self.carro = self.carro_cima
			self.tamanho = self.carro.get_size()
			if self.parede == 'Horizontal':
				self.pos[0] += self.carro_esquerda.get_size()[0] - self.carro_esquerda.get_size()[1]
				self.parede = 'Nulo'


		if self.dire == 'Baixo':
			self.pos[1] += 5
			self.carro = self.carro_baixo
			self.tamanho = self.carro.get_size()
			if self.parede == 'Horizontal':
				self.pos[0] += self.carro_esquerda.get_size()[0] - self.carro_esquerda.get_size()[1]
				self.parede = 'Nulo'

		if self.dire == 'Esquerda':
			self.pos[0] -= 5
			self.carro = self.carro_esquerda
			self.tamanho = self.carro.get_size()
			if self.parede == 'Vertical':
				self.pos[1] += self.carro_cima.get_size()[1] - self.carro_cima.get_size()[0]
				self.parede = 'Nulo'

		if self.dire == 'Direita':
			self.pos[0] += 5
			self.carro = self.carro_direita
			self.tamanho = self.carro.get_size()
			if self.parede == 'Vertical':
				self.pos[1] += self.carro_cima.get_size()[1] - self.carro_cima.get_size()[0]
				self.parede = 'Nulo'

	def naparede(self):

		if self.pos[0] < margem[0]:
			self.pos[0] = margem[0]

		if self.pos[0] + self.tamanho[0] > tamanho[0] - margem[0]:
			self.pos[0] = tamanho[0] - margem[0] - self.tamanho[0]
			self.parede = 'Horizontal'

		if self.pos[1] < margem[1]:
			self.pos[1] = margem[1]

		if self.pos[1] + self.tamanho[1] > tamanho[1] - margem[1]:
			self.pos[1] = tamanho[1] - margem[1] - self.tamanho[1]
			self.parede = 'Vertical'

	def disparado(self):

		if self.municao == 1:
			self.tiro1_dire = self.dire
			if self.dire == 'Cima':
				self.pos_bala1 = [self.pos[0]+1,self.pos[1]-15]
				self.disparo = disparo
				self.disparo_tamanho = self.disparo.get_size()
				self.tiro1 = True
				self.municao -= 1

			if self.dire == 'Baixo':
				self.pos_bala1 = [self.pos[0]+1,self.tamanho[1]+self.pos[1]+15]
				self.disparo = pygame.transform.rotate(disparo, 180)
				self.disparo_tamanho = self.disparo.get_size()
				self.tiro1 = True
				self.municao -= 1

			if self.dire == 'Esquerda':
				self.pos_bala1 = [self.pos[0]-15, self.pos[1]+1,]
				self.disparo = pygame.transform.rotate(disparo, 90)
				self.disparo_tamanho = self.disparo.get_size()
				self.tiro1 = True
				self.municao -= 1

			if self.dire == 'Direita':
				self.pos_bala1 = [self.tamanho[0]+self.pos[0]+15,self.pos[1]+1]
				self.disparo = pygame.transform.rotate(disparo, -90)
				self.disparo_tamanho = self.disparo.get_size()
				self.tiro1 = True
				self.municao -= 1

	def tiroemfrente(self):

		if self.tiro1:
			if self.tiro1_dire == 'Cima':
				self.pos_bala1[1] -= 7
				if self.pos_bala1[1] < margem[1]:
					self.tiro1 = False

			if self.tiro1_dire == 'Baixo':
				self.pos_bala1[1] += 7
				if self.pos_bala1[1] + self.disparo_tamanho[1] > tamanho[1] - margem[1]:
					self.tiro1 = False

			if self.tiro1_dire == 'Esquerda':
				self.pos_bala1[0] -= 7
				if self.pos_bala1[0] < margem[0]:
					self.tiro1 = False

			if self.tiro1_dire == 'Direita':
				self.pos_bala1[0] += 7
				if self.pos_bala1[0] + self.disparo_tamanho[0] > tamanho[0] - margem[0]:
					self.tiro1 = False
		



rodando = True 
fundo = pygame.image.load(r'.\0.png')

vermelho = carrinho('vermelho', [678,675], 'Cima') 
roxo = carrinho('roxo', [313,443], 'Direita') 

disparo = pygame.image.load(r'.\bullet1.png')

margem = [79,57]
tamanho = fundo.get_size()

while rodando == True:

	Display.blit(fundo, (0,0))
	vermelho.blit()
	roxo.blit()

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			rodando = False
			
		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_w:
				vermelho.dire = 'Cima' 

			if event.key == pygame.K_s:
				vermelho.dire = 'Baixo' 

			if event.key == pygame.K_a:
				vermelho.dire = 'Esquerda' 

			if event.key == pygame.K_d:
				vermelho.dire = 'Direita'

			if event.key == pygame.K_SPACE:
				vermelho.disparado()


			if event.key == pygame.K_UP:
				roxo.dire = 'Cima' 

			if event.key == pygame.K_DOWN:
				roxo.dire = 'Baixo'  

			if event.key == pygame.K_LEFT:
				roxo.dire = 'Esquerda'

			if event.key == pygame.K_RIGHT:
				roxo.dire = 'Direita'

	vermelho.tiroemfrente()

	pygame.display.update()
	clock.tick(60)

pygame.quit() #Encerra o pygame
quit()	#Fecha o jogo