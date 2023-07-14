from datetime import time
from typing import Literal

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from timepicker_types import FullTimePickerAction, FullTimePickerCallback


class FullTimePicker:

    @staticmethod
    async def start_picker(
            hour: int = 12,
            minute: int = 0,
            second: int = 0,
            mode: str = "hm"
    ) -> InlineKeyboardMarkup:

        markup = [[], [], []]

        # First row - increase/decrease buttons
        # Second row - current hour and minute and second (each value is optional)
        # Third row - confirm button

        if "h" in mode:
            markup[0] += [
                    InlineKeyboardButton(
                        text="↑",
                        callback_data=FullTimePickerCallback(
                            act=FullTimePickerAction.INCREASE_HOUR,
                            hour=hour,
                            minute=minute,
                            second=second
                        ).pack()
                    ),
                    InlineKeyboardButton(
                        text="↓",
                        callback_data=FullTimePickerCallback(
                            act=FullTimePickerAction.DECREASE_HOUR,
                            hour=hour,
                            minute=minute,
                            second=second
                        ).pack()
                    )
                ]
            markup[1] += [
                InlineKeyboardButton(
                    text=str(hour),
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.SELECT_HOUR,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]

        if "m" in mode:
            markup[0] += [
                InlineKeyboardButton(
                    text="↑",
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.INCREASE_MINUTE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                ),
                InlineKeyboardButton(
                    text="↓",
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.DECREASE_MINUTE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
            markup[1] += [
                InlineKeyboardButton(
                    text=str(minute),
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.SELECT_MINUTE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]

        if "s" in mode:
            markup[0] += [
                InlineKeyboardButton(
                    text="↑",
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.INCREASE_SECOND,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                ),
                InlineKeyboardButton(
                    text="↓",
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.DECREASE_SECOND,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
            markup[1] += [
                InlineKeyboardButton(
                    text=str(second),
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.SELECT_SECOND,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]

        markup[2] += [
                InlineKeyboardButton(
                    text="Confirm",
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.CONFIRM,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
        ]

        keyboard = InlineKeyboardMarkup(inline_keyboard=markup)
        return keyboard

    @staticmethod
    async def _generate_selector(hour: int, minute: int, second: int, select_value: Literal["h", "m", "s"]):
        match select_value:
            case "h":
                x_value = 6
                y_value = 4
                act = FullTimePickerAction.SELECTED_HOUR
            case "m":
                x_value = 6
                y_value = 10
                act = FullTimePickerAction.SELECTED_MINUTE
            case "s":
                x_value = 6
                y_value = 10
                act = FullTimePickerAction.SELECTED_SECOND
            case _:
                raise ValueError("Incorrect select_value value. Available: 'h', 'm', 's'.")

        markup = []

        for i in range(y_value):
            markup.append(
                [
                    InlineKeyboardButton(
                        text=value_index,
                        callback_data=FullTimePickerCallback(
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

    async def process_selection(
            self, query: CallbackQuery, data: [CallbackData, FullTimePickerCallback], mode: str = "hm") -> tuple:

        return_data = (False, None)

        match data.act:
            case FullTimePickerAction.CONFIRM:
                return_data = True, time(hour=int(data.hour), minute=int(data.minute), second=int(data.second))
            case FullTimePickerAction.INCREASE_HOUR:
                next_time = time(
                    hour=(int(data.hour) + 1) % 24,
                    minute=int(data.minute),
                    second=int(data.second)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(next_time.hour, next_time.minute, next_time.second, mode)
                )
            case FullTimePickerAction.DECREASE_HOUR:
                prev_time = time(
                    hour=(int(data.hour) - 1) % 24,
                    minute=int(data.minute),
                    second=int(data.second)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(prev_time.hour, prev_time.minute, prev_time.second, mode))
            case FullTimePickerAction.INCREASE_MINUTE:
                next_time = time(
                    hour=int(data.hour),
                    minute=(int(data.minute) + 1) % 60,
                    second=int(data.second)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(next_time.hour, next_time.minute, next_time.second, mode))
            case FullTimePickerAction.DECREASE_MINUTE:
                prev_time = time(
                    hour=int(data.hour),
                    minute=(int(data.minute) - 1) % 60,
                    second=int(data.second)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(prev_time.hour, prev_time.minute, prev_time.second, mode))
            case FullTimePickerAction.INCREASE_SECOND:
                next_time = time(
                    hour=int(data.hour),
                    minute=int(data.minute),
                    second=(int(data.second) + 1) % 60
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(next_time.hour, next_time.minute, next_time.second, mode))
            case FullTimePickerAction.DECREASE_SECOND:
                prev_time = time(
                    hour=int(data.hour),
                    minute=int(data.minute),
                    second=(int(data.second) - 1) % 60
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(prev_time.hour, prev_time.minute, prev_time.second, mode))
            case FullTimePickerAction.SELECT_HOUR:
                keyboard = await self._generate_selector(data.hour, data.minute, data.second, "h")
                await query.message.edit_reply_markup(reply_markup=keyboard)
            case FullTimePickerAction.SELECT_MINUTE:
                keyboard = await self._generate_selector(data.hour, data.minute, data.second, "m")
                await query.message.edit_reply_markup(reply_markup=keyboard)
            case FullTimePickerAction.SELECT_SECOND:
                keyboard = await self._generate_selector(data.hour, data.minute, data.second, "s")
                await query.message.edit_reply_markup(reply_markup=keyboard)
            case FullTimePickerAction.SELECTED_HOUR | FullTimePickerAction.SELECTED_MINUTE | FullTimePickerAction.SELECTED_SECOND:
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(data.hour, data.minute, data.second, mode))
            case _:
                raise ValueError("Incorrect timepicker action: {}".format(data.act))
        return return_data
