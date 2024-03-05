import asyncio
import logging
import datetime
from aiogram import Bot, Dispatcher, executor
from aiogram.types import ParseMode, InputFile, Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.employee_data import employee_data
from bot.sort import sort_data
from adminID import admin_ID
from time_table import HOUR, MINUTE

API_TOKEN = '7146965175:AAGSMXPhI0KyISUWETmRAz2_YiOKKGvWukA'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    print(message)
    await message.answer("Assalomualeykum bu bot ishchilarni tug'ilgan kunini eslatib turuvchi bot!")


async def send_birthday_message(employee, chat_id):
    data = sort_data(employee)
    caption = data['caption']
    photo = data['image']
    await bot.send_photo(chat_id=chat_id, photo=photo, caption=caption, parse_mode=ParseMode.HTML)


async def check_birthday():
    employees = employee_data()

    today = datetime.date.today().strftime('%m-%d')

    for employee in employees:
        birthday = datetime.datetime.strptime(employee['birth_date'], '%Y-%m-%d').date()
        birthday = birthday.strftime('%m-%d')
        if birthday == today:
            for chat_id in admin_ID:
                await send_birthday_message(employee, chat_id)


async def send_message_time():
    await check_birthday()


async def scheduler():
    logging.basicConfig(level=logging.INFO)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_message_time, 'cron', hour=HOUR, minute=MINUTE)
    scheduler.start()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scheduler())
    executor.start_polling(dp, skip_updates=True)


