from aiogram.fsm.state import State, StatesGroup


class StatsSG(StatesGroup):
    get_stats = State()
