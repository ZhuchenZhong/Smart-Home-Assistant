from fastapi import APIRouter

# 修改这个导入
from backend.app.api.api_v1.endpoints import devices, users, auth, websocket

api_router = APIRouter()

# 注册各模块路由
api_router.include_router(auth.router, prefix="/auth", tags=["认证"])
api_router.include_router(users.router, prefix="/users", tags=["用户"])
api_router.include_router(devices.router, prefix="/devices", tags=["设备"])
api_router.include_router(websocket.router, prefix="/ws", tags=["WebSocket"])