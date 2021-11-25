## BAPHOMET BOT , tora bible codes , jeremiah edition 0.1
import modules.resources.imports as i
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove,KeyboardButton)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler,ConversationHandler)
import threading, time
from queue import Queue
import resources.func.functions as torah

import modules.resources.config as config

import modules.resources.msg as msg
import modules.resources.txt as txt2
import logging


import os.path
from os import path
import os as os
## MAIN SOURCE

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


logger = logging.getLogger(__name__)


START  = range(1)

langin = 'en'
langout = 'es'
ptrans = True
threads = 10

msgqueue = {}


def searchAll(q, number, chatid):
    global langout, ptrans, msgqueue
    #if not q.empty():
    #print('init '+ str(number))
    while not q.empty():
        try:
            value = q.get()
            ret = torah.func_GettextFromNumber(value,number)
            rett = torah.func_translate('iw', langout, ret)
            retp = torah.func_ParseTranslation(rett,langout, ptrans)
            if not retp == 0:
                #print(retp)
                msgqueue[chatid] = msgqueue[chatid] + '\n' +retp
                q.task_done()
            else:
                q.task_done()
        except:
            q.task_done()
            pass

def search(text, chatid):
    global langin, langout, threads, msgqueue
    jobs = Queue()
    msgqueue[chatid] = ''
    listform = ''
    options = text.split(' ')
    for string in options:
        #print(string)
        translated = torah.func_translate(langin, 'iw', string)
        listform = listform +translated
    mod_num = torah.mod_9GetNumberValues.fn_GetNumberValues(listform,options)

    sed = mod_num[1][0]

    for i in range(1,43):
        jobs.put(i)

    for i in range(int(threads)):
        worker = threading.Thread(target=searchAll, args=(jobs, sed, chatid,))
        worker.start()

    #print("waiting for ", str(jobs.qsize())+'/43', "tasks")
    jobs.join()
    if not msgqueue[chatid] == '':
        msg.sendmsg(chatid,msgqueue[chatid]+"\n\n",False)
    #print('Done.')

def searchnumber(number,chatid):
    global jobs, langin, langout, threads, msgqueue
    jobs = Queue()
    msgqueue[chatid] = ''

    for i in range(1,43):
        jobs.put(i)

    for i in range(int(threads)):
        worker = threading.Thread(target=searchAll, args=(jobs, number, chatid,))
        worker.start()

    #print("waiting for ", str(jobs.qsize())+'/43', "tasks")
    jobs.join()
    if not msgqueue[chatid] == '':
        msg.sendmsg(chatid,msgqueue[chatid]+"\n\n",False)
    #print('Done.')


def mainload(chatid,txt,btdat,update):


      if ""=="" :
            if "/help" in txt or "/help" in btdat:
                #print(update.message)
                msg.sendmsg(chatid,txt2.presentacion+'\n\n'+'Baphomet Bot\n\n'+'/search \n\n'+'/searchnum \n\n'+'/talk sentence \n\n'+'/help \n\n'+'/start \n\n',False)

            if "/restart" == txt or "/restart" in btdat or "/start" in txt:


                keyboard = [[InlineKeyboardButton("search", callback_data='/search '+str(chatid))],[InlineKeyboardButton("number search", callback_data='/numsearch '+str(chatid))],[InlineKeyboardButton("talk", callback_data='/talk '+str(chatid))],[InlineKeyboardButton("help", callback_data='/help '+str(chatid))]]

                #keyboard = [[InlineKeyboardButton("Ayuda Emergencia", callback_data='/ayuda_emergencia '+str(chatid)),
                 #   InlineKeyboardButton("Ayuda Económica", callback_data='/ayuda_economica '+str(chatid))],                    [InlineKeyboardButton("Trámites municipio", callback_data='/municipio '+str(chatid))],[InlineKeyboardButton("Identidad Digital", callback_data='/identidad '+str(chatid))],[InlineKeyboardButton("Monedero", callback_data='/monedero '+str(chatid))],[InlineKeyboardButton("Diagnóstico Médico", callback_data='/diagnostico_rapido '+str(chatid))]]
                
                reply_markup = InlineKeyboardMarkup(keyboard)
                print(update)
                
                update.message.reply_text(
                    txt2.inicio+"\n\n"+txt2.presentacion,
                    reply_markup=reply_markup)


                #reply_markup = InlineKeyboardMarkup(keyboard)

               # update.message.reply_text(txt2.inicio+"\n\n"+txt2.presentacion)

                return (range(1))


            if "/search" in txt or "/search" in btdat:
                text_user = 0
                if len(txt) > len(btdat):
                    text_user = txt.replace('/search ','')
                else:
                    text_user = btdat.replace('/search ','')
                if len(text_user) > 0:
                #print(text_user)
                    msg.sendmsg(chatid,"Calculating...Wait...\n\n",False)
                    workmsg = threading.Thread(target=search, args=(text_user, chatid,))
                    workmsg.start()
                #data_search = search(text_user)
                else:
                    msg.sendmsgerror(chatid,"Error: Need string...\n\n",False)


            if "/numsearch" in txt or "/numsearch" in btdat:
                text_user = 0
                if len(txt) > len(btdat):
                    text_user = txt.replace('/numsearch ','')
                else:
                    text_user = btdat.replace('/numsearch ','')
                if len(text_user) > 0:
                    msg.sendmsg(chatid,"Calculating...Wait...\n\n",False)
                    workmsg = threading.Thread(target=searchnumber, args=(text_user, chatid,))
                    workmsg.start()
                else:
                    msg.sendmsgerror(chatid,"Error: Need number...\n\n",False)



            if "/talk" in txt or "/talk" in btdat or "/talk" in btdat or "talk" in btdat:

                msg.sendmsg(chatid,txt2.inicio,False)




            if "/cancel" in txt:
                #os.popen("killall ")
                update.message.reply_text("Servico parado")



            return range(1)

      else:
        update.message.reply_text("Not Allow")



def menu(update, context):
        chatid=0
        #print (update)
        try:
            user = update.message.from_user

            ##LOGGING DEBUG
            print (user)
            print (user.id)
            print(update.message.chat.id)
        except:
            pass

        btdat=""
        try:
            query = update.callback_query
            query.answer()
            btdat=query.data
            try:
                chatid=btdat.split(" ")[1]
            except:
                pass
        except:
            pass
        txt=""
        try:
            chatid = update.message.chat.id 
            txt = update.message.text
            print(txt)
            

        except:
            pass
        
        
        try:
            # TEXT
            files.save_txt("datos/"+str(chatid)+"/"+user.first_name+".userdata",str(user),chatid)
            files.save_txt("datos/"+str(chatid)+"/"+user.first_name+".log", "\n\n"+txt,chatid) 
        except:
            pass



        ## LOAD MODULES
        #if "None" !=str(txt):
        
        mainload(chatid,txt,btdat,update)


        return (range(1))

def cancel(update, context):
    user = update.message.from_user
    logger.info("The user %s stops conversations.", user.first_name)
    update.message.reply_text('See you soon.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def nada() :
    return ""







def main():
    ## main process
    updater = Updater(config.TOKEN, use_context=True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', menu)],

        states={
            START: [MessageHandler(Filters.regex('.') | Filters.location | Filters.photo, menu)]
        },fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(CallbackQueryHandler(menu))
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


main()

def is_validated(chatid):
    #check if user has been validated

    return (path.exists("datos/"+str(chatid)+"/mrcert_"+chatid+".pem"))




