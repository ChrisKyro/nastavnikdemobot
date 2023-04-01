from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiogram.utils.markdown as fmt
import logging


bot_token = ''


bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


class question(StatesGroup):
    speakers_name = State()
    waiting_for_question = State()
    slogan_name = State()

def get_user_id(name: str):

    users_dict = {'Тимофею Сигитову': 'Тимофея Сигитова',
                  'Евгении Нелюбиной': 'Евгении Нелюбиной',
                  'Денису и Карине Ярыгиной': 'Дениса и Карины Ярыгиных',
                  'Ермолину Ивану': 'Ермолина Ивана'}
    try:
        return users_dict[name]
    except KeyError:
        return "Такого спикера нет ("


@dp.message_handler(commands='start')
async def welcome(message: types.message):
    buttons = ['Очные мероприятия', 'Другие порталы']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*buttons)
    await message.answer(
        fmt.text(
            fmt.text(f'Привет, {message.from_user.full_name}!'),
            fmt.text('<b>Наставник</b> - это просветительская платформа для навигации на пути к профессии через реальное взаимодействие с успешными представителями из разных сфер деятельности'),
            sep="\n"
        ), parse_mode="HTML", reply_markup=keyboard
    )

@dp.message_handler(commands='chatid')
async def chatid(message: types.message):
    idchat = message.chat.id
    await message.answer(idchat)

@dp.message_handler(lambda message: message.text == 'В главное меню')
async def welcome2(message: types.message):
    buttons = ['Очные мероприятия', 'Другие порталы']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*buttons)
    await message.answer(
        fmt.text(
            fmt.text(
                '<b>Наставник</b> - это просветительская платформа для навигации на пути к профессии через реальное взаимодействие с успешными представителями из разных сфер деятельности'),
            sep="\n"
        ), parse_mode="HTML", reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text == 'Очные мероприятия')
async def meetings(message: types.message):
    buttons = ['Диалог с Наставником #1', 'Диалог с Наставником #2', 'В главное меню']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*buttons)
    await message.answer(
        fmt.text(
            fmt.text('<b>Диалог с Наставником</b> - это очные мероприятия профориентационного проекта Наставник, открытый и доступный разговор школьников с представителями актуальных современных профессий'),
            fmt.text(),
            fmt.text('Выбери одно из актуальных очных мероприятий:'),
            sep="\n"
        ), parse_mode="HTML", reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text == 'Другие порталы')
async def contacts(message: types.message):
    buttons = 'В главное меню'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(buttons)
    await message.answer(
        fmt.text(
            fmt.text('<b>Полезные ссылки:</b>'),
            fmt.text(''),
            fmt.text('<a href="https://vk.com/nastavnikteam">Наша группа ВКонтакте</a>'),
            fmt.text('<a href="https://nastavnik.team/">Наш сайт</a>'),
            sep="\n"
        ), parse_mode="HTML", reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text == 'Диалог с Наставником #1')
async def m1(message: types.message):
    buttons = 'В главное меню'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(buttons)
    await message.answer(
        fmt.text(
            fmt.text('Данное мероприятие уже завершилось'),
            fmt.text(''),
            fmt.text('<b>Фотоотчёт:</b>'),
            sep="\n"
        ), parse_mode="HTML", reply_markup=keyboard
    )
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('media/1.png'))
    media.attach_photo(types.InputFile('media/2.png'))
    media.attach_photo(types.InputFile('media/3.png'))
    media.attach_photo(types.InputFile('media/4.png'))
    media.attach_photo(types.InputFile('media/5.png'))
    await bot.send_media_group(message.chat.id, media=media)

@dp.message_handler(lambda message: message.text == 'Диалог с Наставником #2')
async def m2(message: types.message):
    buttons = ['Зарегистрироваться', 'Подробнее о спикерах', 'Задать вопрос спикеру', 'В главное меню']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(*buttons)
    await message.answer(
        fmt.text(
            fmt.text('В рамках встречи "<i>Диалога с Наставником #1</i>" мы пообщаемся с профессионалами из сферы предпринимательства'),
            fmt.text(''),
            fmt.text('<b>3 причины, чтобы прийти:</b>'),
            fmt.text(''),
            fmt.text('-<b>Диалог с профи</b>: узнай об интересующее сфере деятельности от успешного профессионала и задай волнующие вопросы'),
            fmt.text(''),
            fmt.text('-<b>Подарки</b>: Получи в подарок фирменный мерч и книги, одобренные нашими Наставниками'),
            fmt.text(''),
            fmt.text('-<b>Нетворкинг</b>: познакомься с мотивированными ребятами с похожими интересами'),
            fmt.text(''),
            fmt.text('Мы подготовили ценные подарки для внимательных и креативных зрителей. Также мы представим каталог предпринимательских конкурсов и акселераторов для школьников, где ты сможешь прокачать своё бизнес-мышление, выиграть ценные призы и открыть своё прибыльное дело.'),
            fmt.text(''),
            fmt.text('Увидимся 8ого августа ;-)'),
            fmt.text(''),
            fmt.text('<a href="https://vk.com/nastavnikteam">Ссылка на группу ВКонтакте</a>'),
            sep="\n"
        ), parse_mode="HTML", reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text == 'Конкурс на лучший слоган')
