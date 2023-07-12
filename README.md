# aiogram3-timepicker

## Usage:

```

from aiogram3_timepicker.full_timepicker import FullTimePicker, FullTimePickerCallback
...

@dispatcher.message(Command(commands=["start"]))
async def start_command(message: Message) -> None:
    keyboard = await FullTimePicker().start_picker()
    await message.answer("Hello! This is your Time picker. Try it out!", reply_keyboard=keyboard)

@dispatcher.callback_query(FullTimePickerCallback.filter())
async def proceed_response(callback: CallbackQuery, callback_data: dict):
    selected, time = await FullTimePicker().process_selection(callback, callback_data)
    if selected:
        await callback.message.answer("Your time is: {}".format(time))        

```

## Result:

![image](https://github.com/lllKoMaHDoRlll/aiogram3-timepicker/assets/88376471/92bb2ba0-5dae-42b4-8f95-0555d5e4dc40)

![image](https://github.com/lllKoMaHDoRlll/aiogram3-timepicker/assets/88376471/d78517e2-d914-4290-a770-7298b6054a13)
