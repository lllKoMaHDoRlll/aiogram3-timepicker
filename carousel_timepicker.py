from datetime import time

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery

from timepicker_types import CarouselTimePickerAction, CarouselTimePickerCallback
from utils_ import generate_selector


class CarouselTimePicker:

    @staticmethod
    async def start_picker(
            hour: int = 12,
            minute: int = 0,
            second: int = 0,
            mode: str = "hm"
    ) -> InlineKeyboardMarkup:

        markup = [[], [], [], [], [], []]

        # First and Second rows - increase buttons
        # Third row - current hour and minute and second (each value is optional)
        # Fourth and Fifth rows - decrease buttons
        # Sixth row - confirm button

        if "h" in mode:
            markup[0] += [
                    InlineKeyboardButton(
                        text=" ",
                        callback_data=CarouselTimePickerCallback(
                            act=CarouselTimePickerAction.IGNORE,
                            hour=hour,
                            minute=minute,
                            second=second
                        ).pack()
                    ),
                    InlineKeyboardButton(
                        text=str((int(hour) + 5) % 24),
                        callback_data=CarouselTimePickerCallback(
                            act=CarouselTimePickerAction.INCREASE_HOUR_BY_5,
                            hour=hour,
                            minute=minute,
                            second=second
                        ).pack()
                    )
                ]
            markup[1] += [
                InlineKeyboardButton(
                    text=" ",
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.IGNORE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                ),
                InlineKeyboardButton(
                    text=str((int(hour) + 1) % 24),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.INCREASE_HOUR_BY_1,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
            markup[2] += [
                InlineKeyboardButton(
                    text=str(hour),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.SELECT_HOUR,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
            markup[3] += [
                InlineKeyboardButton(
                    text=" ",
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.IGNORE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                ),
                InlineKeyboardButton(
                    text=str((int(hour) - 1) % 24),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.DECREASE_HOUR_BY_1,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
            markup[4] += [
                InlineKeyboardButton(
                    text=" ",
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.IGNORE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                ),
                InlineKeyboardButton(
                    text=str((int(hour) - 5) % 24),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.DECREASE_HOUR_BY_5,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]

        if "m" in mode:
            markup[0] += [
                InlineKeyboardButton(
                    text=" ",
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.IGNORE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                ),
                InlineKeyboardButton(
                    text=str((int(minute) + 5) % 60),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.INCREASE_MINUTE_BY_5,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
            markup[1] += [
                InlineKeyboardButton(
                    text=" ",
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.IGNORE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                ),
                InlineKeyboardButton(
                    text=str((int(minute) + 1) % 60),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.INCREASE_MINUTE_BY_1,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
            markup[2] += [
                InlineKeyboardButton(
                    text=str(minute),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.SELECT_MINUTE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
            markup[3] += [
                InlineKeyboardButton(
                    text=" ",
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.IGNORE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                ),
                InlineKeyboardButton(
                    text=str((int(minute) - 1) % 60),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.DECREASE_MINUTE_BY_1,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
            markup[4] += [
                InlineKeyboardButton(
                    text=" ",
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.IGNORE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                ),
                InlineKeyboardButton(
                    text=str((int(minute) - 5) % 60),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.DECREASE_MINUTE_BY_5,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]

        if "s" in mode:
            markup[0] += [
                InlineKeyboardButton(
                    text=" ",
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.IGNORE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                ),
                InlineKeyboardButton(
                    text=str((int(second) + 5) % 60),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.INCREASE_SECOND_BY_5,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
            markup[1] += [
                InlineKeyboardButton(
                    text=" ",
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.IGNORE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                ),
                InlineKeyboardButton(
                    text=str((int(second) + 1) % 60),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.INCREASE_SECOND_BY_1,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
            markup[2] += [
                InlineKeyboardButton(
                    text=str(second),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.SELECT_SECOND,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
            markup[3] += [
                InlineKeyboardButton(
                    text=" ",
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.IGNORE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                ),
                InlineKeyboardButton(
                    text=str((int(second) - 1) % 60),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.DECREASE_SECOND_BY_1,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
            markup[4] += [
                InlineKeyboardButton(
                    text=" ",
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.IGNORE,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                ),
                InlineKeyboardButton(
                    text=str((int(second) - 5) % 60),
                    callback_data=CarouselTimePickerCallback(
                        act=CarouselTimePickerAction.DECREASE_SECOND_BY_5,
                        hour=hour,
                        minute=minute,
                        second=second
                    ).pack()
                )
            ]
        markup[0] += [
            InlineKeyboardButton(
                text=" ",
                callback_data=CarouselTimePickerCallback(
                    act=CarouselTimePickerAction.IGNORE,
                    hour=hour,
                    minute=minute,
                    second=second
                ).pack()
            )
        ]
        markup[1] += [
            InlineKeyboardButton(
                text=" ",
                callback_data=CarouselTimePickerCallback(
                    act=CarouselTimePickerAction.IGNORE,
                    hour=hour,
                    minute=minute,
                    second=second
                ).pack()
            )
        ]
        markup[3] += [
            InlineKeyboardButton(
                text=" ",
                callback_data=CarouselTimePickerCallback(
                    act=CarouselTimePickerAction.IGNORE,
                    hour=hour,
                    minute=minute,
                    second=second
                ).pack()
            )
        ]
        markup[4] += [
            InlineKeyboardButton(
                text=" ",
                callback_data=CarouselTimePickerCallback(
                    act=CarouselTimePickerAction.IGNORE,
                    hour=hour,
                    minute=minute,
                    second=second
                ).pack()
            )
        ]

        markup[5] += [
            InlineKeyboardButton(
                text="Confirm",
                callback_data=CarouselTimePickerCallback(
                    act=CarouselTimePickerAction.CONFIRM,
                    hour=hour,
                    minute=minute,
                    second=second
                ).pack()
            )
        ]

        keyboard = InlineKeyboardMarkup(inline_keyboard=markup)
        return keyboard

    async def process_selection(
            self, query: CallbackQuery, data: [CallbackData, CarouselTimePickerCallback], mode: str = "hm") -> tuple:

        return_data = (False, None)

        match data.act:
            case CarouselTimePickerAction.CONFIRM:
                return_data = True, time(hour=int(data.hour), minute=int(data.minute), second=int(data.second))
            case CarouselTimePickerAction.INCREASE_HOUR_BY_5:
                next_time = time(
                    hour=(int(data.hour) + 5) % 24,
                    minute=int(data.minute),
                    second=int(data.second)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(next_time.hour, next_time.minute, next_time.second, mode)
                )
            case CarouselTimePickerAction.INCREASE_HOUR_BY_1:
                next_time = time(
                    hour=(int(data.hour) + 1) % 24,
                    minute=int(data.minute),
                    second=int(data.second)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(next_time.hour, next_time.minute, next_time.second, mode)
                )
            case CarouselTimePickerAction.DECREASE_HOUR_BY_5:
                prev_time = time(
                    hour=(int(data.hour) - 5) % 24,
                    minute=int(data.minute),
                    second=int(data.second)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(prev_time.hour, prev_time.minute, prev_time.second, mode))
            case CarouselTimePickerAction.DECREASE_HOUR_BY_1:
                prev_time = time(
                    hour=(int(data.hour) - 1) % 24,
                    minute=int(data.minute),
                    second=int(data.second)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(prev_time.hour, prev_time.minute, prev_time.second, mode))
            case CarouselTimePickerAction.INCREASE_MINUTE_BY_5:
                next_time = time(
                    hour=int(data.hour),
                    minute=(int(data.minute) + 5) % 60,
                    second=int(data.second)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(next_time.hour, next_time.minute, next_time.second, mode))
            case CarouselTimePickerAction.INCREASE_MINUTE_BY_1:
                next_time = time(
                    hour=int(data.hour),
                    minute=(int(data.minute) + 1) % 60,
                    second=int(data.second)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(next_time.hour, next_time.minute, next_time.second, mode))
            case CarouselTimePickerAction.DECREASE_MINUTE_BY_5:
                prev_time = time(
                    hour=int(data.hour),
                    minute=(int(data.minute) - 5) % 60,
                    second=int(data.second)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(prev_time.hour, prev_time.minute, prev_time.second, mode))
            case CarouselTimePickerAction.DECREASE_MINUTE_BY_1:
                prev_time = time(
                    hour=int(data.hour),
                    minute=(int(data.minute) - 1) % 60,
                    second=int(data.second)
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(prev_time.hour, prev_time.minute, prev_time.second, mode))
            case CarouselTimePickerAction.INCREASE_SECOND_BY_5:
                next_time = time(
                    hour=int(data.hour),
                    minute=int(data.minute),
                    second=(int(data.second) + 5) % 60
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(next_time.hour, next_time.minute, next_time.second, mode))
            case CarouselTimePickerAction.INCREASE_SECOND_BY_1:
                next_time = time(
                    hour=int(data.hour),
                    minute=int(data.minute),
                    second=(int(data.second) + 1) % 60
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(next_time.hour, next_time.minute, next_time.second, mode))
            case CarouselTimePickerAction.DECREASE_SECOND_BY_5:
                prev_time = time(
                    hour=int(data.hour),
                    minute=int(data.minute),
                    second=(int(data.second) - 5) % 60
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(prev_time.hour, prev_time.minute, prev_time.second, mode))
            case CarouselTimePickerAction.DECREASE_SECOND_BY_1:
                prev_time = time(
                    hour=int(data.hour),
                    minute=int(data.minute),
                    second=(int(data.second) - 1) % 60
                )
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(prev_time.hour, prev_time.minute, prev_time.second, mode))
            case CarouselTimePickerAction.SELECT_HOUR:
                keyboard = await generate_selector(
                    data.hour, data.minute, data.second, "h", CarouselTimePickerAction, CarouselTimePickerCallback)
                await query.message.edit_reply_markup(reply_markup=keyboard)
            case CarouselTimePickerAction.SELECT_MINUTE:
                keyboard = await generate_selector(
                    data.hour, data.minute, data.second, "m", CarouselTimePickerAction, CarouselTimePickerCallback)
                await query.message.edit_reply_markup(reply_markup=keyboard)
            case CarouselTimePickerAction.SELECT_SECOND:
                keyboard = await generate_selector(
                    data.hour, data.minute, data.second, "s", CarouselTimePickerAction, CarouselTimePickerCallback)
                await query.message.edit_reply_markup(reply_markup=keyboard)
            case CarouselTimePickerAction.SELECTED_HOUR | CarouselTimePickerAction.SELECTED_MINUTE | CarouselTimePickerAction.SELECTED_SECOND:
                await query.message.edit_reply_markup(
                    reply_markup=await self.start_picker(data.hour, data.minute, data.second, mode))
            case CarouselTimePickerAction.IGNORE:
                pass
            case _:
                raise ValueError("Incorrect timepicker action: {}".format(data.act))
        return return_data
