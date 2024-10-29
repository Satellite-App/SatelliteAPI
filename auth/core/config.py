from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal, List, Union
from ipaddress import IPv4Address

class AppSettings(BaseSettings):
    APP_NAME: str = "Auth"
    APP_PORT: int = "80"
    MAX_WORKERS: int = 5


class LoggerSettings(BaseSettings):
    LOG_LEVEL: Literal['INFO', 'DEBUG', 'ERROR', 'CRITICAL', 'WARNING'] = "INFO"
    LOGSTASH_SERVER: Union[IPv4Address, str] = ""
    LOGSTASH_PORT: int = 0


class JWTSettings(BaseSettings):
    SECRET: str
    JWT_LIFETIME: int
    REFRESH_LIFETIME: int


class DatabaseSettings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    REPLICA_NAME: str
    DB_HOSTS: List[Union[IPv4Address, str]]
    DB_PORT: int

    @property
    def db_url(self):
        hosts = f':{self.DB_PORT},'.join(self.DB_HOSTS)
        return f'mongodb://{self.DB_USER}:{self.DB_PASSWORD}@{hosts}:{self.DB_PORT}/' +\
               f'{self.DB_NAME}?replicaSet={self.REPLICA_NAME}'


class IAMService(BaseSettings):
    IAM_HOST: str
    IAM_PORT: int


class Settings(AppSettings, LoggerSettings, DatabaseSettings, JWTSettings, IAMService):
    model_config = SettingsConfigDict(env_file='.env')
