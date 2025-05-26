from fastapi import FastAPI
from src.routes.auth import router as auth_router
from src.routes.post import router as post_router

app = FastAPI()

# Include routers for authentication and post operations
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(post_router, prefix="/posts", tags=["posts"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
