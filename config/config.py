from os import getenv, path

from dotenv import load_dotenv

dotenv_path = path.join(path.dirname(__file__), ".env")
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Settings:
    DB_HOST: str = getenv("DB_HOST")
    DB_PORT: str = getenv("DB_PORT")
    DB_USER: str = getenv("DB_USER")
    DB_PASS: str = getenv("DB_PASS")
    DB_NAME: str = getenv("DB_NAME")

    @property
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
