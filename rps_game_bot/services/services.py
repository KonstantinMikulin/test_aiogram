import random

from rps_game_bot.lexicon.lexicon_ru import LEXICON_RU


def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            break
        return key


def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'peper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_win'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'
