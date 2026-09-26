from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time


app = FastAPI(
    title="React DevOps Demo API",
    description="Backend API for React DevOps practice and also learn git & github",
    version="1.0.0"
)


# ------------------------------------------------
# CORS Middleware
# ------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------------------------------------
# Custom Logging Middleware
# ------------------------------------------------

@app.middleware("http")
async def log_requests(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    print(
        f"{request.method} "
        f"{request.url.path} "
        f"-> {response.status_code} "
        f"({process_time:.4f}s)"
    )

    return response


# ------------------------------------------------
# Home API
# ------------------------------------------------

@app.get("/")
async def root():

    return {
        "message": "FastAPI backend is running!",
        "status": "success"
    }


# ------------------------------------------------
# Test API
# ------------------------------------------------

@app.get("/api/test")
async def test_api():

    return {
        "message": "Hello from FastAPI 🚀",
        "status": "success"
    }


# ------------------------------------------------
# DevOps Information API
# ------------------------------------------------

@app.get("/api/devops")
async def devops_info():

    return {
        "topics": [
            "React",
            "Git",
            "GitHub",
            "Deployment",
            "Docker",
            "CI/CD"
        ]
    }