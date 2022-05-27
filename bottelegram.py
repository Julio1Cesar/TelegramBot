import telebot

CHAVE_API = '5305588248:AAHlG9laEx9vANAIKO_n0vCaoLBTDdayCoY'

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=['pastel'])
def pastel(msg):
    bot.send_message(msg.chat.id, "Saindo pizza para sua casa: Tempo de espera em 20 min!")


@bot.message_handler(commands=['hamburguer'])
def hamburguer(msg):
    bot.send_message(msg.chat.id, "Saindo hamburguer tempo de espera aprox: 20 minutos")


@bot.message_handler(commands=['batatafrita'])
def batatafrita(msg):
    bot.send_message(msg.chat.id, 'a batata acabou :( clique aqui para iniciar: /iniciar')


@bot.message_handler(commands=['opcao1'])
def opcao1(msg):
    texto = """
    CARDÁPIO
    /pastel Pastel
    /hamburguer Hamburguer
    /batatafrita Batata frita
    (clique em uma opção
    """
    bot.send_message(msg.chat.id, texto)


@bot.message_handler(commands=['opcao2'])
def opcao2(msg):
    bot.send_message(msg.chat.id, 'Para reclamar de algo mande para o e-mail: reclameaqui@algumacoisa.com')


def verificar(msg):
    return True


@bot.message_handler(func=verificar)
def responder(msg):
    texto = """
    Escolha uma opção para continuar (Clique no item):
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
Responder qualquer outra coisa não vai funcionar, clique em uma das opções
    """
    bot.reply_to(msg, texto)


bot.polling()
