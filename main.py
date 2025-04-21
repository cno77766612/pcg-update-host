from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil, os, subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

REPO_PATH = "repo"
DATA_PATH = os.path.join(REPO_PATH, "data")

@app.post("/upload")
async def upload(file: UploadFile, filename: str = Form(...)):
    os.makedirs(DATA_PATH, exist_ok=True)
    save_path = os.path.join(DATA_PATH, filename)

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        subprocess.run(["git", "add", f"data/{filename}"], cwd=REPO_PATH, check=True)
        subprocess.run(["git", "commit", "-m", f"Add {filename}"], cwd=REPO_PATH, check=True)
        subprocess.run(["git", "push"], cwd=REPO_PATH, check=True)
        return {"message": "已成功上傳並推送至 GitHub"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
