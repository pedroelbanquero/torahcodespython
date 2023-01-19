
import argparse
import os

import scipy.stats as ent
from deep_translator import GoogleTranslator
import string
import random
import sys
import time
import math

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'
ORANGE  = '\033[1;33m' # orange


def func_translate(lang_in, lang_out, data):
	translated = GoogleTranslator(source=lang_in, target=lang_out).translate(data.strip())
	return translated

def atbash(message):
		alphabet = u'A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z a b c d e f g h i j k l m n ñ o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9'.split()
		backward = u'Z Y X W V U T S R Q P O Ñ N M L K J I H G F E D C B A z y x w v u t s r q p o ñ n m l k j i h g f e d c b a 9 8 7 6 5 4 3 2 1 0'.split()
		cipher = []
		
		for letter in message:
				if letter in alphabet:
						for i in range(0,len(alphabet)):
								if alphabet[i] == letter:
										pos = i
						cipher.append(backward[pos])
				else:
						cipher.append(letter)
		
		newMessage = ''.join(cipher)
		print(newMessage)

def sentropy(string):
		"""
		Calculates the Shannon entropy for the given string.

		:param string: String to parse.
		:type string: str

		:returns: Shannon entropy (min bits per byte-character).
		:rtype: float
		"""
		if isinstance(string, bytes):
				string = string.encode("ascii")
		ent = 0.0
		if len(string) < 2:
				return ent
		size = float(len(string))
		for b in abcd:
				freq = string.count(b)
				if freq > 0:
						freq = float(freq) / size
						ent = ent + freq * math.log(freq, 2)
		return -ent

def entropybase(args):


	randsentence=""
	print("ENTROPY BASE")
	
	entrada = ''
	for en in args:
		entrada += en
	entrada = entrada.replace(args[0], '')
	print("input", entrada)
	#print(sentropy(testentropy))
	for e in range(0, int(args[0])):
			try:
					randsentence=""
					for x in range(0,len(entrada)):

							randsentence += random.choice(entrada)

					
					print(sentropy(randsentence))
					print(sentropy(entrada))
					print(randsentence)
					print(func_translate("iw","es",randsentence))
					time.sleep(3)
			except:
					pass


def random_eq_entropy(text_in):

		

		return (entropy, intext,randtext, outext)

def raziel(args):


	w3 = ["א","מ","ש"]
	w7 = ["ב","ג","ד","כ","פ","ר","ת"]
	w12 = ["ה","ו","ז","ח","ט","י","ל","נ","ס","ע","צ","ק"]
	wheel3 =["a","b","c"]
	wheel7=["d","f","g","h","i","j","k"]
	wheel12=["l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w"]

	i=0
	i2=0
	triplets = {}
	triplets2 = {}
	triplets3 = {}
	ng=""
	ng2=""
	ng3=""
	ng4=""

	## RAZIEL
	for q in w3:
			for w in w7:
					for e in w12:
							triplets[i]=str(q)+str(w)+str(e)
							ng = ng+triplets[i]
							ng2 = triplets[i]+ng2
							
							if i % 7 == 0 or i == 0:
									ng3 = triplets[i][0]+triplets[i][1]+ng3
									ng4 = ng4+triplets[i][0]+triplets[i][1]
							print(triplets[i])
							print(func_translate("iw","en",triplets[i]))

							i=i+1


def coreOptions():
	options = [["lang", "lang to search", "es"]]
	return options

## Extend command usage instructions 
def ExtendCommands():
	commands = [["entropybase",""],["raziel",""],["atbash",""]]
	return commands


def core(moduleOptions):
	print('Command run disabled on current module')

def save(moduleOptions):
	global lang
	lang = moduleOptions[0][2]
