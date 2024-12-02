from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb
import emoji


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text = f'Привет, {message.from_user.first_name}{emoji.emojize(":waving_hand:")}! Добро пожаловать в "NSTU.ЕГЭ"!\n'
'Ваш личный помощник в подготовке к ЕГЭ!\n'
'\n'
'С помощью нашего бота вы сможете:\n'
'- Получить доступ к экспертным материалам: учебные планы, тесты, практические задания.\n'
'- Получить всю необходимую теоретическую информацию, необходимую для подготовки к экзаменам.\n'
'- Самостоятельно выбирать тот план подготовки который удобен именно вам.\n'
'\n'
f'Не оставляйте подготовку на последний момент – начинайте уже сегодня с NSTU.ЕГЭ!{emoji.emojize(":check_box_with_check:")}', 
                         reply_markup=kb.main)

@router.message(F.text == emoji.emojize(":herb:")+'Каталог')
async def predmet(message: Message):
    await message.answer(text = f'Мы предлагаем подготовку к 2 предметам{emoji.emojize("✔")}\n'
                         f'Тут ты можешь выбрать нужный тебе предмет{emoji.emojize("⬇")}',
                                 reply_markup=kb.object)

@router.callback_query(F.data == 'MATH')
async def matan(callback: CallbackQuery):
    await callback.answer('Вы выбрали математику')
    await callback.message.edit_text(f'Вы перешли на курс профильной математики!{emoji.emojize(":fire:")}\n'
                                    f'Здесь вы можете выбрать, какой раздел хотите изучить{emoji.emojize(":right_arrow_curving_down:")}' 
                                    ,reply_markup=kb.matan)
    
@router.callback_query(F.data == 'back3')
async def back(callback: CallbackQuery):
    await callback.message.edit_text(text=f'Мы предлагаем подготовку к 2 предметам{emoji.emojize("✔")}\n'
                                     f'Тут ты можешь выбрать нужный тебе предмет{emoji.emojize("⬇")}', reply_markup=kb.object)

@router.callback_query(F.data == 'teory')
async def test1(callback: CallbackQuery):
    await callback.answer('Вы выбрали теорию')
    await callback.message.edit_text(f'Здесь вы можете изучить теорию по всем номерам{emoji.emojize("⚡")}', reply_markup=kb.teory)

@router.callback_query(F.data == 'back2')
async def back(callback: CallbackQuery):
    await callback.message.edit_text(text=f'Вы перешли на курс профильной математики!{emoji.emojize(":fire:")}\n'
                                     f'Здесь вы можете выбрать, какой раздел хотите изучить{emoji.emojize(":right_arrow_curving_down:")}', reply_markup=kb.matan)

@router.callback_query(F.data == 'task')
async def test1(callback: CallbackQuery):
    await callback.answer('Вы выбрали раздел с заданиями')
    await callback.message.edit_text(f'Здесь вы можете выбрать, какие задания вы хотите отрешать{emoji.emojize("🖇")}', reply_markup=kb.teory1)

@router.callback_query(F.data == 'back4')
async def back(callback: CallbackQuery):
    await callback.message.edit_text(text=f'Вы перешли на курс профильной математики!{emoji.emojize(":fire:")}\n'
                                     f'Здесь вы можете выбрать, какой раздел хотите изучить{emoji.emojize(":right_arrow_curving_down:")}', reply_markup=kb.matan)

@router.callback_query(F.data == 'test1')
async def test1(callback: CallbackQuery):
    await callback.answer('Вы выбрали тестовую часть.')
    await callback.message.edit_text(f'Удачного изучения тестовой части!{emoji.emojize("💯")}', reply_markup=kb.test1)
    
@router.callback_query(F.data == 'back1')
async def back(callback: CallbackQuery):
    await callback.message.edit_text(text=f'Здесь вы можете изучить теорию по всем номерам{emoji.emojize("⚡")}', reply_markup=kb.matan)

@router.message(F.text == emoji.emojize(":information:")+"О нас")
async def byo(message: Message):
    await message.answer(text = 'Мы - группа студентов Новосибирского государственного технического университета (НГТУ НЭТИ), и мы хотим представить свой проект: телеграмм-бот по подготовке к ЕГЭ "NSTU.ЕГЭ"\n'
'\n'
'Так как мы сами совсем недавно готовились к ЕГЭ, мы знаем, как тяжело и порой не удобно изучать и практиковаться в заданиях.\n'
'\n'
'В нашем проекте минимизированы все проблемы и сложности, что делает процесс подготовки более качественным и удобным.')
    
@router.callback_query(F.data == 'zadanie1')
async def zadanie11(callback: CallbackQuery):
    await callback.answer('Вы выбрали 1 задание')
    await callback.message.answer_photo(photo='https://i.pinimg.com/originals/9a/e2/e4/9ae2e4fc5e94ff0dc304a8cc226364f0.jpg',
                                        caption= 'Удачного изучения планиметрии!')
    
@router.message(F.text == emoji.emojize(":check_box_with_check:")+'Пожелания')
async def pozhelaniya(message: Message):
    await message.answer(f"Тут вы можете оставить свои пожелания и предложения по улучшению тг-бота{emoji.emojize("📈")}\n"
                         f"Пишите их @ha1domo - один из авторов NSTU.ЕГЭ{emoji.emojize("👨‍💻")}")


