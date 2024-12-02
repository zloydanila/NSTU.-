from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import emoji

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text= emoji.emojize(":herb:")+'Каталог')],
    [KeyboardButton(text= emoji.emojize(":information:")+'О нас'),  
    KeyboardButton(text= emoji.emojize(":check_box_with_check:")+'Пожелания')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню.')

object = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = f'Профильная Математика{emoji.emojize("💡")}', callback_data='MATH')],
    [InlineKeyboardButton(text = f'Русский язык{emoji.emojize("📚")}', callback_data='RUS')]
])

matan = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = f'Теория{emoji.emojize(":open_book:")}', callback_data='teory'), InlineKeyboardButton(text = f'Задания{emoji.emojize(":memo:")}', callback_data='task')],
    [InlineKeyboardButton(text = f'Вернуться назад{emoji.emojize("↩")}', callback_data='back3')]
])

teory  = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = f'Тестовая часть{emoji.emojize("📓")}', callback_data='test1'), InlineKeyboardButton(text = f'Вторая часть{emoji.emojize("🗂")}', callback_data='test2')],
    [InlineKeyboardButton(text = f'Вернуться назад{emoji.emojize("↩")}', callback_data='back2')]
])

task1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Номер 1. Планик', callback_data='zadanie11'), InlineKeyboardButton(text = 'Номер 2. Векторы', callback_data='zadanie21')],
    [InlineKeyboardButton(text = 'Номер 3. Стерео', callback_data='zadanie31'), InlineKeyboardButton(text = 'Номер 4. ТеорВер', callback_data='zadanie41')],
    [InlineKeyboardButton(text = 'Номер 5. ТеорВер+', callback_data='zadanie51'), InlineKeyboardButton(text = 'Номер 6. Уравнения', callback_data='zadanie61')],
    [InlineKeyboardButton(text = 'Номер 7. Вычисления', callback_data='zadanie71'), InlineKeyboardButton(text = 'Номер 8. Производная', callback_data='zadanie81')],
    [InlineKeyboardButton(text = 'Номер 9. Задачи', callback_data='zadanie91'), InlineKeyboardButton(text = 'Номер 10. Текст', callback_data='zadanie101')],
    [InlineKeyboardButton(text = 'Номер 11. Графики', callback_data='zadanie111'), InlineKeyboardButton(text = 'Номер 12. Функции', callback_data='zadanie121')],
    [InlineKeyboardButton(text = f'Вернуться назад{emoji.emojize("↩")}', callback_data='back4')]
])


test1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Номер 1. Планик', callback_data='zadanie1'), InlineKeyboardButton(text = 'Номер 2. Векторы', callback_data='zadanie2')],
    [InlineKeyboardButton(text = 'Номер 3. Стерео', callback_data='zadanie3'), InlineKeyboardButton(text = 'Номер 4. ТеорВер', callback_data='zadanie4')],
    [InlineKeyboardButton(text = 'Номер 5. ТеорВер+', callback_data='zadanie5'), InlineKeyboardButton(text = 'Номер 6. Уравнения', callback_data='zadanie6')],
    [InlineKeyboardButton(text = 'Номер 7. Вычисления', callback_data='zadanie7'), InlineKeyboardButton(text = 'Номер 8. Производная', callback_data='zadanie8')],
    [InlineKeyboardButton(text = 'Номер 9. Задачи', callback_data='zadanie9'), InlineKeyboardButton(text = 'Номер 10. Текст', callback_data='zadanie10')],
    [InlineKeyboardButton(text = 'Номер 11. Графики', callback_data='zadanie11'), InlineKeyboardButton(text = 'Номер 12. Функции', callback_data='zadanie12')],
    [InlineKeyboardButton(text = f'Вернуться назад{emoji.emojize("↩")}', callback_data='back1')]
])

teory1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = f'Тестовая часть{emoji.emojize("📓")}', callback_data='test11'), InlineKeyboardButton(text = f'Вторая часть{emoji.emojize("🗂")}', callback_data='test21')],
    [InlineKeyboardButton(text = f'Вернуться назад{emoji.emojize("↩")}', callback_data='back2')]
])


 