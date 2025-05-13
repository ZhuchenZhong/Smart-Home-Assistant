import asyncio
import logging
from typing import Dict, Any, Callable

import paho.mqtt.client as mqtt
from paho.mqtt.client import MQTTMessage

from backend.app.core.config import settings

logger = logging.getLogger(__name__)

class AsyncMQTTClient:
    def __init__(self):
        self.client = mqtt.Client(client_id=settings.MQTT_CLIENT_ID)
        if settings.MQTT_USERNAME and settings.MQTT_PASSWORD:
            self.client.username_pw_set(settings.MQTT_USERNAME, settings.MQTT_PASSWORD)
            
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_disconnect = self._on_disconnect
        
        self.topics: Dict[str, Callable[[MQTTMessage], None]] = {}
        self.is_connected = False
        
    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info("已连接到MQTT服务器")
            self.is_connected = True
            # 订阅所有已注册的主题
            for topic in self.topics.keys():
                client.subscribe(topic)
        else:
            logger.error(f"连接MQTT服务器失败，代码: {rc}")
            
    def _on_message(self, client, userdata, msg):
        logger.debug(f"从主题 {msg.topic} 收到消息: {msg.payload.decode()}")
        if msg.topic in self.topics:
            callback = self.topics[msg.topic]
            callback(msg)
            
    def _on_disconnect(self, client, userdata, rc):
        logger.info("与MQTT服务器断开连接")
        self.is_connected = False
        
    async def connect(self):
        """连接MQTT代理"""
        logger.info(f"正在连接MQTT服务器 {settings.MQTT_BROKER_HOST}:{settings.MQTT_BROKER_PORT}")
        self.client.connect_async(settings.MQTT_BROKER_HOST, settings.MQTT_BROKER_PORT)
        self.client.loop_start()
        
    async def disconnect(self):
        """断开MQTT代理连接"""
        if self.is_connected:
            self.client.disconnect()
            self.client.loop_stop()
            logger.info("已断开MQTT连接")
            
    def subscribe(self, topic: str, callback: Callable[[MQTTMessage], None]):
        """订阅MQTT主题"""
        self.topics[topic] = callback
        if self.is_connected:
            self.client.subscribe(topic)
            logger.info(f"已订阅主题: {topic}")
            
    def publish(self, topic: str, payload: Any, qos: int = 0, retain: bool = False):
        """发布MQTT消息"""
        if isinstance(payload, dict):
            import json
            payload = json.dumps(payload)
        elif not isinstance(payload, str):
            payload = str(payload)
            
        self.client.publish(topic, payload, qos, retain)
        logger.debug(f"已发布消息到主题 {topic}: {payload}")

# 创建全局MQTT客户端实例
mqtt_client = AsyncMQTTClient()