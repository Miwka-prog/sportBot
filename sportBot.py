import telebot
from telebot import types

bot = telebot.TeleBot("1344484129:AAGLzI-fbJVGaLjNwZCNUbBD0r0wGIr4t-w")


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("💪 Вивчення вправ")
    markup.add(item1)
    bot.send_message(message.chat.id, "Привіт, {0.first_name}!\nЯ — <b>{1.first_name}</b>, бот створений, щоб навчити робити вправи правильно.".format(message.from_user, bot.get_me()), parse_mode = 'html', reply_markup = markup)


@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.chat.type == 'private':
        if message.text == '💪 Вивчення вправ':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Жим лежачи", callback_data='1')
            item2 = types.InlineKeyboardButton("Розводка гантелів", callback_data='2')
            item3 = types.InlineKeyboardButton("Жим гантелей на лаві з нахилом", callback_data='3')
            item4 = types.InlineKeyboardButton("Жим штанги лежачи на похилій лаві", callback_data='4')
            item5 = types.InlineKeyboardButton("Віджимання від підлоги", callback_data='5')
            item6 = types.InlineKeyboardButton("Жим гантелей лежачи", callback_data='6')
            item7 = types.InlineKeyboardButton("Тяга штанги лежачи PULL-OVER", callback_data='7')
            item8 = types.InlineKeyboardButton("Віджимання на брусах", callback_data='8')
            item9 = types.InlineKeyboardButton("Жим штанги вузьким хватом лежачи на лаві", callback_data='9')
            item10 = types.InlineKeyboardButton("Зведення рук на тренажері", callback_data='10')
            item11 = types.InlineKeyboardButton("Зведення верхніх блоків CROSS-OVER", callback_data='11')
            item12 = types.InlineKeyboardButton("Тяга гантелі через голову лежачи PULL-OVER", callback_data='12')
            item13 = types.InlineKeyboardButton("Станова тяга зі штангою", callback_data='13')
            item14 = types.InlineKeyboardButton("Гіперекстензія", callback_data='14')
            item15 = types.InlineKeyboardButton("«Мертва» тяга в стилі сумо", callback_data='15')
            item16 = types.InlineKeyboardButton("Присідання зі штангою на плечах", callback_data='16')
            item17 = types.InlineKeyboardButton("Розгинання ніг в тренажері сидячи", callback_data='17')
            item18 = types.InlineKeyboardButton("Згинання ніг лежачи", callback_data='18')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18)
            bot.send_message(message.chat.id, '{0.first_name}, обери вправу, яку потрібно пояснити.'.format(message.from_user),reply_markup=markup)
        else:
            bot.send_message(message.chat.id, message.text)


@bot.message_handler(func=lambda message: True)
def image(message, name):
    bot.send_photo(message.chat.id, open(name, "rb"))


