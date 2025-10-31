from aiogram import Bot, Dispatcher, F
from aiogram.types import Message,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
from aiogram.filters import CommandStart
import asyncio
from aiogram.fsm.context import FSMContext
from handlers.WeatherHandler import w_router
from decouple import config




BOT_TOKEN ='8284006780:AAFsIzPR_sQvklpBcToFFpVC6hxouGMIcpY'



bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handle(message: Message, state: FSMContext):
    key_board=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Farg'ona", callback_data ="region_Fergana"),InlineKeyboardButton(text="Samarkand",callback_data="region_Samarkand")],
        [InlineKeyboardButton(text="Andijon", callback_data="region_Andijan"),InlineKeyboardButton(text="Buxoro",callback_data="region_Bukhara")],
        [InlineKeyboardButton(text="Namangan", callback_data="region_Namangan"),InlineKeyboardButton(text="Xiva",callback_data="region_Khiva")],
        [InlineKeyboardButton(text="Toshkent", callback_data="region_Tashkent"),InlineKeyboardButton(text="Navoiy",callback_data="region_Navoiy")],

    ]
    
    )
    await message.answer("Assalomu alaykum , Xush kelibsiz.\nViloyatingizni tanlang",reply_markup=key_board)

    
    

async def main():
 print("bot ishga tushdi")
 dp.include_router(w_router)
 await dp.start_polling(bot)

asyncio.run(main())
