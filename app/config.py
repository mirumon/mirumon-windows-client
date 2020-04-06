import logging
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings

from app.logging import InterceptHandler

# BASE_DIR = Path(__file__).resolve().parent.parent
# ENV_PATH = BASE_DIR.joinpath(".env")
# load_dotenv(ENV_PATH)


class Settings(BaseSettings):
    server_websocket_url: str = "wss://api.mirumon.dev/clients/ws"  # ws://localhost:8000/clients/ws
    reconnect_delay: int = 10
    debug: bool = True

    class Config:  # noqa: WPS431
        case_sensitive = True


settings = Settings()

LOGGING_LEVEL = logging.DEBUG if settings.debug else logging.INFO

logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
