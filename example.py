from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command, Text

from full_timepicker import FullTimePicker, FullTimePickerCallback
from carousel_timepicker import CarouselTimePicker, CarouselTimePickerCallback


API_TOKEN = "your token here"

bot = Bot(API_TOKEN)
dispatcher = Dispatcher()


@dispatcher.message(Command(commands=["start"]))
async def start_command(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Full"), KeyboardButton(text="Carousel")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Choose timepicker: ", reply_markup=keyboard)


@dispatcher.message(Text(text="Full"))
async def full_timepicker_example(message: Message):
    text = "Select time:"
    keyboard = await FullTimePicker().start_picker()
    await message.answer(text=text, reply_markup=keyboard)


@dispatcher.callback_query(FullTimePickerCallback.filter())
async def full_timepicker_proceed(callback: CallbackQuery, callback_data: dict):
    selected, time = await FullTimePicker().process_selection(callback, callback_data)
    if selected:
        await callback.message.answer("You have selected: {}".format(str(time)))


@dispatcher.message(Text(text="Carousel"))
async def carousel_timepicker_example(message: Message):
    text = "Select time:"
    keyboard = await CarouselTimePicker().start_picker(mode="hms")
    await message.answer(text=text, reply_markup=keyboard)


@dispatcher.callback_query(CarouselTimePickerCallback.filter())
async def carousel_timepicker_proceed(callback: CallbackQuery, callback_data: dict):
    selected, time = await CarouselTimePicker().process_selection(callback, callback_data, mode="hms")
    if selected:
        await callback.message.answer("You have selected: {}".format(str(time)))


if __name__ == '__main__':
    dispatcher.run_polling(bot)


