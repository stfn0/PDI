 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import sys

import numpy as np
from PIL import Image

##########################
#Primeiro Trabalho de PDI#
##########################


def abreImagem(destino):
	imagem = Image.open(destino)
	return imagem

def salvaImagem(imagem, destino):
	imagem.save(destino, 'png')

def criaImagem(i,j):
	imagem = Image.new("RGB",(i,j))
	return imagem

def pegaPixel(imagem,i,j):
	width, height = imagem.size
	if((i>width) or (j>height)):
		return None
	pixel = imagem.getpixel((i,j))
	return pixel

#1.1 - Conversão RGB-YIQ-RGB
def RGB_YIQ_RGB(imagem):
	width, height = imagem.size
	new = criaImagem(width,height)
	pixels = new.load()

	for k in range(0,width):
		for j in range(0,height):

			pixel = pegaPixel(imagem, k, j)

			r = pixel[0]
			g = pixel[1]
			b = pixel[2]
			#RGB PARA YIQ
			y = r * 0.299 + g * 0.587 + b * 0.114
			i = r * 0.596 - g * 0.275 - b * 0.321
			q = r * 0.212 - g * 0.523 + b * 0.311
			#YIQ PARA RGB
			r = 1*y + 0.956*i + 0.621*q
			g = 1*y - 0.272*i - 0.647*q
			b = 1*y - 1.105*i + 1.702*q

			#Tratando os limites
			r = min(max(r,0),255)
			g = min(max(g,0),255)
			b = min(max(b,0),255)

			#print(r,g,b)
			pixels[k,j] = (int(r),int(g),int(b))

	return new

#1.2 - Exibição de bandas individuais (R, G e B) como imagens monocromáticas ou coloridas (em tons de R, G ou B, respectivamente)

def Mono(imagem):
	width, height = imagem.size
	new = criaImagem(width,height)
	pixels = new.load()

	for k in range(0,width):
		for j in range(0,height):

			pixel = pegaPixel(imagem, k, j)

			r = pixel[0]
			g = pixel[1]
			b = pixel[2]

			r = r/2
			g = g/2
			b = b/2

			cinza = r * 0.299 + g * 0.587 + b * 0.114 

			#r = min(max(r,0),255)
			pixels[k,j] = (int(cinza),int(cinza),int(cinza))

	return new

def Banda_R(imagem):
	width, height = imagem.size
	new = criaImagem(width,height)
	pixels = new.load()

	for k in range(0,width):
		for j in range(0,height):

			pixel = pegaPixel(imagem, k, j)

			r = pixel[0]
			g = pixel[1]
			b = pixel[2]
			
			g = 0
			b = 0
	
			pixels[k,j] = (int(r),int(g),int(b))

	return new

def Banda_G(imagem):
	width, height = imagem.size
	new = criaImagem(width,height)
	pixels = new.load()

	for k in range(0,width):
			for j in range(0,height):
				pixel = pegaPixel(imagem, k, j)

				r = pixel[0]
				g = pixel[1]
				b = pixel[2]
				
				r = 0
				b = 0
		
				pixels[k,j] = (int(r),int(g),int(b))

	return new

def Banda_B(imagem):
	width, height = imagem.size
	new = criaImagem(width,height)
	pixels = new.load()

	for k in range(0,width):
		for j in range(0,height):

			pixel = pegaPixel(imagem, k, j)

			r = pixel[0]
			g = pixel[1]
			b = pixel[2]
			
			r = 0
			g = 0

			pixels[k,j] = (int(r),int(g),int(b))

	return new

def Negativo(imagem):
	width, height = imagem.size
	new = criaImagem(width,height)
	pixels = new.load()

	for k in range(0,width):
		for j in range(0,height):

			pixel = pegaPixel(imagem, k, j)

			r = pixel[0]
			g = pixel[1]
			b = pixel[2]
			
			r = (-1*r+255)
			g = (-1*g+255)
			b = (-1*b+255)

			pixels[k,j] = (int(r),int(g),int(b))

	return new

#1.4 - Brilho Aditivo
def BrilhoAditivo(imagem,c):
	width, height = imagem.size
	new = criaImagem(width,height)
	pixels = new.load()

	for k in range(0,width):
		for j in range(0,height):

			pixel = pegaPixel(imagem, k, j)

			r = pixel[0]
			g = pixel[1]
			b = pixel[2]

			r = r+c
			g = g+c
			b = b+c

			#Tratando os limites
			r = min(max(r,0),255)
			g = min(max(g,0),255)
			b = min(max(b,0),255)

			pixels[k,j] = (int(r),int(g),int(b))

	return new

#1.5 - Brilho Multiplicativo
def BrilhoMultiplicativo(imagem,d):
	width, height = imagem.size
	new = criaImagem(width,height)
	pixels = new.load()

	for k in range(0,width):
		for j in range(0,height):

			pixel = pegaPixel(imagem, k, j)

			r = pixel[0]
			g = pixel[1]
			b = pixel[2]

			r = r*d
			g = g*d
			b = b*d

			#Tratando os limites
			r = min(max(r,0),255)
			g = min(max(g,0),255)
			b = min(max(b,0),255)

			pixels[k,j] = (int(r),int(g),int(b))

	return new






