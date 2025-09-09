from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os
from pathlib import Path

app = FastAPI(title="Data Parser API", description="REST API to serve documents from data folder")

DATA_DIR = Path("data")

@app.get("/")
def read_root():
    return {"message": "Data Parser API is running"}

@app.get("/data/{filename}")
def get_file(filename: str):
    # Security: prevent path traversal attacks
    if ".." in filename or "/" in filename or "\\" in filename:
        raise HTTPException(status_code=400, detail="Invalid filename")
    
    file_path = DATA_DIR / filename
    
    # Check if file exists
    if not file_path.exists() or not file_path.is_file():
        raise HTTPException(status_code=404, detail="File not found")
    
    # Check if file is within data directory (additional security)
    try:
        file_path.resolve().relative_to(DATA_DIR.resolve())
    except ValueError:
        raise HTTPException(status_code=400, detail="Access denied")
    
    return FileResponse(path=file_path, filename=filename)

@app.get("/data/")
def list_files():
    if not DATA_DIR.exists():
        return {"files": []}
    
    files = [f.name for f in DATA_DIR.iterdir() if f.is_file()]
    return {"files": files}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)