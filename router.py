from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from states import From
from aiogram.fsm.context import FSMContext
import aiohttp

router = Router()

@router.message(Command("start"))
async def start_command(msg: Message, state: FSMContext):
    await msg.answer("Salom! Botga xush kelibsiz 😊\nIltimos, yashayotgan shahringizni yozing:")
    await state.set_state(From.name)


@router.message(F.text, From.name)
async def name_harorat(msg: Message, state: FSMContext):
    WEATHER_API_KEY = '0766fe8dc91733f998894f7f8f1e42b6'
    city = msg.text.strip()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=uz"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                await msg.answer(f"🌍 {city} shahri:\n🌡 Harorat: {temp}°C\n📌 Holati: {desc}")
            else:
                await msg.answer("❌ Shahar topilmadi yoki xatolik yuz berdi. Iltimos, qaytadan urinib ko‘ring.")

    await state.clear()