#1.8 - Limiarização com limiar m escolhido pelo usuário.

def Limiarizacao(imagem,m):
	width, height = imagem.size
	new = criaImagem(width,height)
	pixels = new.load()

	for k in range(0,width):
		for j in range(0,height):

			pixel = pegaPixel(imagem, k, j)

			r = pixel[0]
			g = pixel[1]
			b = pixel[2]
			# result = (false,true)[condition]
			r = (255,0)[r<=m]
			g = (255,0)[g<=m]
			b = (255,0)[b<=m]

			pixels[k,j] = (int(r),int(g),int(b))

	return new



if __name__ == "__main__":

		fileInput = sys.argv[1]
		fileOutput = sys.argv[2]
		imagem = abreImagem(fileInput)

		MenuSelect = input(
		" _____                                           _          ____  _     _ _       _      _        _                           \n"
		+"|  _  |___ ___ ___ ___ ___ ___ ___ _____ ___ ___| |_ ___   |    \|_|___|_| |_ ___| |   _| |___   |_|_____ ___ ___ ___ ___ ___ \n"
		+"|   __|  _| . |  _| -_|_ -|_ -| .'|     | -_|   |  _| . |  |  |  | | . | |  _| .'| |  | . | -_|  | |     | .'| . | -_|   |_ -|\n"
		+"|__|  |_| |___|___|___|___|___|__,|_|_|_|___|_|_|_| |___|  |____/|_|_  |_|_| |__,|_|  |___|___|  |_|_|_|_|__,|_  |___|_|_|___|\n"
		+"                                                                   |___|                                     |___|            \n\n\n\n"		
		+"\t+---+-------------------------------------------------------+\n"
		+"\t|   |           Digite o numero da opção desejada           |\n"
		+"\t+---+-------------------------------------------------------+\n"
		+"\t| 1 | RGB-YIQ-RGB                                           |\n"
		+"\t| 2 | Mono                                                  |\n"
		+"\t| 3 | Banda R                                               |\n"
		+"\t| 4 | Banda G                                               |\n"
		+"\t| 5 | Banda B                                               |\n"
		+"\t| 6 | Negativo                                              |\n"
		+"\t| 7 | Brilho Aditivo                                        |\n"
		+"\t| 8 | Brilho Multiplicativo                                 |\n"
		+"\t| 9 | Limiarização                                          |\n"
		+"\t+---+-------------------------------------------------------+\n"
		)
		if(MenuSelect == '1'):
			#RGB_YIQ_RGB
			RGB_YIQ_RGB = RGB_YIQ_RGB(imagem)
			salvaImagem(RGB_YIQ_RGB, 'saida/'+fileOutput+'_RGB-YIQ-RGB.png')
		elif(MenuSelect == '2'):
			#Monocromática
			Mono = Mono(imagem)
			salvaImagem(Mono, 'saida/'+fileOutput+'_Mono.png')
		elif(MenuSelect == '3'):
			#Banda Red
			Banda_R = Banda_R(imagem)
			salvaImagem(Banda_R,'saida/'+fileOutput+'_Banda_R.png')
		elif(MenuSelect == '4'):
			#Banda Green
			Banda_G = Banda_G(imagem)
			salvaImagem(Banda_G,'saida/'+fileOutput+'_Banda_G.png')
		elif(MenuSelect == '5'):
			#Banda Blue
			Banda_B = Banda_B(imagem)
			salvaImagem(Banda_B,'saida/'+fileOutput+'_Banda_B.png')
		elif(MenuSelect == '6'):
			#Negativo
			Negativo = Negativo(imagem)
			salvaImagem(Negativo,'saida/'+fileOutput+'_Negativo.png')
		elif(MenuSelect == '7'):
			#Brilho Aditivo
			c = int(input("Valor do aditivo: "))
			BrilhoAditivo = BrilhoAditivo(imagem,c)
			salvaImagem(BrilhoAditivo,'saida/'+fileOutput+'_BrilhoAditivo_'+str(c)+'.png')
		elif(MenuSelect == '8'):
			#Brilho Multiplicativo
			d = int(input("Valor do multiplicativo: "))
			BrilhoAditivo = BrilhoMultiplicativo(imagem,d)
			salvaImagem(BrilhoAditivo,'saida/'+fileOutput+'_brilhoMultiplicativo_'+str(d)+'.png')
		elif(MenuSelect == '9'):
			#Limiarização
			m = int(input("Valor do limiar: "))
			Limiarizacao = Limiarizacao(imagem,m)
			salvaImagem(Limiarizacao,'saida/'+fileOutput+'_LimiarM_'+str(m)+'.png')

		print("Filtro aplicada com sucesso")