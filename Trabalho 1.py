from PIL import Image
import numpy as np

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

def Mono_R(imagem):
	width, height = imagem.size
	new = criaImagem(width,height)
	pixels = new.load()

	for k in range(0,width):
			for j in range(0,height):
				pixel = pegaPixel(imagem, k, j)

				r = pixel[0]
				g = pixel[1]
				b = pixel[2]

				#cinza =  

				r = r/2
				g = g/2
				b = b/2

				#r = min(max(r,0),255)
				pixels[k,j] = (int(cinza),int(cinza),int(cinza))

	return new


if __name__ == "__main__":
	imagem = abreImagem("teste.jpg")
	#RGB_YIQ_RGB = RGB_YIQ_RGB(imagem)
	#salvaImagem(RGB_YIQ_RGB, 'saida/RGB-YIQ-RGB.png')
	Mono_R = Mono_R(imagem)
	salvaImagem(Mono_R, 'saida/Mono_R.png')

				