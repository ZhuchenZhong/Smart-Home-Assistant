from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class UserBase(SQLModel):
    """用户基础信息"""
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    full_name: Optional[str] = None
    is_active: bool = True
    is_admin: bool = False

class User(UserBase, table=True):
    """用户数据模型"""
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class UserCreate(UserBase):
    """创建用户请求模型"""
    password: str

class UserUpdate(SQLModel):
    """更新用户请求模型"""
    username: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None

class UserResponse(UserBase):
    """用户响应模型"""
    id: int
    created_at: datetime