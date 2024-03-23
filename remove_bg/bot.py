



import asyncio
import logging
import sys 
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message,CallbackQuery,FSInputFile
from mybuttons import colours_inline_button
from myremovebg import bg_change_color
from aiogram.client.session.aiohttp import AiohttpSession

TOKEN = "6747702351:AAHovbu0HzQGsoY2LrgMPuCeWChXVTfqUD8"
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Assalomu alaykum, foto yuboring")

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(F.photo)
async def name(message:Message):
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"white")
    if rasm:
        await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="start-remove.png"),reply_markup=colours_inline_button)
        # await message.answer_document(document=types.input_file.BufferedInputFile(rasm,filename="no-remove.png"))

@dp.callback_query(F.data == "red")
async def colours_changes(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"red")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="red-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()

@dp.callback_query(F.data == "black")
async def colours_changes_black(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"black")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="black-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()
    
@dp.callback_query(F.data == "brown")
async def colours_changes_brown(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"brown")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="brown-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()
    
@dp.callback_query(F.data == "yellow")
async def colours_changes_yellow(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"yellow")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="yellow-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()
    
@dp.callback_query(F.data == "blue")
async def colours_changes_blue(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"blue")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="blue-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()

@dp.callback_query(F.data == "green")
async def colours_changes_green(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"green")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="green-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()
    
@dp.callback_query(F.data == "purple")
async def colours_changes_purple(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"purple")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="purple-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()

@dp.callback_query(F.data == "pink")
async def colours_changes_pink(callback:CallbackQuery):
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = bg_change_color(photos_url,"pink")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="pink-remove.png"),reply_markup=colours_inline_button)
    await callback.message.delete()


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
 

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
