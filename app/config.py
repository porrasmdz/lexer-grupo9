from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    NOMBRE_ESTUDIANTE: str
    NOMBRE_AVANCE: str

settings = Settings(_env_file='prod.env', _env_file_encoding='utf-8')