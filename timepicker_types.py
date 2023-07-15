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


class CarouselTimePickerAction(IntEnum):
    INCREASE_HOUR_BY_5 = 0
    INCREASE_HOUR_BY_1 = 1
    DECREASE_HOUR_BY_1 = 2
    DECREASE_HOUR_BY_5 = 3
    INCREASE_MINUTE_BY_5 = 4
    INCREASE_MINUTE_BY_1 = 5
    DECREASE_MINUTE_BY_1 = 6
    DECREASE_MINUTE_BY_5 = 7
    INCREASE_SECOND_BY_5 = 8
    INCREASE_SECOND_BY_1 = 9
    DECREASE_SECOND_BY_1 = 10
    DECREASE_SECOND_BY_5 = 11
    SELECT_HOUR = 12
    SELECT_MINUTE = 13
    SELECT_SECOND = 14
    SELECTED_HOUR = 15
    SELECTED_MINUTE = 16
    SELECTED_SECOND = 17
    CANCEL = 18
    CONFIRM = 19
    IGNORE = 20


class CarouselTimePickerCallback(CallbackData, prefix="carousel_timepicker"):
    act: CarouselTimePickerAction
    hour: int
    minute: int
    second: int
