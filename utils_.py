from typing import Literal

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from timepicker_types import (
    FullTimePickerAction, CarouselTimePickerAction, FullTimePickerCallback, CarouselTimePickerCallback
)


async def generate_selector(
    hour: int,
    minute: int,
    second: int,
    select_value: Literal["h", "m", "s"],
    actions_class: type[FullTimePickerAction] | type[CarouselTimePickerAction],
    callback_class: type[FullTimePickerCallback] | type[CarouselTimePickerCallback]
):
    match select_value:
        case "h":
            x_value = 6
            y_value = 4
            act = actions_class.SELECTED_HOUR
        case "m":
            x_value = 6
            y_value = 10
            act = actions_class.SELECTED_MINUTE
        case "s":
            x_value = 6
            y_value = 10
            act = actions_class.SELECTED_SECOND
        case _:
            raise ValueError("Incorrect select_value value. Available: 'h', 'm', 's'.")

    markup = []

    for i in range(y_value):
        markup.append(
            [
                InlineKeyboardButton(
                    text=value_index,
                    callback_data=callback_class(
                        act=act,
                        hour=value_index if select_value == "h" else hour,
                        minute=value_index if select_value == "m" else minute,
                        second=value_index if select_value == "s" else second
                    ).pack()
                )
                for value_index in range(i * x_value, (i + 1) * x_value)
            ]
        )

    keyboard = InlineKeyboardMarkup(inline_keyboard=markup)
    return keyboard
