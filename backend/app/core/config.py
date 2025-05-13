from typing import List, Union
from pydantic_settings import BaseSettings
import secrets
from pydantic import AnyHttpUrl, validator

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "智能家居助手"
    PROJECT_DESCRIPTION: str = "一个现代化的智能家居控制和管理系统"
    VERSION: str = "0.1.0"
    
    # 安全设置
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1天
    
    # CORS设置
    CORS_ORIGINS: List[Union[str, AnyHttpUrl]] = ["http://localhost:3000", "http://localhost:8080"]
    
    # 数据库设置
    SQLITE_DATABASE_URI: str = "sqlite:///./smart_home.db"
    
    # MQTT设置
    MQTT_BROKER_HOST: str = "localhost"
    MQTT_BROKER_PORT: int = 1883
    MQTT_CLIENT_ID: str = "smart_home_backend"
    MQTT_USERNAME: str = ""
    MQTT_PASSWORD: str = ""
    
    @validator("CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()