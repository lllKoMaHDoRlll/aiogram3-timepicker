from datetime import time

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from timepicker_types import FullTimePickerAction, FullTimePickerCallback


class FullTimePicker:

    @staticmethod
    async def start_picker(
            hour: int = 12,
            minute: int = 0
    ) -> InlineKeyboardMarkup:

        markup = list()

        # First row - increase/decrease buttons
        markup.append(
            [
                InlineKeyboardButton(
                    text="↑",
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.INCREASE_HOUR,
                        hour=hour,
                        minute=minute
                    ).pack()
                ),
                InlineKeyboardButton(
                    text="↓",
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.DECREASE_HOUR,
                        hour=hour,
                        minute=minute
                    ).pack()
                ),
                InlineKeyboardButton(
                    text="↑",
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.INCREASE_MINUTE,
                        hour=hour,
                        minute=minute
                    ).pack()
                ),
                InlineKeyboardButton(
                    text="↓",
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.DECREASE_MINUTE,
                        hour=hour,
                        minute=minute
                    ).pack()
                )
            ]
        )

        # Second row - current hour and minute
        markup.append(
            [
                InlineKeyboardButton(
                    text=str(hour),
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.SELECT_HOUR,
                        hour=hour,
                        minute=minute
                    ).pack()
                ),
                InlineKeyboardButton(
                    text=str(minute),
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.SELECT_MINUTE,
                        hour=hour,
                        minute=minute
                    ).pack()
                )
            ]
        )

        # Third row - confirm button
        markup.append(
            [
                InlineKeyboardButton(
                    text="Confirm",
                    callback_data=FullTimePickerCallback(
                        act=FullTimePickerAction.CONFIRM,
                        hour=hour,
                        minute=minute
                    ).pack()
                )
            ]
        )

        keyboard = InlineKeyboardMarkup(inline_keyboard=markup)
        return keyboard

    @staticmethod
    async def get_hours_selector(hour: int, minute: int) -> InlineKeyboardMarkup:
        markup = []
        for i in range(4):
            markup.append(
                [
                    InlineKeyboardButton(
                        text=hour_index,
                        callback_data=FullTimePickerCallback(
                            act=FullTimePickerAction.SELECTED_HOUR,
                            hour=hour_index,
                            minute=minute
                        ).pack()
                    )
                    for hour_index in range(i * 6, i * 6 + 6)
                ]
            )
        keyboard = InlineKeyboardMarkup(inline_keyboard=markup)
        return keyboard

    @staticmethod
    async def get_minutes_selector(hour: int, minute: int) -> InlineKeyboardMarkup:
        markup = []
        for i in range(6):
            markup.append(
                [
                    InlineKeyboardButton(
                        text=minute_index,
                        callback_data=FullTimePickerCallback(
                            act=FullTimePickerAction.SELECTED_MINUTE,
                            hour=hour,
                            minute=minute_index
                        ).pack()
                    )
                    for minute_index in range(i * 10, i * 10 + 10)
                ]
            )
        keyboard = InlineKeyboardMarkup(inline_keyboard=markup)
        return keyboard

    async def process_selection(self, query: CallbackQuery, data: [CallbackData, FullTimePickerCallback]) -> tuple:
        return_data = (False, None)

        match data.act:
            case FullTimePickerAction.CONFIRM:
                return_data = True, time(hour=int(data.hour), minute=int(data.minute))
            case FullTimePickerAction.INCREASE_HOUR:
                next_time = time(
                    hour=(int(data.hour) + 1) % 24,
                    minute=int(data.minute)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(next_time.hour, next_time.minute)
                )
            case FullTimePickerAction.DECREASE_HOUR:
                prev_time = time(
                    hour=(int(data.hour) - 1) % 24,
                    minute=int(data.minute)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(prev_time.hour, prev_time.minute)
                )
            case FullTimePickerAction.INCREASE_MINUTE:
                next_time = time(
                    hour=int(data.hour),
                    minute=(int(data.minute) + 1) % 60
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(next_time.hour, next_time.minute))
            case FullTimePickerAction.DECREASE_MINUTE:
                prev_time = time(
                    hour=int(data.hour),
                    minute=(int(data.minute) - 1) % 60
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(prev_time.hour, prev_time.minute))
            case FullTimePickerAction.SELECT_HOUR:
                keyboard = await self.get_hours_selector(data.hour, data.minute)
                await query.message.edit_reply_markup(reply_markup=keyboard)
            case FullTimePickerAction.SELECT_MINUTE:
                keyboard = await self.get_minutes_selector(data.hour, data.minute)
                await query.message.edit_reply_markup(reply_markup=keyboard)
            case FullTimePickerAction.SELECTED_HOUR | FullTimePickerAction.SELECTED_MINUTE:
                await query.message.edit_reply_markup(reply_markup=await self.start_picker(data.hour, data.minute))
            case _:
                raise ValueError("Incorrect timepicker action: {}".format(data.act))
        return return_data
