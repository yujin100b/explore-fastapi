from fastapi import FastAPI

from api.routes.router import api_router
from core.config import (API_PREFIX, APP_NAME, APP_VERSION,
                                        DB_CONNECTION ,IS_DEBUG)
from core.event_handlers import (start_app_handler,
                                                  stop_app_handler)
from core.database import db


def get_app() -> FastAPI:
    fast_app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)

    db.init_app(app=fast_app, DB_URL=DB_CONNECTION)
    fast_app.include_router(api_router, prefix=API_PREFIX)

    return fast_app


app = get_app()