async def slogan(message: types.message):
    buttons = ['Предложить свой слоган', 'В главное меню']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    keyboard.add(*buttons)
    await message.answer(
        fmt.text(
            fmt.text('В рамках встречи "<i>Диалога с Наставником #1</i>" мы проводим конкурс на лучший слоган'),
            fmt.text(''),
            fmt.text('<b>Для участия в конкурсе вам нужно просто написать свой слоган в данного бота</b>'),
            fmt.text(''),
            fmt.text('Победитель получит <b>худи</b> с нашим дизайном'),
            fmt.text(''),
            fmt.text('Пример слогана: <i>Узнавай, пробуй, выбирай</i>'),
            sep="\n"
        ), parse_mode="HTML", reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text == 'Предложить свой слоган')
async def sloganreply(message: types.message):
    await question.slogan_name.set()
    await message.answer('Напишите ваш слоган')

@dp.message_handler(state=question.slogan_name)
async def process_slogan(message: types.Message, state: FSMContext):
    buttons = 'В главное меню'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(buttons)
    await bot.send_message(chat_id=5974527080, text=f'Пользователь {message.from_user.mention} предложил(а) новый слоган: {message.text.lower()}')
    await bot.send_message(chat_id=5974527080,
                           text=f'Пользователь {message.from_user.mention} предложил(а) новый слоган: {message.text.lower()}')
    await bot.send_message(chat_id=5974527080,
                           text=f'Пользователь {message.from_user.mention} предложил(а) новый слоган: {message.text.lower()}')
    await bot.send_message(chat_id=5974527080,
                           text=f'Пользователь {message.from_user.mention} предложил(а) новый слоган: {message.text.lower()}')
    await bot.send_message(chat_id=5974527080,
                           text=f'Пользователь {message.from_user.mention} предложил(а) новый слоган: {message.text.lower()}')
    await state.finish()
    await message.answer('Ваш слоган был отправлен наставникам 👍', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Задать вопрос спикеру')
async def towhom(message: types.message):
    buttons = ['Тимофею Сигитову', 'Евгении Нелюбиной', 'Денису и Карине Ярыгиной', 'Ермолину Ивану']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    keyboard.add(*buttons)
    await question.speakers_name.set()
    await message.answer('Кому вы хотите задать вопрос?', reply_markup=keyboard)

@dp.message_handler(state='', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(lambda message: message.text not in ['Тимофею Сигитову', 'Евгении Нелюбиной', 'Денису и Карине Ярыгиной', 'Ермолину Ивану'], state=question.speakers_name)
async def process_name_invalid(message: types.Message):
    return await message.answer("Такого спикера нет. Выберите спикера из предложенного списка")

@dp.message_handler(state=question.speakers_name)
async def process_name(message: types.Message, state: FSMContext):
    await question.next()
    async with state.proxy() as data:
        data['name'] = message.text
    await message.reply("Напишите ваш вопрос")

@dp.message_handler(state=question.waiting_for_question)
async def process_question(message: types.Message, state: FSMContext):
    buttons = 'В главное меню'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(buttons)
    async with state.proxy() as data:
        namesp = data['name']
    await bot.send_message(chat_id=5974527080, text=f'Пришёл новый вопрос {namesp} от {message.from_user.mention} : {message.text.lower()}')
    await state.finish()
    await message.reply("Ваш вопрос был отправлен спикеру 👍", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Подробнее о спикерах')
async def speakers(message: types.message):
    buttons = ['Тимофей Сигитов', 'Евгения Нелюбина', 'Денис и Карина Ярыгины', 'Ермолин Иван', 'В главное меню']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*buttons)
    await message.answer('Выберите спикера, о котором хотите узнать подробнее', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == 'Тимофей Сигитов')
async def sp1(message: types.message):
    await message.answer(
        fmt.text(
            fmt.text('<b>Тимофей Сигитов</b> - совладелец киберспортивного клуба <i>Colizeum</i>'),
            fmt.text(''),
            fmt.text('<b>Тема: Кем быть - найм или предпринимательство?</b>'),
            fmt.text(''),
            fmt.text('- Миф про Бали: Запустил бизнес, настроил процессы и можно отдыхать - не верь в сказки!'),
            fmt.text(''),
            fmt.text('- Минусы и и плюсы найма: личный опыт в Mindbox и плюсы найма - каждому свой путь.'),
            fmt.text(''),
            fmt.text('- Один в поле воин: Почему важна команда и гибкие навыки?'),
            fmt.text(''),
            fmt.text('- Один раз подумай 7 раз сделай: Почему в бизнесе важно постоянно действовать?'),
            fmt.text(''),
            fmt.text('- Будем знакомы: пишите в ЛС, если нужна помощь.'),
            sep="\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(lambda message: message.text == 'Евгения Нелюбина')
async def sp2(message: types.message):
    await message.answer(
        fmt.text(
            fmt.text('<b>Евгения Нелюбина</b> - совладелица цветочного салона <i>FLOW</i>'),
            fmt.text(''),
            fmt.text('"<b>Тема: Личный бренд предпринимателя</b>"'),
            fmt.text(''),
            fmt.text('- Как найти бизнес-идею и воплотить мечту в жизнь?'),
            fmt.text(''),
            fmt.text('- Моя история: от МГИМО до FLOW'),
            fmt.text(''),
            fmt.text('- Личный бренд : что это и зачем он нужен?'),
            fmt.text(''),
            fmt.text('- Сферы предпринимательства, где важен ваш персональный брендинг'),
            fmt.text(''),
            fmt.text('- Ведение социальных сетей: Почему важно и как нужно?'),
            fmt.text(''),
            fmt.text('- Самопрезентация : Почему нужно уметь и любить рассказывать о себе?'),
            sep="\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(lambda message: message.text == 'Денис и Карина Ярыгины')
async def sp3(message: types.message):
    await message.answer(
        fmt.text(
            fmt.text('<b>Денис и Карина Ярыгины</b> - производители гриль-оборудования <i>ELBRUS HOME</i>'),
            fmt.text(''),
            fmt.text('<b>Тема: Новый рынок: как открыть, захватить и удержаться</b>'),
            fmt.text(''),
            fmt.text('- История ELBRUS’а: пробы и поиски ниши'),
            fmt.text(''),
            fmt.text('- Почему важна масштабируемость бизнеса?'),
            fmt.text(''),
            fmt.text('- Что понимают под новым рынком и зачем его «создавать»?'),
            fmt.text(''),
            fmt.text('- Как конкуренция рождает новые идеи, технологии, товары и услуги.'),
            fmt.text(''),
            fmt.text('- Как соответствовать рыночным трендам и задавать свои?'),
            fmt.text(''),
            fmt.text('- Почему команда - это ключевой фактор в бизнесе? Единомышленники vs наемные сотрудники'),
            sep="\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(lambda message: message.text == 'Ермолин Иван')
async def sp4(message: types.message):
    await message.answer(
        fmt.text(
            fmt.text('<b>Ермолин Иван</b> - основатель бренда <i>Molotov Streetwear</i>, магазина мультибрендовой одежды <i>Shkaf</i>, студии кастомизации <i>Custom.Works</i>'),
            fmt.text(''),
            fmt.text('<b>Тема: Создание фешн-бренда: пошаговая инструкция</b>'),
            fmt.text(''),
            fmt.text('- История бренда Molotov Streetwear'),
            fmt.text(''),
            fmt.text('- Как разработать концепцию бренда одежды?'),
            fmt.text(''),
            fmt.text('- Маркетинговая стратегия и позиционирование на рынке'),
            fmt.text(''),
            fmt.text('- Как создавать продающий контент?'),
            fmt.text(''),
            fmt.text('- Как масштабировать бизнес?'),
            fmt.text(''),
            fmt.text('- Синергия моих проектов'),
            sep="\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(lambda message: message.text == 'Зарегистрироваться')
async def registration(message: types.message):
    buttons = 'В главное меню'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    keyboard.add(buttons)
    await message.answer(
        fmt.text(
            fmt.text('Пройдите простую регистрацию по ссылке: <a href="https://leader-id.ru/events/311697"><b>ТЫК</b></a>'),
            sep="\n"
        ), parse_mode="HTML", reply_markup=keyboard
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)