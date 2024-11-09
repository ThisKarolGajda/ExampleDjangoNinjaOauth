from backend.oauth import router as auth_router
from ninja import NinjaAPI
from users.views import router as users_router

api = NinjaAPI(
    title="Backend",
    description="Backend documentation",
    version="1.0.0",

)

api.add_router("users", users_router, tags=["Users"])
api.add_router("auth", auth_router, tags=["Auth"])