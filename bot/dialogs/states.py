from aiogram.fsm.state import State, StatesGroup


class ScoreSG(StatesGroup):
    fill_score = State()
