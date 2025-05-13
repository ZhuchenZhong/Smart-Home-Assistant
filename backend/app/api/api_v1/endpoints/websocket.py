from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List

router = APIRouter()

# 保存所有活跃的WebSocket连接
active_connections: List[WebSocket] = []

@router.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for connection in active_connections:
                await connection.send_text(f"Message: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)