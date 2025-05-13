from sqlmodel import SQLModel, create_engine, Session

from backend.app.core.config import settings

# 创建数据库引擎
engine = create_engine(
    settings.SQLITE_DATABASE_URI, 
    echo=True,
    connect_args={"check_same_thread": False}  # SQLite特有设置
)

def create_db_and_tables():
    """创建数据库和表"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """获取数据库会话"""
    with Session(engine) as session:
        yield session