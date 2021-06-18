from fastapi import Response, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.logger import logger
import traceback
from app.database import Session


def setup(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "https://kuchida1981.github.io",
        ],
    )

    @app.middleware("http")
    async def db_session_middleware(request: Request, call_next):
        request.state.db_session = Session()
        try:
            response = await call_next(request)
            request.state.db_session.commit()
        except Exception:
            logger.error(traceback.format_exc())
            request.state.db_session.rollback()
            response = Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            request.state.db_session.close()
        return response
