from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Lesson Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Lesson Generator API работает!"}

@app.get("/api/health")
async def health():
    return {"status": "healthy"}

@app.post("/api/upload")
async def upload():
    return {"message": "Загрузка файла - заглушка"}

@app.get("/api/status/{job_id}")
async def status(job_id: str):
    return {"job_id": job_id, "status": "pending", "message": "Заглушка"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)