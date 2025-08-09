from aiogram import Bot, Dispatcher, F
from aiogram.types import Message,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
from aiogram.filters import CommandStart
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram import Router
from .WeatherApi import get_weather
from datetime import datetime


w_router=Router()


@w_router.message()
async def handle_message(message:Message):
    await message

@w_router.callback_query(F.data.startswith("region_"))
async def send_weather_info(callback_quary: CallbackQuery):
    vaqt=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    region=callback_quary.data.split("_")[1]
    weather=await get_weather(region)

    buttons=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Yangilash",callback_data=f"update_{region}")],
        [InlineKeyboardButton(text=" Orqaga ",callback_data="orqaga")],


    ])
   
    text=f"Viloyat nomi : {weather["name"]}\nHavo : {weather["weather"][0]["description"]}\nShamol tezligi : {weather["wind"]["speed"]}\nHarorat : {weather["main"]["temp_max"]}\n\n Hozirgi vaqt : {vaqt}"
    await callback_quary.message.edit_text(text,reply_markup=buttons)




@w_router.callback_query(F.data.startswith("update_"))
async def send_weather_info(callback_quary: CallbackQuery):
    vaqt=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    region=callback_quary.data.split("_")[1]
    weather=await get_weather(region)

    buttons=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Yangilash",callback_data=f"update_{region}")],
        [InlineKeyboardButton(text=" Orqaga ",callback_data="orqaga")],


    ])
   
    text=f"Viloyat nomi : {weather["name"]}\nHavo : {weather["weather"][0]["description"]}\nShamol tezligi : {weather["wind"]["speed"]}\nHarorat : {weather["main"]["temp_max"]}\n\n Hozirgi vaqt : {vaqt}"
    await callback_quary.message.edit_text(text,reply_markup=buttons)


@w_router.callback_query(F.data=="orqaga")
async def orqaga(callback_quary:CallbackQuery):
    key_board=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Farg'ona", callback_data ="region_Fergana"),InlineKeyboardButton(text="Samarkand",callback_data="region_Samarkand")],
        [InlineKeyboardButton(text="Andijon", callback_data="region_Andijan"),InlineKeyboardButton(text="Buxoro",callback_data="region_Bukhara")],
        [InlineKeyboardButton(text="Namangan", callback_data="region_Namangan"),InlineKeyboardButton(text="Xiva",callback_data="region_Khiva")],
        [InlineKeyboardButton(text="Toshkent", callback_data="region_Tashkent"),InlineKeyboardButton(text="Navoiy",callback_data="region_Navoiy")],
    ]
    
    )
    
    await callback_quary.message.edit_text("Viloyatingizni tanlang :",reply_markup=key_board)
