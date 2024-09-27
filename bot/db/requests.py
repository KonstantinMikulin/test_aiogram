from sqlalchemy.dialects.postgresql import insert as upsert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from bot.db.models import User, Score


async def upsert_user(
    session: AsyncSession,
    telegram_id: int,
    first_name: str,
    last_name: str | None = None
):
    """
    Add user or upgrade user info
    """
    stmt = upsert(User).values(
        {
            "telegram_id": telegram_id,
            "first_name": first_name,
            "last_name": last_name
        }
    )
    stmt = stmt.on_conflict_do_update(
        index_elements=["telegram_id"],
        set_=dict(
            first_name=first_name,
            last_name=last_name
        )
    )
    
    await session.execute(stmt)
    await session.commit()


async def add_score(
    session: AsyncSession,
    telegram_id: int,
    score: int
):
    """
    Add score (random int)
    """
    new_score = Score(
        user_id=telegram_id,
        score=score
    )
    session.add(new_score)
    await session.commit()


async def get_total_score_for_user(
    session: AsyncSession,
    telegram_id: int
) -> int:
    """
    Return total score for user
    """
    user = await session.get(
        User,
        {'telegram_id': telegram_id},
        options=[selectinload(User.scores)]
    )
    
    return sum(item.score for item in user.scores)
