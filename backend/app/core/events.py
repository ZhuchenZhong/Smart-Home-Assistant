import logging
from typing import Callable
from fastapi import FastAPI

from backend.app.database.session import create_db_and_tables
from backend.app.mqtt.client import mqtt_client

logger = logging.getLogger(__name__)

def startup_event_handler(app: FastAPI) -> Callable:
    async def startup() -> None:
        logger.info("正在执行应用启动事件")
        # 创建数据库表
        create_db_and_tables()
        # 连接MQTT代理
        await mqtt_client.connect()
    
    return startup

def shutdown_event_handler(app: FastAPI) -> Callable:
    async def shutdown() -> None:
        logger.info("正在执行应用关闭事件")
        # 断开MQTT连接
        await mqtt_client.disconnect()
    
    return shutdown