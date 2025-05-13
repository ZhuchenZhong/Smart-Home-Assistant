from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_devices():
    """获取所有设备列表"""
    return {"devices": []}