import telebot, requests, re, json
from telebot import types

PRIVADO = [1993550658,1195893167]
#
#
GRUPO = [-1001523114084]
#
#
EXCEPT = [] # Hello World
#
#
ANONY = [] # OFF

bot = telebot.TeleBot("2018445619:AAFmgnSAL3sXBz5n0abPpNEM7wGUx0VyOY4")

@bot.message_handler(commands=['cnpj'])
def zn(message):
            id1 = message.chat.id
            ltnome = PRIVADO + GRUPO 
            botao = telebot.types.InlineKeyboardMarkup()
            delete = telebot.types.InlineKeyboardButton('Apagar', callback_data='get-USD')
            botao.add(delete)
            
            if id1 in ltnome:
                try:
                    msg = message.text
                    fl = msg.split('/cnpj')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://www.receitaws.com.br/v1/cnpj/' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CNPJ</b> 🔍\n\n<b>• CNPJ</b>: <code>{req["cnpj"]}</code>\n<b>• MATRIZ</b>: <code>{req["tipo"]}</code>\n\n<b>• ABERTURA</b>: <code>{req["abertura"]}</code>\n\n<b>• NOME</b>: <code>{req["nome"]}</code>\n\n<b>• NOME DA FANTASIA</b>: <code>{req["fantasia"]}</code>\n<b>• PORTE</b>: <code>{req["porte"]}</code>\n\n<b>• ATIVIDADE PRINCIPAL</b>: <code>{req["atividade_principal"]}</code>\n\n<b>• ATIVIDADES SEGUNDARIAS</b>: <code>{req["atividades_secundarias"]}</code>\n\n<b>• CÓDIGO NATUREZA JUDICIÁRIAS</b>: <code>{req["natureza_juridica"]}</code>\n\n<b>• QUEDRO DE SÓCIOS E ADMINISTRADORES</b>: <code>{req["nome"]}</code>\n\n<b>• LOGRADOURO</b>: <code>{req["logradouro"]}</code>\n<b>• NÚMERO</b>: <code>{req["numero"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n\n<b>• CEP</b>: <code>{req["cep"]}</code>\n<b>• BAIRRO</b>: <code>{req["bairro"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• ESTADO</b>: <code>{req["uf"]}</code>\n\n<b>• TELEFONE</b>: <code>{req["telefone"]}</code>\n<b>• EMAIL</b>: <code>{req["email"]}</code>\n\n<b>• By</b>: @federaldadosbot'
                    bot.send_chat_action(message.chat.id, 'typing')
                    bot.send_chat_action(message.chat.id, 'typing')
                    return bot.send_message(message.chat.id, response, reply_markup=botao, reply_to_message_id=message.message_id, parse_mode='html')
                    #bot.reply_to(nome, response, parse_mode='html')
                    def iq_callback(query):
                        data = query.data
                        if data == ('get-USD'):
                            bot.delete_message(message.chat.id, message.message_id)
                except Exception as e:
                    print(e)
                    bot.reply_to(message, '<b>CNPJ NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(message, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏
🔍 ⚡️「Federal Dados」⚡️ 🔎
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉
━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️
🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$10
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$19
• 1 MÊS = R$29
𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$28
• 31 𝘿𝙄𝘼𝙎 = R$35
━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼𝙎 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊𝙎 💲
✅ 𝙋𝙞𝙭
✅ 𝘾𝙧𝙞𝙥𝙩𝙤𝙢𝙤𝙚𝙙𝙖𝙨
✅ 𝘽𝙤𝙡𝙚𝙩𝙤
✅ 𝙋𝙞𝙘𝙋𝙖𝙮
<a href='http://t.me/jhon_shaft'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')
                		  		
@bot.message_handler(commands=['menu', 'help', 'start', 'ajuda'])
def bniio(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/menuu':
        bot.reply_to(men, '<b>' + '⚠ ERRADO MANO ⚠' + '</b>')
    else:
        try:
        	menu = f'Olá, <pre>{men.from_user.first_name}</pre>\n<b>VEJA MEUS COMANDOS</b>\n\n<b>🔍 MENU DO BOT 🔍</b>\n\n<b>• CPF</b>: <code>/cpf 09447342515</code>\n<b>• CNPJ</b>: <code>/cnpj 27865757000102</code>\n<b>• BIN</b>: <code>/bin 545323</code>\n<b>• VIZINHOS</b>: <code>/vizinhos 27867260854</code>\n<b>• PLACA</b>: <code>/placa ATJ8617</code>\n\n<b>• By</b>: @federaldadosbot'
        	bot.reply_to(men, menu, parse_mode='HTML')
        except:
                    bot.reply_to(men, 'ERRADO MANO',)
                    
@bot.message_handler(commands=['vizinhos'])
def byti(men):
            chtid = men.chat.id
            permitidos = PRIVADO + GRUPO 
            botao = telebot.types.InlineKeyboardMarkup()
            delete = telebot.types.InlineKeyboardButton('Apagar', callback_data='get-USD')
            botao.add(delete)
            
            if int(chtid) in permitidos:
                if men.text == '/vizinhos':
                    bot.reply_to(men, 'VIZINHOS Checker - Consulta de VIZINHOS, obtém os nomes dos vizinhos do portador do número de CPF.' + '\n\n' + 'Formato' + '\n' + '27867260854' + '\n' + 'ou' + '\n' + '278.672.608-54' + '\n\n' + '/vizinhos 27867260854')

                else:
                    header = {'Host': 'tudosobretodos.info', 'cache-control': 'max-age=0',
                              'upgrade-insecure-requests': '1', 'save-data': 'on',
                              'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
                              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                              'sec-fetch-site': 'cross-site', 'sec-fetch-mode': 'navigate',
                              'sec-fetch-user': '?1',
                              'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
                              'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                              'cookie': '__cfduid=dc3ac236c5f39888dbd7f585eedf6feb11596724421',
                              'cookie': '_ga=GA1.2.971515152.1596724424',
                              'cookie': '_gid=GA1.2.109978583.1596724424'}
                    num = re.sub('[^0-9]', '', men.text)
                    envia = requests.get("https://tudosobretodos.info/{}".format(num), headers=header).text

                    if "itemMoradores" in envia:
                        try:
                            bot.reply_to(men, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='html')

                            viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[3].split("<")[0][3:40]) + '\n' + str(envia.split("<div class='itemMoradores'>")[4].split("<")[0][3:40]) +'\n'+ \
                                   str(envia.split("<div class='itemMoradores'>")[5].split("<")[0][3:40])
                            
                            bot.reply_to(men, '<b>' '🔍 CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• By: @federaldadosbot' '</b>' , parse_mode='html')
                            
                        except:
                            try:
                                viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                       str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40])
                                
                                bot.reply_to(men,
                                             '<b>' '🔍 CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• By: @federaldadosbot' '</b>',
                                             parse_mode='html')
                            except:
                                bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>', parse_mode='HTML')



                    else:
                        bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>️', parse_mode='html')

            else:
                bot.reply_to(men, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏
🔍 ⚡️「Federal Dados」⚡️ 🔎
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉
━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️
🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$10
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$19
• 1 MÊS = R$29
𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$28
• 31 𝘿𝙄𝘼𝙎 = R$35
━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼𝙎 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊𝙎 💲
✅ 𝙋𝙞𝙭
✅ 𝘾𝙧𝙞𝙥𝙩𝙤𝙢𝙤𝙚𝙙𝙖𝙨
✅ 𝘽𝙤𝙡𝙚𝙩𝙤
✅ 𝙋𝙞𝙘𝙋𝙖𝙮
<a href='http://t.me/jhon_shaft'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')

@bot.message_handler(commands=['telefone'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO 
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/telefone')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://www.dualitybuscas.org/api_nova/telefoneastra.php?consulta=' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE TELEFONE</b> 🔍\n\n<b>• TELEFONE</b>: <code>{req["TELEFONE"]}</code>\n\n<b>• By</b>: @federaldadosbot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>TELEFONE NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                  bot.reply_to(nome, '<b>VOCÊ NÃO TEM AUTORIZAÇÃO</b>', parse_mode='HTML')



                
@bot.message_handler(commands=['placa'])
def zbsn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO 
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/placa')
                    ipp = re.sub('[^A-Z]', '', msg)
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get("https://apicarros.com/v1/consulta/" + ipp + ip + "/json", verify=False)
                    req = url.json()
                    response = f'🔍<b>PLACA ENCONTRADA</b>🔍\n\n<b>• PLACA</b>: <code>{req["placa"]}</code>\n<b>• ANO</b>: <code>{req["ano"]}</code>\n<b>• CHASSI</b>: <code>{req["chassi"]}</code>\n<b>• COR</b>: <code>{req["cor"]}</code>\n<b>• DATA</b>: <code>{req["data"]}</code>\n<b>• ALERME</b>: <code>{req["dataAtualizacaoAlarme"]}</code>\n<b>• VEICULO</b>: <code>{req["dataAtualizacaoCaracteristicasVeiculo"]}</code>\n<b>• ROUBO/FURTO</b>: <code>{req["dataAtualizacaoRouboFurto"]}</code>\n<b>• MARCA</b>: <code>{req["marca"]}</code>\n<b>• MODELO</b>: <code>{req["modelo"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• UF</b>: <code>{req["uf"]}</code>\n<b>• SITUAÇÃO</b>: <code>{req["situacao"]}</code>\n\n<b>• By</b>: @federaldadosbot'
                    bot.reply_to(nome, response, parse_mode="html") 
                    
                except:
                	bot.reply_to(nome, '<b>PLACA NÃO FOI ENCONTRADA</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏
🔍 ⚡️「Federal Dados」⚡️ 🔎
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉
━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️
🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$10
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$19
• 1 MÊS = R$29
𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$28
• 31 𝘿𝙄𝘼𝙎 = R$35
━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼𝙎 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊𝙎 💲
✅ 𝙋𝙞𝙭
✅ 𝘾𝙧𝙞𝙥𝙩𝙤𝙢𝙤𝙚𝙙𝙖𝙨
✅ 𝘽𝙤𝙡𝙚𝙩𝙤
✅ 𝙋𝙞𝙘𝙋𝙖𝙮
<a href='http://t.me/jhon_shaft'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')     
                      

@bot.message_handler(commands=['gov'])
def zbsn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO 
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='html')
                    msg = nome.text
                    fl = msg.split('/cpf')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('http://52.161.23.71/' + ip)
                    req = url.json()                    
                    response = f'🔍<b>CPF ENCONTRADO</b>🔍\n\n<b>• CPF</b>: <code>{req["cpfConsultado"]}</code>\n<b>• NOME</b>: <code>{req["nomeCompleto"]}</code>\n<b>• NASCIMENTO</b>: <code>{req["dataNascimento"]}</code>\n<b>• MÃE</b>: <code>{req["nomeDaMae"]}</code>\n\n<b>• LOGRADOURO</b>: <code>{req["nomeLogradouro"]}</code>\n<b>• NÚMERO</b>: <code>{req["numeroLogradouro"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["dsComplemento"]}</code>\n<b>• BAIRRO</b>: <code>{req["nomeBairro"]}</code>\n<b>• CIDADE</b>: <code>{req["nomeMunicipio"]}</code>\n<b>• ESTADO</b>: <code>{req["SiglaEstadoBrasileiro"]}</code>\n<b>• CEP</b>: <code>{req["cep"]}</code>\n\n<b>• By</b>: @federaldadosbot'
                    bot.reply_to(nome, response, parse_mode="html")
                except:
                	bot.reply_to(nome, '<b>CPF NÃO FOI ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏
🔍 ⚡️「Federal Dados」⚡️ 🔎
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉
━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️
🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$10
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$19
• 1 MÊS = R$29
𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$28
• 31 𝘿𝙄𝘼𝙎 = R$35
━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼𝙎 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊𝙎 💲
✅ 𝙋𝙞𝙭
✅ 𝘾𝙧𝙞𝙥𝙩𝙤𝙢𝙤𝙚𝙙𝙖𝙨
✅ 𝘽𝙤𝙡𝙚𝙩𝙤
✅ 𝙋𝙞𝙘𝙋𝙖𝙮
<a href='http://t.me/jhon_shaft'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')
                     

@bot.message_handler(commands=['tel'])
def zbsn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO 
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='html')
                    msg = nome.text
                    fl = msg.split('/tel')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('http://ifind.chapada.com.br:7777/?token=1217584c-856c-4d4f-83b9-fa4dc19fdb2a&tel=' + ip)
                    req = url.json()
                    response = f'🔍<b>TELEFONE ENCONTRADO</b>🔍\n\n<b>• CPF</b>: <code>{req["cpf"]}</code>\n<b>• NOME</b>: <code>{req["nome"]}</code>\n<b>• NASCIMENTO</b>: <code>{req["nasc"]}</code>\n<b>• MÃE</b>: <code>{req["mae"]}</code>\n\n<b>• GÊNERO</b>: <code>{req["sexo"]}</code>\n\n<b>• By</b>: @federaldadosbot'
                    bot.reply_to(nome, response, parse_mode="html")
                except:
                	bot.reply_to(nome, '<b>TELEFONE NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏
🔍 ⚡️「Federal Dados」⚡️ 🔎
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉
━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️
🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$10
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$19
• 1 MÊS = R$29
𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$28
• 31 𝘿𝙄𝘼𝙎 = R$35
━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼𝙎 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊𝙎 💲
✅ 𝙋𝙞𝙭
✅ 𝘾𝙧𝙞𝙥𝙩𝙤𝙢𝙤𝙚𝙙𝙖𝙨
✅ 𝘽𝙤𝙡𝙚𝙩𝙤
✅ 𝙋𝙞𝙘𝙋𝙖𝙮
<a href='http://t.me/jhon_shaft'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')	
                                   
@bot.message_handler(commands=['nome'])
def zbsn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO 
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='html')
                    msg = nome.text
                    fl = msg.split('/nome')                   
                    url = requests.get('http://ifind.chapada.com.br:7777/?token=1217584c-856c-4d4f-83b9-fa4dc19fdb2a&nome=' + msg)
                    req = url.json()
                    response = f'🔍<b>NOME ENCONTRADO</b>🔍\n\n<b>• CPF</b>: <code>{req["Cpf"]}</code>\n<b>• NOME</b>: <code>{req["Nome"]}</code>\n<b>• NASCIMENTO</b>: <code>{req["Nascimento"]}</code>\n<b>• Sexo</b>: <code>{req["Genero"]}</code>\n\n<b>• By</b>: @federaldadosbot'
                    bot.reply_to(nome, response, parse_mode="html")
                except:
                	bot.reply_to(nome, '<b>NOME NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏
🔍 ⚡️「Federal Dados」⚡️ 🔎
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉
━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️
🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$10
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$19
• 1 MÊS = R$29
𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$28
• 31 𝘿𝙄𝘼𝙎 = R$35
━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼𝙎 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊𝙎 💲
✅ 𝙋𝙞𝙭
✅ 𝘾𝙧𝙞𝙥𝙩𝙤𝙢𝙤𝙚𝙙𝙖𝙨
✅ 𝘽𝙤𝙡𝙚𝙩𝙤
✅ 𝙋𝙞𝙘𝙋𝙖𝙮
<a href='http://t.me/jhon_shaft'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')

@bot.message_handler(commands=['home'])
def help_command(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton(text = 'Dono do Bot', url='telegram.me/jhon_shaft'))

   bot.send_message(
       message.chat.id,
       '1) The bot supports inline. Bot @federaldadosbot',
       reply_markup=keyboard, parse_mode='html')

@bot.message_handler(commands=['teste'])
def command(message):
  oik = ('''Consulta de CPF
         CPF: 000000
         Nome: Luke mak det
         Endereço: lupo alt, 1576.
         Complemento: N/D
         ''')
  keyboard = telebot.types.InlineKeyboardMarkup()
  keyboard.row(
      telebot.types.InlineKeyboardButton('Teste1', callback_data='get-USD')
  )
  keyboard.row(
    telebot.types.InlineKeyboardButton('Teste2', callback_data='get-EUR'),
    #telebot.types.InlineKeyboardButton('Teste3', callback_data='get-RUR')
  )
  
  #bot.send_message(message.chat.id, 'Click no Botão:', reply_markup=keyboard, parse_mode='html')
  bot.send_message(message.chat.id, oik, reply_markup=keyboard, parse_mode='html')

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
   data = query.data
   if data.startswith('get-'):
       get_ex_callback(query)

def get_ex_callback(query):
   bot.answer_callback_query(query.id)
   send_exchange_result(query.message, query.data[4:])

def send_exchange_result(message, USD):
#    bot.send_chat_action(message.chat.id, 'typing')
#    bot.send_message(message.chat.id, 'Teste 1 OK', parse_mode='html')
   bot.delete_message(message.chat.id, message.message_id)

#Duplicação do botão

@bot.message_handler(commands=['vps'])
def command(message):
  luk = ('''Consulta de CPF
CPF: 000000
Nome: Luke mak det
Endereço: lupo alt, 1576.
Complemento: N/D''')


  botao = telebot.types.InlineKeyboardMarkup()
  delete = telebot.types.InlineKeyboardButton('Apagar', callback_data='get-USD')
  botao.add(delete)
  
  bot.send_message(message.chat.id, luk, reply_markup=botao, parse_mode='html')

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
   data = query.data
   if data == ('get-USD'):
      bot.delete_message(message.chat.id, message.message_id)
      

@bot.message_handler(commands=['ff'])
def zbsn(message):
            botao = telebot.types.InlineKeyboardMarkup()
            delete = telebot.types.InlineKeyboardButton('Apagar', callback_data='get-USD')
            botao.add(delete)
            id1 = message.chat.id

            ltnome = PRIVADO + GRUPO 
            if id1 in ltnome:
                    #bot.reply_to(message, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='html')
                    msg = message.text
                    fl = msg.split('/ff')
                    ipp = re.sub('[^A-Z]', '', msg)
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get("https://apicarros.com/v1/consulta/" + ipp + ip + "/json")#, verify=False)
                    req = url.json()
                    response = f'🔍<b>PLACA ENCONTRADA</b>🔍\n\n<b>• PLACA</b>: <code>{req["placa"]}</code>\n<b>• ANO</b>: <code>{req["ano"]}</code>\n<b>• CHASSI</b>: <code>{req["chassi"]}</code>\n<b>• COR</b>: <code>{req["cor"]}</code>\n<b>• DATA</b>: <code>{req["data"]}</code>\n<b>• ALERME</b>: <code>{req["dataAtualizacaoAlarme"]}</code>\n<b>• VEICULO</b>: <code>{req["dataAtualizacaoCaracteristicasVeiculo"]}</code>\n<b>• ROUBO/FURTO</b>: <code>{req["dataAtualizacaoRouboFurto"]}</code>\n<b>• MARCA</b>: <code>{req["marca"]}</code>\n<b>• MODELO</b>: <code>{req["modelo"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• UF</b>: <code>{req["uf"]}</code>\n<b>• SITUAÇÃO</b>: <code>{req["situacao"]}</code>\n\n<b>Para vc:</b> @{message.from_user.username}\n\n<b>• By</b>: @federaldadosbot'
                    #bot.reply_to(message, response, parse_mode="html")
                    bot.send_chat_action(message.chat.id, 'typing')
                    #bot.send_message(id1, response, reply_markup=botao, parse_mode='html')
                    return bot.send_message(message.chat.id, response, reply_markup=botao, reply_to_message_id=message.message_id, parse_mode='html')
                    
                    
@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
   data = query.data
   if data == ('get-USD'):
      bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(commands=['cpf'])
def zbsn(message):
            botao = telebot.types.InlineKeyboardMarkup()
            delete = telebot.types.InlineKeyboardButton('Apagar', callback_data='get-USD')
            botao.add(delete)
            id1 = message.chat.id

            ltnome = PRIVADO + GRUPO 
            if id1 in ltnome:
                try:
                    #bot.reply_to(message, '<code>AGUARDE, ESTOU BUSCANDO...</code>', parse_mode='html')
                    msg = message.text
                    fl = msg.split('/cpf')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('http://testemmmm-27623.portmap.host:27623/' + ip, verify=False)
                    req = url.json()                    
                    response = f'🔍 <b>CPF ENCONTRADO</b> 🔍\n\n<b>• CPF</b>: <code>{req["cpfConsultado"]}</code>\n<b>• NOME</b>: <code>{req["nomeCompleto"]}</code>\n<b>• NASCIMENTO</b>: <code>{req["dataNascimento"]}</code>\n<b>• MÃE</b>: <code>{req["nomeDaMae"]}</code>\n\n<b>• LOGRADOURO</b>: <code>{req["nomeLogradouro"]}</code>\n<b>• NÚMERO</b>: <code>{req["numeroLogradouro"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["dsComplemento"]}</code>\n<b>• BAIRRO</b>: <code>{req["nomeBairro"]}</code>\n<b>• CIDADE</b>: <code>{req["nomeMunicipio"]}</code>\n<b>• ESTADO</b>: <code>{req["SiglaEstadoBrasileiro"]}</code>\n<b>• CEP</b>: <code>{req["cep"]}</code>\n\n<b>• By</b>: @federaldadosbot'
                    bot.send_chat_action(message.chat.id, 'typing')
                    return bot.send_message(message.chat.id, response, reply_markup=botao, reply_to_message_id=message.message_id, parse_mode='html')
                    #bot.send_message(message.chat.id, response, reply_markup=botao, parse_mode='html')
                    def iq_callback(query):
                        data = query.data
                        if data == ('get-USD'):
                           bot.delete_message(message.chat.id, message.message_id)
                except:
                	bot.reply_to(message, '<b>CPF NÃO FOI ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(message, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏
🔍 ⚡️「Federal Dados」⚡️ 🔎
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉
━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️
🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$10
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$19
• 1 MÊS = R$29
𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$28
• 31 𝘿𝙄𝘼𝙎 = R$35
━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼𝙎 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊𝙎 💲
✅ 𝙋𝙞𝙭
✅ 𝘾𝙧𝙞𝙥𝙩𝙤𝙢𝙤𝙚𝙙𝙖𝙨
✅ 𝘽𝙤𝙡𝙚𝙩𝙤
✅ 𝙋𝙞𝙘𝙋𝙖𝙮
<a href='http://t.me/jhon_shaft'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')


@bot.message_handler(commands=['set'])
def zbsn(message):
            botao = telebot.types.InlineKeyboardMarkup()
            delete = telebot.types.InlineKeyboardButton('Apagar', callback_data='get-USD')
            botao.add(delete)
            id1 = message.chat.id

            ltnome = PRIVADO + GRUPO 
            if id1 in ltnome:
                try:
                    msg = message.text
                    fl = msg.split('/set')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('http://ghostcenter.xyz/api/cpf/' + ip, verify=False)
                    req = url.json()                    
                    response = f'🔍 <b>CPF ENCONTRADO</b> 🔍\n\n<b>• CPF</b>: <code>{req["cpf"]}</code>\n<b>• NOME</b>: <code>{req["nome"]}</code>\n<b>• NASCIMENTO</b>: <code>{req["nascimento"]}</code>\n<b>• SEXO</b>: <code>{req["sexo"]}</code>\n\n<b>• By</b>: @federaldadosbot'
                    bot.send_chat_action(message.chat.id, 'typing')
                    return bot.send_message(message.chat.id, response, reply_markup=botao, reply_to_message_id=message.message_id, parse_mode='html')
                    def iq_callback(query):
                        data = query.data
                        if data == ('get-USD'):
                           bot.delete_message(message.chat.id, message.message_id)
                except:
                	    #bot.reply_to(message, '<b>CPF NÃO FOI ENCONTRADO</b>', parse_mode='html')
                            return bot.send_message(message.chat.id, '<b>CPF NÃO FOI ENCONTRADO</b>', reply_markup=botao, reply_to_message_id=message.message_id, parse_mode='html')
                            def iq_callback(query):
                                data = query.data
                                if data == ('get-USD'):
                                   bot.delete_message(message.chat.id, message.message_id)
            else:
                		bot.reply_to(message, '''𝘾𝙊𝙈𝙋𝙍𝙀 𝙅𝘼 𝙊 𝙎𝙀𝙐 𝘼𝘾𝙀𝙎𝙎𝙊 𝘼𝙊 𝙉𝙊𝙎𝙎𝙊 𝘽𝙊𝙏
🔍 ⚡️「Federal Dados」⚡️ 🔎
━━━━━━━━━━━━━━━━━
𝙊 𝘽𝙊𝙏 𝙏𝙀𝙈:
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙋𝙁
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘾𝙉𝙋𝙅
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙐𝙈𝙀𝙍𝙊
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙉𝙊𝙈𝙀
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙑𝙄𝙕𝙄𝙉𝙃𝙊𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝘼𝙍𝙀𝙉𝙏𝙀𝙎
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝙋𝙇𝘼𝘾𝘼
✅ 𝘾𝙊𝙉𝙎𝙐𝙇𝙏𝘼 𝘿𝙀 𝘽𝙄𝙉
━━━━━━━━━━━━━━━━━
⚠️ 𝙍𝙀𝙏𝙊𝙍𝙉𝘼 𝙏𝙊𝘿𝙊𝙎 𝙊𝙎 𝘿𝘼𝘿𝙊𝙎 ⚠️
🚨 𝙐𝙎𝙊 𝙄𝙇𝙄𝙈𝙄𝙏𝘼𝘿𝙊 PV 𝘿𝙊 𝘽𝙊𝙏 🚨
━━━━━━━━━━━━━━━━━
𝙑𝘼𝙇𝙊𝙍𝙀𝙎:
• 1 𝙎𝙀𝙈𝘼𝙉𝘼 = R$10
• 2 𝙎𝙀𝙈𝘼𝙉𝘼𝙎 = R$19
• 1 MÊS = R$29
𝙋𝘼𝙍𝘼 𝙎𝙀𝙐 𝙂𝙍𝙐𝙋𝙊:
• 15 𝘿𝙄𝘼𝙎 = R$28
• 31 𝘿𝙄𝘼𝙎 = R$35
━━━━━━━━━━━━━━━━━
💲 𝙁𝙊𝙍𝙈𝘼𝙎 𝘿𝙀 𝙋𝘼𝙂𝘼𝙈𝙀𝙉𝙏𝙊𝙎 💲
✅ 𝙋𝙞𝙭
✅ 𝘾𝙧𝙞𝙥𝙩𝙤𝙢𝙤𝙚𝙙𝙖𝙨
✅ 𝘽𝙤𝙡𝙚𝙩𝙤
✅ 𝙋𝙞𝙘𝙋𝙖𝙮
<a href='http://t.me/jhon_shaft'>Contratar Planos</a>
━━━━━━━━━━━━━━━━━''', parse_mode='html')
      
                        
bot.polling()