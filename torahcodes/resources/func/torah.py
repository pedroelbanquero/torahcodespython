from deep_translator import GoogleTranslator
import torahcodes.resources.func.utils as util
from hebrew_numbers import gematria_to_int
#from textblob import TextBlob
from os import listdir
from os.path import isfile, join
import re
import time
import random


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'
ORANGE  = '\033[1;33m' # orange

import os

data_dir = os.path.abspath( os.path.dirname( __file__ ) )

data_dir = data_dir.replace('func', 'data/')

class BibleBooks():
    def __init__(self):
        self.folder = data_dir
        self.book = {}
    def load(self):
        
        for f in listdir(self.folder):
            if isfile(join(self.folder, f)) and f.endswith(".json"):
                fn = f.split('.')
                #print('Load', fn[0])
                with open(self.folder+f, encoding="utf-8-sig") as File:
                    self.book[fn[0]] = File.read()

    def rawdata(self, bookname):
        return self.book[bookname]

    def booklist(self):
        return list(self.book.keys())

books = BibleBooks()

class Torah():
	def __init__(self):
		self.book = ''
		self.gcode = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
               'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80,
               'צ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400, 'ך': 20, 'ם': 40, 'ן': 50, 'ף': 80, 'ץ': 90}
		

	def loadbooks(self):
		books.load()

	def func_getnumber(self, listL, listW):
		return util.fn_GetNumberValues(listL, listW)



	def numtobook(self, number):
		for x in books.booklist():
			xt = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", x)
			if xt[0] == str(number):
				return x

	def func_translate(self, lang_in, lang_out, data):
		translated = GoogleTranslator(source=lang_in, target=lang_out).translate(data.strip()) 
		return translated

	def gematria(self, word: str) -> int:
		try:
			if word.isdigit():
				return int(word)

			# Aufteilen des Wortes in Buchstaben und Zahlen
			letters = [char for char in word if char.isalpha()]
			numbers = [int(char) for char in word if char.isdigit()]

			# Berechnen des Gematria-Werts für die Buchstaben
			letters_value = sum([self.gcode[char] for char in letters if char in self.gcode])


			# Hinzufügen der Summe der Zahlen zum Gematria-Wert der Buchstaben
			total_value = letters_value + sum(numbers)

			return total_value
		except:
			print(word)
			raise ValueError


	def gematrix(self, phrase: str) -> int:
		phrase = self.strip_accents(phrase.lower())
		phrase = ''.join([i for i in phrase if i.isalpha() or i.isdigit() or i.isspace()])

		# Aufteilen der Eingabe in separate Wörter und Zahlen
		elements = phrase.split()
		total_value = 0

		for element in elements:
			if element.isalpha():
				# Berechne den Wert für Buchstaben
				total_value += sum([self.gcode[char] for char in element if char in self.gcode])
			elif element.isdigit():
				# Addiere Zahlen direkt zum Gesamtwert
				total_value += int(element)

		return total_value






	def strip_accents(self, s):
	    try:
	        return ''.join(
	            c for c in unicodedata.normalize('NFD', s)
	            if unicodedata.category(c) != 'Mn'
	        )
	    except:
	        return s


	def gematria_iw_int(text):
		return gematria_to_int(text)


	def func_ParseTranslation(self, translated, lang, active):
		abd = 'abcdefghijklmnñopqrstuvwxyz1234567890'
		str_split = translated.split(' ')
		str_final = ''
		for word in str_split:
			try:
				if word[0].lower() in abd:

					str_final = str_final+ word+' '
			except:
				pass
		
		if not str_final == '':
			return str_final
		else:
			return 0
	def els(self, namebook, number, tracert='false', visualice=False):
		space = number
		abd = 'abcdefghijklmnñopqrstuvwxyz'
		i=1
		rese=""
		totalvalue = 0
		D = self.GetDataBook(namebook)
		for (z,b,y) in D:
			try:
				charnum = 0
				res=""

				for char in D[z,b,y]:
					charnum = charnum+1
					if (i % int(space)) == 0:
						if tracert == 'true':
							totalvalue = totalvalue + int(charnum)
							print('Source:',int(z),'chapter:', int(b),'Verse:', int(y),'CharNum:',int(charnum),'Char:', char)

						res=res+char

					i=i+1
				rese=rese+" "+res
			except:
				pass
		#print('Total', totalvalue)
		ret = re.sub('\s+', ' ', rese.strip())
		return ret, totalvalue

	def GetDataBook(self, bibleNumberBook):


		JSON = books.rawdata(bibleNumberBook) 
		ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces = util.fn_TextFilePreprocess(JSON)
		ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces = util.fn_ConvertJSONStringsToDicts(ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces)
		SearchTextChosen = util.fn_GetNumberOfTextChosen(ListOfDictsOfJSONStringsParsed)
		ZippedTupleNoSpaces, ZippedTupleWithSpaces = util.fn_ZippedTupleCreate(ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces, SearchTextChosen)
		D, DS = util.fn_DictionaryOfVersesCreate(ZippedTupleNoSpaces, ZippedTupleWithSpaces)
		S, L, DL, D5, ListOfWords = util.fn_DataObjectsCreate(D, DS)
		N, NW = util.fn_GetNumberValues(S, ListOfWords) 
		ListOfIndexesCustom = util.fn_ListOfIndexesCustomCreate(D5)
		W = util.fn_TupleOfWordsAndGematriaValuesCreate(ListOfWords, NW)

		return D

