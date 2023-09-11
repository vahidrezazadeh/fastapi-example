from asgiref.sync import sync_to_async
from starlette.types import ASGIApp, Scope, Receive, Send
from starlette.requests import Request


class LoggerMiddleware:
    # Example Middleware For Log
    
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        print ('CALL LOGGER MIDDLEWARE')
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        await self.app(scope, receive, send)
        
        return

    async def execute_request(self, request: Request, send: Send) -> None:
        print ('execute_request LOGGER MIDDLEWARE')
        pass

    @staticmethod
    @sync_to_async
    def exception_middleware_handler(request: Request):
        print ('exception_middleware_handler LOGGER MIDDLEWARE')

    @staticmethod
    @sync_to_async
    def desensitization(args: dict):
        print ('desensitization LOGGER MIDDLEWARE')
