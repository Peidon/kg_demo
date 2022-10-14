# coding: utf-8
from pyfasttext import FastText

def text():
	model = FastText('wiki.zh.bin')
	print('load over..')
	print(model.nearest_neighbors('桃', k=5))
		
#text()