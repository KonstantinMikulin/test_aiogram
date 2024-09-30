from typing import Any

from aiogram.types import User

from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.text import Format

from bot.db.requests import get_total_score_for_user
from .states import StatsSG


async def get_total_score(
    dialog_manager: DialogManager,
    event_from_user: User,
    **kwargs
    ) -> dict[str, Any]:
    session = dialog_manager.middleware_data.get('session')
    user_id = event_from_user.id
    name = event_from_user.first_name
    total_score = await get_total_score_for_user(session, user_id) #type:ignore
    
    return {'name': name, 'total_score': total_score}


stats_dialog = Dialog(
    Window(
        Format('Hello, {name}'),
        Format('Your total score: {total_score}'),
        getter=get_total_score,
        state=StatsSG.get_stats
    )
)
