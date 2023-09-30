import uvicorn
from fastapi import FastAPI

from .app import Application, settings_load


app = FastAPI(
    title='Smartisha',
    description='HR-bot',
    version='1.0.0',
)
settings = settings_load('./config.yaml')

application = Application(settings=settings, app=app)


@app.on_event('startup')
async def startup():
    await application.initialize()


@app.on_event('shutdown')
async def shutdown():
    await application.deinitialize()


if __name__ == '__main__':
    uvicorn.run(
        'src.__main__:app',
        host=settings['host'],
        port=settings['port'],
        reload=True,
    )
