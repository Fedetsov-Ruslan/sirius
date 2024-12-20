import requests
import json
import re
import logging
import time
import aiohttp
import asyncio

from fastapi import APIRouter, HTTPException

from config import (
    OMNIDESK_URL,
    HEADERS,)


router = APIRouter(
    prefix="/cases",
    tags=["cases"],
)


def get_macros(headers):
    response = requests.get(f'{OMNIDESK_URL}/api/macros.json', headers=headers)
    try:
        data = response.json()
        title = []
        result = []
        for macro_id, macro_data in data.get('common', {}).get('0', {}).get('data', {}).items():
            title.append(f" {macro_data.get('title', '')}")
            x = macro_data.get('actions', '')[0]['action_destination']['1']
            result.append(re.sub(r'\n+','',re.sub(r'<[^>]*>', '',x)).strip())
        return title, result
    except:
        logging.error(f'Ошибка: {response.status_code} {response.text}')
    
    
def get_cases(headers : str, params : dict = {}):
    response = requests.get(f'{OMNIDESK_URL}/api/cases.json', headers=headers, params=params)
    try:
        data = response.json()
        return data
    except:
        logging.error(f'Ошибка: {response.status_code} {response.text}')


async def async_get_cases(headers : str, params : dict = {}):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{OMNIDESK_URL}/api/cases.json', headers=headers, params=params) as response:
            try:
                data = await response.json()
                return data
            except:
                logging.error(f'Ошибка: {response.status_code} {response.text}')

async def async_get_users(headers : str, params : dict = {}):
    async with aiohttp.ClientSession() as session:
        params['page'] = 1
        params['limit'] = 100
        for i in range(1, 500):
            async with session.get(f'{OMNIDESK_URL}/api/users.json', headers=headers, params=params) as response:
                try:
                    data = await response.json()
                    return data
                except:
                    logging.error(f'Ошибка: {response.status_code} {response.text}')
                    await asyncio.sleep(2)   

def get_users(headers):
    for i in range(1, 500):
        response = requests.get(f'{OMNIDESK_URL}/api/users.json', headers=headers, params={'page': i, 'limit': 100})

        write_in_file('users.txt', response.json()) 
        time.sleep(2) 
        

def write_macros_in_file(title, result):
    for i in range(len(title)):
        with open('macros.txt', 'a', encoding='utf-8') as f:
            f.write(f"Заголовок: {title[i]} - Текст: {result[i]}")
            f.write('\n')

      
def write_in_file(file_name, cases):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(str(json.dumps(cases, indent=4, ensure_ascii=False)))

s = get_cases(HEADERS)

write_in_file('cases_one_user.txt', s)




            
