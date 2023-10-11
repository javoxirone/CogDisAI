import asyncio
import sys
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, CallbackQuery
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
import logging

from aiogram.utils.keyboard import KeyboardBuilder

TOKEN = '6673961294:AAGhUWqKwfzlSxYEzxh_kiRM9DnFMzekkhI'

dp = Dispatcher()


@dp.message(Command('help', 'start'))
async def command_start_handler(message: Message) -> None:
    item1 = InlineKeyboardButton(text="Daily Check In", callback_data='check_in')
    item2 = InlineKeyboardButton(text="Daily Gratitude", callback_data='gratitude')
    item3 = InlineKeyboardButton(text="CBT Diary", callback_data='cbt_diary')
    builder = KeyboardBuilder(button_type=InlineKeyboardButton)
    builder.add(item1, item2, item3)
    markup = InlineKeyboardMarkup(inline_keyboard=builder.export())
    await message.answer("Hello! I'm your AI Consultant. How can I assist you today?", reply_markup=markup)


CHECK_IN_STATE = {
    'question1': 'How do you feel today? (Scale 1-5)',
    'question2': 'What emotions are you experiencing?',
    'question3': 'Describe a moment that made you ___ today?'
}


@dp.callback_query(lambda c: c.data == 'check_in')
async def process_callback_check_in(callback_query: CallbackQuery):
    print(callback_query.id)
    await callback_query.answer(CHECK_IN_STATE['question1'])


@dp.callback_query(lambda c: c.data == 'gratitude')
async def process_callback_gratitude(callback_query: CallbackQuery):
    print(callback_query.id)
    await callback_query.answer(CHECK_IN_STATE['question2'])


@dp.callback_query(lambda c: c.data == 'cbt_diary')
async def process_callback_cbt_diary(callback_query: CallbackQuery):
    print(callback_query.id)
    await callback_query.answer(CHECK_IN_STATE['question3'])


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

# Define the language choices
# def get_language_keyboard():
#     keyboard = InlineKeyboardMarkup()
#     keyboard.row(
#         InlineKeyboardButton("🇷🇺 Russian", callback_data="language_russian"),
#         InlineKeyboardButton("🇺🇸 English", callback_data="language_english")
#     )
#     return keyboard
#
# button1 = InlineKeyboardButton(text="🇷🇺 Russian", callback_data="russian_button")
# button2 = InlineKeyboardButton(text="🇺🇸 English", callback_data="language_english")
# keyboard_inline = InlineKeyboardMarkup().add(button1, button2)
#
# keyboard1= ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("🇷🇺 Russian", "🇺🇸 English")
#
# @dp.message_handler(commands=['start'])
# async def on_start(message: types.Message):
#     # await message.answer("Welcomd to CogDis AI", reply_markup=keyboard1)
#     await message.answer("Выберите язык / Choose language:", reply_markup=keyboard_inline)

# @dp.message_handler(commands=['language'])
# async def language(message: types.Message):
#     await message.reply("Выберите язык / Choose language:", reply_markup=keyboard_inline)


# @dp.callback_query_handler(text=['language_russian', 'language_english'])
# async def language_selected(call: types.CallbackQuery):
#
#     if call.data == "language_russian":
#         response = "Вы выбрали русский язык!"
#         await call.message.reply("Вы выбрали русский язык!")
#     if call.data == "language_english":
#         response = "You've chosen English!"
#         await call.message.reply("You've chosen English!")
#
#     await call.answer()

#
# @dp.callback_query_handler(lambda query: query.data in ["russian_button", "english_button"])
# async def handle_button_click(query: types.CallbackQuery):
#     # Get the button data
#     button_data = query.data
#
#     # Send a message based on the button clicked
#     if button_data == "russian_button":
#         await query.message.answer("Вы выбрали русский язык!")
#     elif button_data == "english_button":
#         await query.message.answer("You have chosen English language!")

# @dp.message_handler()
# async def selected_language(message: types.Message):
#     if message.text == "🇷🇺 Russian":
#         await message.reply("Hi! How are you?")
#     elif message.text == "🇺🇸 English":
#         await message.reply("https://youtube.com/gunthersuper")
#     else:
#         await message.reply(f"Your message is: {message.text}")


# Handler for the /start command
# @dp.message_handler(commands=['start'])
# async def on_start(message: types.Message):
#     keyboard = get_language_keyboard()
#     await message.answer("Выберите язык / Choose language:", reply_markup=keyboard)


# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('language_'))
# async def language_selected(callback_query: types.CallbackQuery):
#     language = callback_query.data.split('_')[1]
#
#     if language == "russian":
#         response = "Вы выбрали русский язык!"
#     elif language == "english":
#         response = "You've chosen English!"
#
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, response)


#
# MESSAGES = {
#     "english": {
#         "how_to_use": "Here's how to use this bot: ...",
#         "greeting": "Hello! How can I assist you today?",
#         # ... other English messages ...
#     },
#     "russian": {
#         "how_to_use": "Вот как использовать этого бота: ...",
#         "greeting": "Привет! Как я могу вам помочь сегодня?",
#         # ... other Russian messages ...
#     }
# }
#
#
# user_languages = {}  # user_id: language
#
#
# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('language_'))
# async def language_selected(callback_query: types.CallbackQuery):
#     language = callback_query.data.split('_')[1]
#
#     # Store the user's language preference
#     user_languages[callback_query.from_user.id] = language
#
#     # Send the "how to use" message in the selected language
#     response = MESSAGES[language]["how_to_use"]
#
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, response)
#
#
# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('language_'))
# async def language_selected(callback_query: types.CallbackQuery):
#     language = callback_query.data.split('_')[1]
#
#     # Store the user's language preference
#     user_languages[callback_query.from_user.id] = language
#
#     # Send the "how to use" message in the selected language
#     how_to_use_response = MESSAGES[language]["how_to_use"]
#     await bot.send_message(callback_query.from_user.id, how_to_use_response)
#
#     # Send the greeting message in the selected language
#     greeting_response = MESSAGES[language]["greeting"]
#     await bot.send_message(callback_query.from_user.id, greeting_response)
#
#     # Answer the callback query (important to make the "loading" animation on the button go away)
#     await bot.answer_callback_query(callback_query.id)
#
#


#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
