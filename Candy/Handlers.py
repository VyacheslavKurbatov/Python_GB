from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from Config import dp
import Text
import Game
import random


# @dp.message_handler(commands=['start'])
# async def on_start(message: Message):
#   await message.answer(text=f'{message.from_user.first_name}, че нада?')

# @dp.message_handler(Text(equals=('100', '101')))
# async def on_hundred(message: Message):
#   await message.answer(text=f'Шеф, гляди! Я поймал тебе цифры!')


# @dp.message_handler()
# async def all_handler(message: Message):
#   if message.text.isdigit():
#     await message.answer(text=f'Шеф, гляди! Я поймал тебе ЦИФЕРКУ!')
#   else:
#     await message.answer(text=f'Фу, какая хрень')

@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name}{Text.greeting}')


@dp.message_handler(commands=['new_game'])
async def start_new_game(message: Message):
    Game.new_game()
    if Game.check_game():
        toss = random.randint(0, 2)
        if toss:
            await player_turn(message)
        else:
            await bot_turn(message)


async def player_turn(message: Message):
    await message.answer(f'{message.from_user.first_name}, твой ход! Сколько возьмешь конфет?')


@dp.message_handler()
async def take(message: Message):
    name = message.from_user.first_name

    if Game.check_game():
        if message.text.isdigit():
            take = int(message.text)
            if (0 < take < 29) and take <= Game.get_total():
                Game.take_candies(take)
                if await check_win(message, take, 'player'):
                    return
                await message.answer(f'{name} взял {take} конфет и на столе осталось {Game.get_total()}. Ходит бот ...')
                await bot_turn(message)
            elif take > 28:
                await message.answer('Что-то ты многовато взял! Надо от 1 до 28')
            elif take < 1:
                await message.answer('Не стесняйся, бери конфеты')
            elif take > Game.get_total():
                await message.answer(f'Осталось всего {Game.get_total()} конфет, больше взять не получится')
            else:
                await message.answer(f'Вводи ЧИСЛА от 1 до 28')
        else:
            pass


async def bot_turn(message):
    total = Game.get_total()
    if total <= 28:
        take = total
    else:
        take = random.randint(1, 28)
    Game.take_candies(take)
    await message.answer(f'Бот взял {take} конфет и их осталось {Game.get_total()}')
    if await check_win(message, take, 'Бот'):
        return
    await player_turn(message)

async def check_win(message, take: int, player: str):
    if Game.get_total() <= 0:
        if player == 'player':
            await message.answer(f'ПОБЕДА !!! {message.from_user.first_name} взял {take} конфет(ы) и одержал победу над железякой! Для новой игры введи /new_game')
        else:
            await message.answer(f' Как же так {message.from_user.first_name} 0_0 ? Бот взял {take} конфет(ы) и одержал победу над тобой. Для новой игры введи /new_game')

        Game.new_game()
        return True
    else:
        return False

