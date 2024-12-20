import aiohttp

from fastapi import FastAPI

from cases.router import router as cases_router
from users.router import router as users_router


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    app.state.session = aiohttp.ClientSession()


@app.on_event("shutdown")
async def shutdown_event():
    await app.state.session.close()


app.include_router(cases_router)
app.include_router(users_router)