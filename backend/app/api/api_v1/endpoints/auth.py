from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

# 修改这些导入
from backend.app.core.security import create_access_token
from backend.app.core.config import settings

router = APIRouter()

@router.post("/login")
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """OAuth2 兼容的token登录，获取access token"""
    # 此处应添加用户验证逻辑
    return {"access_token": "临时token", "token_type": "bearer"}