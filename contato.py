import telebot


CHAVE_API = "6896488404:AAHj01CxdTXY74VDSOsDsyUOmhLu7oyHtXU"
bot = telebot.TeleBot(CHAVE_API)

# Dados das pessoas da COPEG
@bot.message_handler(commands=["ALLAN"]) # um comando com opção 1
def ALLAN(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    dados = """
    Ramal: 3115-2424
    E-mail: ALLAN@sefaz.ba.gov.br
    """
    bot.send_message(mensagem.chat.id, dados)

# Dados das pessoa dentro da COPPE 
@bot.message_handler(commands=["COPEG"]) # um comando com opção 1
def COPEG(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    nome = """
    Nome:
    /ALLAN
    """
    bot.send_message(mensagem.chat.id, nome)

# Dados das pessoas da COPEG
@bot.message_handler(commands=["KATIA"]) # um comando com opção 1
def KATIA(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    dados = """
    Ramal: 3115-2424
    E-mail: KATIA@sefaz.ba.gov.br
    """
    bot.send_message(mensagem.chat.id, dados)

@bot.message_handler(commands=["DILMA"]) # um comando com opção 1
def DILMA(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    dados = """
    Ramal: 3115-8854
    E-mail: DILMA@sefaz.ba.gov.br
    """
    bot.send_message(mensagem.chat.id, dados)

# Dados das pessoa dentro da COPEG 
@bot.message_handler(commands=["COPEG"]) # um comando com opção 1
def COPEG(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    nome = """
    Nome:
    /DILMA 
    /KATIA
    """
    bot.send_message(mensagem.chat.id, nome)

# Dados das pessoas COEFI.
@bot.message_handler(commands=["RAIMUNDO"]) # um comando com opção 1
def RAIMUNDO(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    dados = """
    Ramal: 3115-8861 ou 3115-2428
    E-mail: RAIMUNDO@sefaz.ba.gov.br
    """
    bot.send_message(mensagem.chat.id, dados)

@bot.message_handler(commands=["MARCELO"]) # um comando com opção 1
def MARCELO(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    dados = """
    Ramal: 3115-5094
    E-mail: MARCELO@sefaz.ba.gov.br
    """
    bot.send_message(mensagem.chat.id, dados)

@bot.message_handler(commands=["LEILA"]) # um comando com opção 1
def LEILA(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    dados = """
    Ramal: 3115-8861 ou 3115-2428
    E-mail: LEILA@sefaz.ba.gov.br
    """
    bot.send_message(mensagem.chat.id, dados)

@bot.message_handler(commands=["FERNADO"]) # um comando com opção 1
def FERNADO(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    dados = """
    Ramal: 3115-2469
    E-mail: FERNADO@sefaz.ba.gov.br
    """
    bot.send_message(mensagem.chat.id, dados)

@bot.message_handler(commands=["CLARICE"]) # um comando com opção 1
def CLARICE(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    dados = """
    Ramal: 3115-2469
    E-mail: CLARICE@sefaz.ba.gov.br
    """
    bot.send_message(mensagem.chat.id, dados)

@bot.message_handler(commands=["CARLOS"]) # um comando com opção 1
def CARLOS(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    dados = """
    Ramal: 3115-5094
    E-mail: CARLOS@sefaz.ba.gov.br
    """
    bot.send_message(mensagem.chat.id, dados)

@bot.message_handler(commands=["ALISSON"]) # um comando com opção 1
def ALISSON(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    dados = """
    Ramal: 3115-2428 ou 3115-2428
    E-mail: ALISSON@sefaz.ba.gov.br
    """
    bot.send_message(mensagem.chat.id, dados)


@bot.message_handler(commands=["ALEXANDRA"]) # um comando com opção 1
def ALEXANDRA(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    dados = """
    Ramal: 3115-8859
    E-mail: ALEXANDRA@sefaz.ba.gov.br
    """
    bot.send_message(mensagem.chat.id, dados)

@bot.message_handler(commands=["ADRIANA"]) # um comando com opção 1
def ADRIANA(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    dados = """
    Ramal: 3115-8861 ou 3115-2428
    E-mail: ADRIANA@sefaz.ba.gov.br
    """
    bot.send_message(mensagem.chat.id, dados)

# Dados das pessoa dentro da COEFI 
@bot.message_handler(commands=["COEFI"]) # um comando com opção 1
def COEFI(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    nome = """
    Nome:
    /ADRIANA 
    /ALEXANDRA
    /ALISSON
    /CARLOS
    /CLARICE
    /FERNADO
    /LEILA
    /MARCELO
    /RAIMUNDO
    """
    bot.send_message(mensagem.chat.id, nome)

# Informar a Coordenação dentro da GEENC. 
@bot.message_handler(commands=["GEENC"]) 
def GEENC(mensagem):
    coordenacao = """
    SELECIONE A COORDENAÇÃO:
    /COEFI
    /COPEG
    /COPPE
    """
    bot.send_message(mensagem.chat.id, coordenacao)
# INFORMAR A GERENCIA SEPARADAMNETE. 
    
@bot.message_handler(commands=["RH"]) 
def RH(mensagem): 
    bot.send_message(mensagem.chat.id, "Essa função não esta disonivel")
    
@bot.message_handler(commands=["GSCETI"]) 
def GSCETI(mensagem): 
    bot.send_message(mensagem.chat.id, "Essa função não esta disonivel")
    
@bot.message_handler(commands=["DICOP"]) 
def DICOP(mensagem): 
    bot.send_message(mensagem.chat.id, "Essa função não esta disonivel")

@bot.message_handler(commands=["GEFIN"]) 
def GEFIN(mensagem): 
    bot.send_message(mensagem.chat.id, "Essa função não esta disonivel")

@bot.message_handler(commands=["GEENC"]) 
def GEENC(mensagem): 
    bot.send_message(mensagem.chat.id, "Essa função não esta disonivel")

# INFORMAR A GERENCIA
@bot.message_handler(commands=["SEFAZ"]) # um comando com opção 1
def opcao1(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    texto = """
    SELECIONE A GERÊNCIA:
    /GEENC
    /GEFIN
    /DICOP
    /GSCETI
    /RH
    """
    bot.send_message(mensagem.chat.id, texto)

# CRIAÇÃO DE OPÇÕES
@bot.message_handler(commands=["OUTRAS_SECRETARIAS"]) # um comando com opção 1
def SEFAZ(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    bot.send_message(mensagem.chat.id, "Esta opção ainda não esta habiliada")

@bot.message_handler(commands=["OUTRAS"]) # um comando com opção 1
def OUTRAS_SECRETARIAS(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    print(mensagem)
    # bot.reply_to(mensagem, "Valeu! um abraço")
    bot.send_message(mensagem.chat.id, "Esta opção ainda não esta habiliada") # Aqui ele não vai respoder a mesagem marcando. 


# Mensagem padrão. 
def verificar(mensagem): # função reficar que recebe a mensagem e que faz alguma coisa, retornando verdadebiro ou falso.
    return True # aqui a mensagem sempre vai retornar verdadeiro, não emporta a mensagem que enviar, ira responder "Olá eu sou Bot".

@bot.message_handler(func=verificar) # func é um parametro de função.
# Essa função vai responder qualquer mensagem que for enviada.
def respoder(mensagem): # mensagem é a ensagem quea pessoa vai receber como parametro. 
    texto = """
    SELECIONE UMA SECRETARIA (Cliqueno item):
    /SEFAZ
    /SETRI
    /OUTRAS_SECRETARIAS
    /NEW

Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    # bot.reply_to(mensagem, "Olá eu sou Bot")
    bot.reply_to(mensagem, texto)

    
# Configurando o bot.
bot.polling() # è como se fosse um loop infinito, vai fazer com que o pbot esteja conversando o tempo todo. Vai esta o tempo todo conversando

# http://t.me/dados_contacts_bot