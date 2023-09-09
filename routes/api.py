from fastapi import APIRouter

from app.api.controllers.auth.login import router as login_api

router = APIRouter()


def includeApiRoutes():
    ''' Include to router all api rest routes with version prefix '''
    router.include_router(login_api)


includeApiRoutes()