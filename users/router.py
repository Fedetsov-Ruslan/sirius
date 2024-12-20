import aiohttp
import logging
import asyncio

from fastapi import APIRouter, HTTPException, Depends, Request

from config import (
    OMNIDESK_URL,
    HEADERS,)


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

async def get_session(request: Request):
    """Получение сессии для HTTP запросов к API"""
    
    return request.app.state.session

@router.post("/", summary="Получить список пользователей")
async def async_get_users(
    params : dict = {},
    session: aiohttp.ClientSession = Depends(get_session)):
    async with aiohttp.ClientSession() as session:
        params['page'] = 1
        params['limit'] = 100
        list_data = []
        for i in range(1, 500):
            async with session.get(f'{OMNIDESK_URL}/api/users.json', headers=HEADERS, params=params) as response:
                try:
                    data = await response.json()
                    list_data.append(data)
                    await asyncio.sleep(2)
                except:
                    logging.error(f'Ошибка: {response.status_code} {response.text}')
        return list_data
    
    
