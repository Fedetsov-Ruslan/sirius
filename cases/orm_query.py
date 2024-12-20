from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models import User, Case


async def set_cases(session: AsyncSession, case: dict):
    cases = Case(
        case_id=case['case_id'],
        case_number=case['case_number'],
        user_id=case['user_id'],
        subject=case['subject'],
        group_id=case['group_id'],
        status=case['status'],
        priority=case['priority'],
        channel=case['channel'],
        deleted=case['deleted'],
        spam=case['spam'],
        created_at=case['created_at'],
        updated_at=case['updated_at']
        )
    session.add(cases)
    await session.commit()
    


