from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Add this line
from . import models
from .database import engine
from .router import blog, user, authentication
import os  # Add this line for Render port configuration

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (replace "*" with your frontend URL in production)
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

# Add this block for Render deployment
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))