from aiogram.fsm.state import State, StatesGroup


class DeleteUserSG(StatesGroup):
    delete_user_state = State()
