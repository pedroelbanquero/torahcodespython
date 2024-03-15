import argparse
import os
import sys
import subprocess
import shlex
#import pandas as pd
import threading, time
from queue import Queue
from torahcodes.resources.func.torah import *
#import modules.resources.xgboost as xgb
from deep_translator import GoogleTranslator
import re
import torahcodes.resources.func.db as db
from torahcodes.resources.func.thread import *


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'
ORANGE  = '\033[1;33m' # orange


tracert = 'false'
ptrans = 'true'
visualice = False
threads = 4
threads_trans = 4
totalvalue = 0
totalresult = 0
res_data = []
res_book = []
usedb = True
torah = Torah()
jobstrans = Jobs()
books.load()
db.createtable()

def checkdb(query, result):

        ret = db.getText(query)
        if len(ret) !=0:
                for dbitem in ret:
                        if dbitem[2] == result:
                                return dbitem

                return False
        else:
                return False




def test(options):
    for x in range(int(options[0]), int(options[1])):
        searchnumber([x, ''])

def process_hebrew_text(text):
    # Replace "י" with simple spaces
    # text = text.replace("י", "")

    # Replace multiple spaces with a single space
    text = re.sub(" +", "", text)

    # Remove single spaces
    text = text.replace(" ", "")

    return text

translations = {}

def ttranslator():
    global ptrans, totalvalue, tracert, totalresult, jobstrans, translations
    while True:
        tchunk = jobstrans.get()
        if tchunk is None:
            break
        tchunk = tchunk.split('*')
        dchunk = process_hebrew_text(tchunk[0])
        n = 2000
        text_chunks = [dchunk[i:i+n] for i in range(0, len(dchunk), n)]

        try:
            for chunk in text_chunks:
                fjoin = checkdb(tchunk[2], chunk)
                book = tchunk[1]
                gematria = tchunk[2]

                if fjoin is False:
                    rett_en = torah.func_translate('iw', 'en', chunk)
                    retp_en = torah.func_ParseTranslation(rett_en, 'en', ptrans)
                    if retp_en and retp_en != '0':
                        rett = torah.func_translate('en', 'es', str(retp_en))
                        retp = rett
                        db.addText(gematria, chunk, retp, retp_en, book)
                        totalresult += 1
                else:
                    retp, retp_en = fjoin[3], fjoin[4]

                if book not in translations:
                    translations[book] = {}
                if gematria not in translations[book]:
                    translations[book][gematria] = []

                translations[book][gematria].append({
                    "original": chunk,
                    "es": retp,
                    "en": retp_en,
                })
            jobstrans.done()
        except Exception as e:
            print(f"Exception in ttranslator: {e}")
            jobstrans.done()

def sort_books(book_key):
    """
    Sorting function for books.
    Attempts to extract book numbers and parts and sort them, e.g., 'text_12I' -> (12, 'I').
    """
    parts = book_key.split('_')
    number_part = parts[-1]  # Assumes that the number is at the end.
    num = ''.join(filter(str.isdigit, number_part))  # Extract digits
    suffix = ''.join(filter(str.isalpha, number_part))  # Extract letters
    return (int(num) if num else 0, suffix)

def print_translations():
    global translations
    no=0
    # Sort books by their number and suffix.
    for book in sorted(translations.keys(), key=sort_books):
        no+=1
        gematrias = translations[book]
        print(f"{WHITE}\n{no}. Result, Book: {book}")
        # Assumption: Gematria values do not need to be sorted or are already sorted.
        for gematria, texts in gematrias.items():
            print(f"{WHITE}Gematria: {gematria}")
            for text in texts:
                original = text["original"]
                es = text["es"]
                en = text["en"]
                print(f"{BLUE}HE: {original}")
                print(f"{ORANGE}ES: {es}")
                print(f"{GREEN}EN: {en}")

    print(f'{WHITE}\nFound {len(translations)} Results')
    # Reset the translations after displaying
    translations.clear()


def searchAll(q, number):
    global ptrans, totalvalue, tracert, totalresult, jobstrans
    while not q.empty():
        try:
            value = q.get()
            text_chunk = ''
            ret, tvalue = torah.els(value, number, tracert=tracert)
            totalvalue = totalvalue + tvalue

            text_trans= ''
            len_chunk = len(text_chunk)
            #print(GREEN, 'chunk size: ', len_chunk, END)
            nch = 0

            jobstrans.add(str(ret)+'*'+value+'*'+number)
            jobstrans.join()
            q.task_done()

        except Exception as e:
            q.task_done()
            #print(ORANGE + retp + END)
            print(RED,"Exception: {}".format(type(e).__name__),END)
            print(ORANGE,"Exception message: {}".format(e),END)
            #print(e)
            pass

def tonum(options):
    global langin, langout, threads, totalresult
    listform = ''
    print(options[0])
    if len(options) > 1:
        for string in options:
            listform = listform+' '+string
        sed = torah.gematrix(listform)
    else:
        #print(options[0])

        try:
            sed = torah.gematria(options[0].strip())
        except Exception as e:
            pass
            print(e)

    print(sed)


def search(options):
    global threads, totalresult, translations
    totalresult = 0
    jobs = Queue()

    listform = ' '.join(options)
    if len(options) > 1:
        sed = torah.gematrix(listform)
    else:
        sed = torah.gematria(options[0].strip())

    for i in books.booklist():
        jobs.put(i)

    for i in range(int(threads)):
        worker = threading.Thread(target=searchAll, args=(jobs, str(sed),))
        worker.start()

    jobs.join()
    print_translations()



def searchnumber(options):
    global threads, totalresult, jobstrans
    number = str(options[0])
    #threads = 1
    totalresult = 0

    jobs = Queue()

    bfor = books.booklist()
    for i in bfor:
        jobs.put(i)

    for i in range(int(threads)):
        worker = threading.Thread(target=searchAll, args=(jobs, number,))
        worker.start()

    jobs.join()
    print_translations()

def xgboost(options):
    print('Coming soon')

def probnet(options):
    print('Coming soon')

def coreOptions():
    options = [["threads", "Number of threads from search", "4"],["th_trans", "Number of threads from translate", "4"],["parse", "Parse char and detect language", "true"],["tracert", "Tracert Search", "false"]]
    return options

## Extend command usage instructions 
def ExtendCommands():
    commands = [["tonum","get number"],["test","test"],["searchnumber","search number space"],["search","search termsexp"],["xgboost"," XGBOOST"],["probnet","PROBNET"]]
    return commands


def core(moduleOptions):
    print('Command run disabled on current module')

def save(moduleOptions):
    global threads_trans, threads, ptrans, tracert, usedb
    threads = moduleOptions[0][2]
    threads_trans = moduleOptions[1][2]
    ptrans = moduleOptions[2][2]
    tracert = moduleOptions[3][2]
    usedb = moduleOptions[3][2]

worker = Threads(func=ttranslator, ntask=threads_trans)
worker.start()
