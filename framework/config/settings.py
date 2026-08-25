import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    API_BASE_URL = os.getenv(
        "API_BASE_URL",
        "https://jsonplaceholder.typicode.com"
    )

    WEB_BASE_URL = os.getenv(
        "WEB_BASE_URL",
        "https://www.saucedemo.com"
    )

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "local"
    )

    HEADLESS = os.getenv(
        "HEADLESS",
        "true"
    ).lower() == "true"