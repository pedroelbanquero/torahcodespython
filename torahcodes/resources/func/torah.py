from deep_translator import GoogleTranslator
import torahcodes.resources.func.utils as util
from hebrew_numbers import gematria_to_int
from textblob import TextBlob
from os import listdir
from os.path import isfile, join
import re
import time
import random
import unicodedata


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
		self.gcode = {
    # Lateinische Buchstaben
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 600,
    'k': 10, 'l': 20, 'm': 30, 'n': 40, 'o': 50, 'p': 60, 'q': 70, 'r': 80, 's': 90,
    't': 100, 'u': 200, 'v': 700, 'w': 900, 'x': 300, 'y': 400, 'z': 500,

    # Basisbuchstaben und einige bereits genannte Varianten
    'ا': 1, 'أ': 1, 'إ': 1, 'آ': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9,
    'ي': 10, 'ى': 10, 'ك': 20, 'ک': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80,
    'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000,
    'ٱ': 1, # Alif Wasla
    'ـ': 0, # Tatweel

    # Zusätzliche Varianten und Sonderzeichen
    'ة': 400, # Taa Marbuta
    'ؤ': 6,  # Waw mit Hamza darüber
    'ئ': 10, # Ya mit Hamza darüber
    'ء': 1,  # Hamza
    'ى': 10, # Alif Maqsurah
    'ٹ': 400, # Taa' marbuta goal
    'پ': 2,  # Pe (Persisch/Urdu)
    'چ': 3,  # Che (Persisch/Urdu)
    'ژ': 7,  # Zhe (Persisch/Urdu)
    'گ': 20, # Gaf (Persisch/Urdu)
    'ڭ': 20, # Ngaf (Kazakh, Uyghur, Uzbek, and in some Arabic dialects)
    'ں': 50, # Noon Ghunna (Persisch/Urdu)
    'ۀ': 5,  # Heh with Yeh above (Persisch/Urdu)
    'ے': 10, # Barree Yeh (Persisch/Urdu)
    '؋': 0,  # Afghani Sign (wird als Währungssymbol verwendet, nicht für Gematria relevant, aber hier zur Vollständigkeit aufgeführt)

    # Anmerkung: Das Währungssymbol und ähnliche Zeichen sind in einem Gematria-Kontext normalerweise nicht relevant,
    # werden aber der Vollständigkeit halber aufgeführt. Es gibt noch viele weitere spezifische Zeichen in erweiterten
    # arabischen Schriftsystemen (z.B. für andere Sprachen wie Persisch, Urdu, Pashto usw.), die hier nicht vollständig
    # abgedeckt sind.

    # Grund- und Schlussformen hebräischer Buchstaben

    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
    'כ': 20, 'ך': 500, 'ל': 30, 'מ': 40, 'ם': 600, 'נ': 50, 'ן': 700, 'ס': 60, 'ע': 70, 'פ': 80, 'ף': 800,
    'צ': 90, 'ץ': 900, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400,

    # Griechische Buchstaben
    'α': 1, 'β': 2, 'γ': 3, 'δ': 4, 'ε': 5, 'ϝ': 6, 'ζ': 7, 'η': 8, 'θ': 9, 'ι': 10,
    'κ': 20, 'λ': 30, 'μ': 40, 'ν': 50, 'ξ': 60, 'ο': 70, 'π': 80, 'ϟ': 90, 'ρ': 100,
    'σ': 200, 'τ': 300, 'υ': 400, 'φ': 500, 'χ': 600, 'ψ': 700, 'ω': 800, 'ϡ': 900,

    # Griechische Großbuchstaben
    'Α': 1, 'Β': 2, 'Γ': 3, 'Δ': 4, 'Ε': 5, 'Ϝ': 6, 'Ζ': 7, 'Η': 8, 'Θ': 9, 'Ι': 10,
    'Κ': 20, 'Λ': 30, 'Μ': 40, 'Ν': 50, 'Ξ': 60, 'Ο': 70, 'Π': 80, 'Ϟ': 90, 'Ρ': 100,
    'Σ': 200, 'Τ': 300, 'Υ': 400, 'Φ': 500, 'Χ': 600, 'Ψ': 700, 'Ω': 800, 'Ϡ': 900,
    }

	def loadbooks(self):
		books.load()

	def func_getnumber(self, listL, listW):
		return util.fn_GetNumberValues(listL, listW)

	def func_checklang(self, word, lang):
		b = TextBlob(word)
		
		try:
			b.detect_language()
			if (b.detect_language() == lang):
				return True
		except:
			return True
		return False

	def numtobook(self, number):
		for x in books.booklist():
			xt = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", x)
			if xt[0] == str(number):
				return x

	def func_translate(self, lang_in, lang_out, data):
		translated = GoogleTranslator(source=lang_in, target=lang_out).translate(data.strip()) 
		return translated

	def strip_diacritics(self, text):
		if isinstance(text, list):
			text = ''.join(text)  # Konvertiere die Liste in einen String, falls notwendig
		stripped_text = ''
		for char in unicodedata.normalize('NFD', text):
			if unicodedata.category(char) not in ['Mn', 'Cf']:
				stripped_text += char
			else:
				print(f"Info: Diakritisches Zeichen '{char}' wird ignoriert.")
		return stripped_text

	def gematria(self, word: str) -> int:
		try:
			if word.isdigit():
				return int(word)

			letters = [char for char in word if char.isalpha()]
			numbers = [int(char) for char in word if char.isdigit()]

			letter_no_diacritics = self.strip_diacritics(letters)  # Jetzt wird hier ein String übergeben
			letters_value = sum(
				[self.gcode.get(char, 0) for char in letter_no_diacritics])  # Verwende .get() um Fehler zu vermeiden

			total_value = letters_value + sum(numbers)
			return total_value
		except Exception as e:
			print(f"Ein Fehler ist aufgetreten bei der Verarbeitung von '{word}': {e}")
			raise

	def gematrix(self, phrase: str) -> int:
		phrase = self.strip_diacritics(phrase.lower())
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


	def gematria_iw_int(text):
		return gematria_to_int(text)


	def func_ParseTranslation(self, translated, lang, active):
		abd = 'abcdefghijklmnñopqrstuvwxyz1234567890'
		str_split = translated.split(' ')
		str_final = ''
		for word in str_split:
			try:
				if word[0].lower() in abd:
					if active == 'true':
						if self.func_checklang(word, lang) == True:
							str_final = str_final+ word+' '
					else:
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
		return rese

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


