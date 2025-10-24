from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.database import engine, Base
from app.routers import blog, user, comment, category
# from app.config import settings

# Create database tables
# Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="The Idiots Blog API",
    description="A simple blog API built with FastAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS (allow frontend to access API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
# app.include_router(user.router, prefix="/users", tags=["Users"])
# app.include_router(blog.router, prefix="/blogs", tags=["Blogs"])
# app.include_router(comment.router, prefix="/comments", tags=["Comments"])
# app.include_router(category.router, prefix="/categories", tags=["Categories"])

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to The Idiots Blog API!",
        "docs": "/docs",
        "version": "1.0.0"
    }

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "database": "connected"
    }

# Run with: uvicorn app.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )