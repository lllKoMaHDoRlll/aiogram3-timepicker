from aiogram.filters.callback_data import CallbackData
from enum import IntEnum


class FullTimePickerAction(IntEnum):
    INCREASE_HOUR = 0
    DECREASE_HOUR = 1
    INCREASE_MINUTE = 2
    DECREASE_MINUTE = 3
    SELECT_HOUR = 4
    SELECT_MINUTE = 5
    CANCEL = 6
    CONFIRM = 7
    SELECTED_HOUR = 8
    SELECTED_MINUTE = 9


class FullTimePickerCallback(CallbackData, prefix='full_timepicker'):
    act: FullTimePickerAction
    hour: int
    minute: int
