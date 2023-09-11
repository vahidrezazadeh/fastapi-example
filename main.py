from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.middlewares.loggerMiddleware import LoggerMiddleware

from routes.api import router

from settings import settings

def initApplication() -> FastAPI:

    ## Create FastApi App
    fastApiApp = FastAPI()

    fullApiPrefix = str("/%s/%s" %(settings.apiPrefix , settings.apiVersion))
    ## Mapping api routes
    fastApiApp.include_router(router,prefix=fullApiPrefix)

    ## Custom Middlewares
    fastApiApp.add_middleware(LoggerMiddleware)

    ## Allow cors
    fastApiApp.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return fastApiApp


app = initApplication()