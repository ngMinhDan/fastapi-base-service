"""
Router package
"""

from fastapi import APIRouter
from .users import router as user_router
from .admin import router as admin_router

router = APIRouter(prefix="/api/v1")
router.include_router(user_router, tags=["users"], prefix="/users")
router.include_router(admin_router, tags=["admin"], prefix="/admin")