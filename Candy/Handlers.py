from aiogram.types import Message, location
from aiogram.dispatcher.filters import Text
from Config import dp
import Text
import Game
import random
from Keyboard import kb_new, kb_stop
from datetime import datetime

@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name}{Text.greeting}', reply_markup=kb_new)

    user = []
    user.append(datetime.now())
    user.append(message.from_user.full_name)
    user.append(message.from_user.id)
    user.append(message.from_user.username)
    user = list(map(str, user))
    with open('log.txt', 'a', encoding='UTF-8') as data:
        data.write(' ▲ '.join(user)+'\n')

@dp.message_handler(commands=['new_game'])
async def start_new_game(message: Message):
    if Game.check_game():
        Game.set_total_to_max()
    else:
        Game.new_game()
    if Game.check_game():
        toss = random.choice([True, False])
        if toss:
            await player_turn(message)
        else:
            await bot_turn(message)


@dp.message_handler(commands=['stop_game'])
async def stop_game(message):
    Game.new_game()
    await message.reply('ИГРА ОКОНЧЕНА', reply_markup=kb_new)

@dp.message_handler(commands=['set_total'])
async def set_total_candies(message: Message):
    if not Game.check_game():
        max_total = message.text.split()
        if len(max_total) > 1 and max_total[1].isdigit():
            Game.set_max_total(int(max_total[1]))
            await message.reply(text=f'Максимальное кол-во конфет изменено на {max_total[1]}')
        else:
            await message.reply(text='Этой коммандой можно настроить максимально кол-во конфет. Введите \n/set_total ... , где "..." целое число ')
    else:
        await message.reply(text='Эту настройку можно изменить только после окончания партии')


@dp.message_handler(commands=['level'])
async def set_bot_level(message: Message):
    if not Game.check_game():
        Game.change_level()
        await message.reply(text=f'Уровень сложности установлен: {Game.get_bot_level()}')
    else:
        await message.reply(text='Эту настройку можно изменить только после окончания партии')


async def player_turn(message: Message):
    await message.answer(f'{message.from_user.first_name}, твой ход! Сколько возьмешь конфет?', reply_markup=kb_stop)


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
    take = 0
    if Game.get_bot_level() == 'Light':
        if total <= 28:
            take = total
        else:
            take = random.randint(1, 28)
    else:
        if total <= 28:
            take = total
        else:
            var = (Game.get_total()%29)
            take = var if var > 0 else random.randint(1,28)
    Game.take_candies(take)
    await message.answer(f'Бот взял {take} конфет и их осталось {Game.get_total()}')
    if await check_win(message, take, 'Бот'):
        return
    await player_turn(message)


async def check_win(message, take: int, player: str):
    if Game.get_total() <= 0:
        if player == 'player':
            await message.answer(
                f'ПОБЕДА !!! {message.from_user.first_name} взял {take} конфет(ы) и одержал победу над железякой! Для новой игры введи /new_game')
        else:
            await message.answer(
                f' Как же так {message.from_user.first_name} 0_0 ? Бот взял {take} конфет(ы) и одержал победу над тобой. Для новой игры введи /new_game')

        Game.new_game()
        return True
    else:
        return False
