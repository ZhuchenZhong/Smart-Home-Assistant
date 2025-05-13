import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# 修改导入语句 - 将相对导入改为绝对导入
from backend.app.core.config import settings
from backend.app.api.api_v1.api import api_router
from backend.app.core.events import startup_event_handler, shutdown_event_handler

# 创建FastAPI应用实例
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载静态文件
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# 注册API路由
app.include_router(api_router, prefix=settings.API_V1_STR)

# 注册事件处理
app.add_event_handler("startup", startup_event_handler(app))
app.add_event_handler("shutdown", shutdown_event_handler(app))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)