import os
import signal
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.config import settings
from app.exception_handler.base import exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
    exception_handlers=exception_handlers,
)

if __name__ == "__main__":
    try:
        uvicorn.run(
            app="main:app",
            host=settings.HOST,
            port=settings.PORT,
            reload=settings.DEBUG,
        )
    except KeyboardInterrupt:
        pass
    finally:
        os.kill(os.getpid(), signal.SIGINT)
