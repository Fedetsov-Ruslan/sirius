import aiohttp
import logging

from fastapi import APIRouter, HTTPException, Request, Depends

from config import (
    OMNIDESK_URL,
    HEADERS,)


router = APIRouter(
    prefix="/cases",
    tags=["cases"],
)

async def get_session(request: Request):
    """Получение сессии для HTTP запросов к API"""
    
    return request.app.state.session 


async def async_get_cases(
    params: dict = {},
    session: aiohttp.ClientSession = Depends(get_session)
    ):
    async with session.get(f'{OMNIDESK_URL}/api/cases.json', headers=HEADERS, params=params) as response:
        try:
            data = await response.json()
            return data
        except:
            logging.error(f'Ошибка: {response.status_code} {response.text}')
            raise HTTPException(status_code=response.status, detail="Error fetching data")


@router.post("/", summary="Получить список дел")
async def get_cases(
    params: dict = {},
    session: aiohttp.ClientSession = Depends(get_session)
    ):
    try:
        logging.info("Получение списка дел")
        return await async_get_cases(params, session)
    except:
        logging.info("Ошибка при получении списка дел")
        return 1


@router.post("/{case_id}", summary="Получить информацию о деле")
async def get_case(case_id: int, session: aiohttp.ClientSession = Depends(get_session)):
    logging.info("Получение информации о деле")
    return await async_get_cases({'id': case_id}, session)



    
        