@bot.message_handler(func=lambda message: True)
def send_message(message, definition):
    bot.send_message(message.chat.id, definition.format(message.from_user))


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == '1':
        image(call.message, "img/zhim.jpg")
        send_message(call.message, "Виконання жиму штанги на горизонтальній лаві\n"
            "1. Беремо гриф штанги трохи ширше плечей хватом зверху.\n"
            "2. Робимо вдих і повільно, підконтрольний опускаємо штангу до рівня грудей.\n"
            "3. Вижимаємо штангу і в кінці руху робимо видих.\n")
        send_message(call.message, "Жим штанги, лежачи на горизонтальній лаві опрацьовує весь великий грудний м'яз, малий грудний м'яз, передню частину дельтоподібного м'яза плеча, зубчасті і клювовидно-плечові м'язи, трицепси.")
    if call.data == '2':
        image(call.message, "img/rozvodka1.jpg")
        image(call.message, "img/rozvodka2.jpg")
        send_message(call.message, "Виконання розведення гантелей на похилій лаві\n"
                                   "1. Робимо вдих і розводимо руки так, щоб лікті були на одному горизонтальному рівні з плечима.\n"
                                   "2. Піднімаємо руки вгору і робимо видих.\n"
                                   "3. Коли руки підняті вертикально, то робимо короткочасне статичне напряження.\n")
        send_message(call.message, "Ця вправа в основному завантажує верх великого грудного м'яза.")
    if call.data == '3':
        image(call.message, "img/3.jpg")
        send_message(call.message, "Виконання вправи - жим гантелей лежачи на похилій лаві\n"
                                   "1. Робимо вдих і випрямляє руки вверх.Жім гантелей лежачи на похилій лаві - закінчення руху\n"
                                   "2. В кінці руху робимо видих.\n")
        send_message(call.message, "Жим гантелей лежачи на похилій лаві включає в роботу найбільше ключичний відділ грудних м'язів. Також працюють передні дельти, передні малі і зубчасті м'язи грудей, а також трохи трицепси.")
    if call.data == '4':
        image(call.message, "img/4.jpg")
        send_message(call.message, "Виконання вправи - жим штанги лежачи на похилій лаві\n"
                                   "1. Робимо вдих і опускаємо штангу до ключиць.\n"
                                   "2. Вижимаємо штангу вгору і робимо видих.\n")
        send_message(call.message, "Жим штанги лежачи на похилій лаві включає в роботу ключичний або верхній відділ великого грудного м'яза, передні дельти, передню малу і зубчасту грудну м'язи, трицепси.")
    if call.data == '5':
        image(call.message, "img/5.jpg")
        send_message(call.message, "Виконання вправи віджимання від підлоги\n"
                                   "1. Робимо вдих і згинаємо лікті, поки груди майже не торкнеться підлоги, хребет сильно не вигинає.\n"
                                   "2. Віджатися до повного випрямлення рук.\n"
                                   "3. У завершенні руху зробити видих.\n")
        send_message(call.message, "При віджиманні від підлоги робота передніх зубчастих м'язів притискає лопатки до грудної клітки, тим самим об'єднуючи роботу тулуба і рук.")
    if call.data == '6':
        image(call.message, "img/6.jpg")
        send_message(call.message, "Виконання жиму гантелей лежачи\n"
                                   "1. Робимо вдих і випрямляє руки не повертаючи передпліччя.\n"
                                   "2. По завершенні руху робимо видих.\n")
        send_message(call.message, "Жим гантелей лежачи аналогічний жиму штанги лежачи, тільки у вправі з гантелями досягається велика амплітуда руху, що сприяє більшому розтягуванню великих грудних."
                                   "\nПри цьому також працюють (хоча і не так інтенсивно) передні дельтовидні м'язи і трицепси.")
    if call.data == '7':
        image(call.message, "img/7.jpg")
        send_message(call.message, "Виконання тяги штанги лежачи PULL-OVER\n"
                                   "1. Робимо глибокий вдих і опускаємо штангу за голову трохи зігнувши руки в ліктях.\n"
                                   "2. Повертаємося в початкове положення і робимо видих.")
        send_message(call.message, "Тяга штанги лежачи PULL-OVER опрацьовує великий грудний м'яз, великий круглий м'яз, довгий пучок трицепсів, а також малу грудний м'яз, ромбоподібну м'яз і передні зубчасті м'язи.")
    if call.data == '8':
        image(call.message, "img/8.jpg")
        send_message(call.message, "Віджимання на брусах - виконання\n"
                                   "1. Робимо вдих і згинаючи руки опускаємося вниз.\n"
                                   "2. Віджатися вгору і в кінці руху зробити видих.\n")
        send_message(call.message, "Віджимання на брусах відмінно розтягують грудні м'язи і збільшують еластичність м'язів плечового пояса.")
    if call.data == '9':
        image(call.message, "img/9.jpg")
        send_message(call.message, "Жим штанги вузьким хватом лежачи на лаві: виконання вправи\n"
                                   "1. Робимо вдих і повільно, підконтрольний опускаємо гриф на низ грудей.\n"
                                   "2. Вижимаємо штангу у вихідне положення і робимо видих.\n")
        send_message(call.message, "Жим штанги вузьким хватом лежачи на лаві відмінно годиться для промальовування середини грудей і трицепсів.")
    if call.data == '10':
        image(call.message, "img/10.jpg")
        send_message(call.message, "Виконання відомості рук на тренажері\n"
                                   "1. Робимо вдих і зводимо руки якомога ближче один до одного.\n"
                                   "2. По завершенні руху зробити видих.\n")
        send_message(call.message, "Ця вправа завантажує великі грудні м'язи. Коли ми зводимо лікті воно впливає на внутрішні частини м'язів грудей, також працюють коротка головка біцепса і клювовидно-плечові м'язи.")
    if call.data == '11':
        image(call.message, "img/11.jpg")
        send_message(call.message, "Виконання вправи\n"
                                   "1. Зробити вдих і звести руки перед собою до торкання один з одним.\n"
                                   "2. По завершенні руху робимо видих.\n")
        send_message(call.message, "Зведення верхніх блоків CROSS-OVER добре впливає на великий грудний м'яз. Змінюючи кут нахилу корпусу та траєкторію руху рук можна пропрацювати всі частини великого грудного м'яза.")
    if call.data == '12':
        image(call.message, "img/12.jpg")
        send_message(call.message, "Тяга гантелі через голову лежачи PULL-OVER: виконання вправи\n"
                                   "1. Робимо вдих і опускаємо гантель за голову.\n"
                                   "2. Повертаємося в початкове положення і робимо видих.\n")
        send_message(call.message, "Ця вправа впливає на внутрішню частину грудей, довгий пучок трицепсів, найширший м'яз спини, велику круглу м'яз, малу грудний м'яз, ромбоподібну і передню зубчасту.")
    if call.data == '13':
        image(call.message, "img/13.jpg")
        send_message(call.message, "Виконання вправи станова тяга зі штангою\n"
                                   "1. Контролюючи напругу преса і поясниці робимо вдих, відриваємо штангу і піднімаємо уздовж передньої поверхні гомілок.\n"
                                   "2. Коли штанга дійде до колін, продовжувати випрямляти корпус і распрямлять ноги до повного випрямлення ніг.\n"
                                   "3. Після закінчення руху робимо видих.")
        send_message(call.message, "Станова тяга зі штангою задіє чотириглаві м'язи стегна і сідничні м'язи, при цьому працюють трапецієподібні і хребетно-крижові м'язи.")
    if call.data == '14':
        image(call.message, "img/14.jpg")
        send_message(call.message, "Поперекові прогинання: виконання\n"
                                   "1. Робимо вдих і затримавши дихання, і прогинаючи поперековий відділ, піднімаємо корпус вгору, поки він не буде в горизонтальному положенні.\n"
                                   "2. Плавно повертаємося в початкове положення і робимо видих.\n")
        send_message(call.message, "Гіперекстензія (поперекові прогинання) тренують в основному м'язи розгинають хребет, квадратний м'яз попереку і менше сідничного-великогомілкової м'язи і сідничні м'язи, за винятком короткого пучка біцепса стегна. ")
    if call.data == '15':
        image(call.message, "img/15.jpg")
        send_message(call.message, "Виконання «мертвої» тяги в стилі сумо\n"
                                   "1. Присісти так щоб стегна знаходились горизонтально підлозі;\n"
                                   "2. Взяти гриф трохи ширше плечей прямими руками;\n"
                                   "3. Робимо глибокий вдих, затримуємо дихання, напружуємо прес, прогинаємо спину в попереку, одночасно випрямляє ноги і тулуб встаємо;\n"
                                   "4. По завершенні руху робимо видих.")
        send_message(call.message, "На відміну від класичної станової тяги, «мертва» тяга в стилі сумо більше задействовует квадріцепс стегна і привідний м'яз і менше задіяна спина, яка на початку виконання мало прогинається.")
    if call.data == '16':
        image(call.message, "img/16.1.jpg")
        image(call.message, "img/16.2.jpg")
        send_message(call.message, "Присідання зі штангою на плечах: вихідне положення. Штанга повинна розташовуватися на спеціальній стійці. Взяти гриф на ширині, зручній для вашого статури. Підсісти під гриф, помістивши його на трапецевідних м'язах, і відвести лікті назад:\n"
                                   "1. Робиться глибокий вдих, спина прогнута в попереку, м'язи преса напружені, дивимося прямо перед собою або трохи вище, зміщуючи таз вперед знімаємо штангу зі стійки;\n"
                                   "2. Робимо пару кроків назад і ставимо ноги на ширині плечей, носки дивляться вперед або трохи розведені;\n"
                                   "3. Згинаємо коліна і присідаємо, спину під час руху фіксуємо, щоб не отримати травму;\n"
                                   "4. Присідаємо до горизонтального положення стегна, потім розгинає ноги і повертаємося в початкове положення;\n"
                                   "5. По завершенні присідаючи робимо видих.")
        send_message(call.message, "Присідання зі штангою розробляють в основному квадріцепси, м'язи сідниць, м'язи преса, м'язи, що випрямляють хребет, що приводять м'язи стегон і сідничного-великогомілкової м'язи.")
    if call.data == '17':
        image(call.message, "img/17.jpg")
        send_message(call.message, "Виконання розгинання ніг в тренажері сидячи\n"
                                   "1. Робимо вдих і випрямляє ноги до горизонталі. Повільно повертаємося в початкове положення.\n"
                                   "2. По завершенні руху робимо видих..\n")
        send_message(call.message, "Розгинання ніг сидячи добре підходить для ізольованої роботи над квадрицепсами - чотириголового м'яза стегна. Рекомендується для виконання новачкам. Його корисно виконувати перед більш складними вправами, наприклад, для розігріву колін.")
    if call.data == '18':
        image(call.message, "img/18.jpg")
        send_message(call.message, "Виконання згинання ніг лежачи\n"
                                   "1. Робимо вдих і одночасно згинаємо ноги, намагаємося торкнутися п'ятами сідниць. Повільно, під контролем, опустити ноги в початкове положення.\n"
                                   "2. По завершенні руху робимо видих.\n")
        send_message(call.message, "Згинання ніг лежачи задіє всі сідничного-підколінні м'язи, литкові м'язи, а також глибокі підколінні м'язи.")


bot.polling(none_stop=True)
