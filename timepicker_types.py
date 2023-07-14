from aiogram.filters.callback_data import CallbackData
from enum import IntEnum


class FullTimePickerAction(IntEnum):
    INCREASE_HOUR = 0
    DECREASE_HOUR = 1
    INCREASE_MINUTE = 2
    DECREASE_MINUTE = 3
    INCREASE_SECOND = 4
    DECREASE_SECOND = 5
    SELECT_HOUR = 6
    SELECT_MINUTE = 7
    SELECT_SECOND = 8
    SELECTED_HOUR = 9
    SELECTED_MINUTE = 10
    SELECTED_SECOND = 11
    CANCEL = 12
    CONFIRM = 13


class FullTimePickerCallback(CallbackData, prefix='full_timepicker'):
    act: FullTimePickerAction
    hour: int
    minute: int
    second: int
