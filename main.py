from fastapi import FastAPI

app = FastAPI(title="FastAPI App", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/api/info")
async def info():
    return {"app": "FastAPI", "version": "1.0.0"}
