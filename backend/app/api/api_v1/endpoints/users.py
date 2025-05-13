from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from backend.app.database.session import get_session
from backend.app.models.user import User, UserCreate, UserResponse, UserUpdate

router = APIRouter()

@router.get("/")
async def read_users():
    """获取所有用户列表"""
    return {"users": []}