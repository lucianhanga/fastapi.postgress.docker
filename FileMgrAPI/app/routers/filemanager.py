from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
import os

router = APIRouter()

class FolderCreateRequest(BaseModel):
    foldername: str

@router.post("/create-file")
async def create_file(file: UploadFile = File(...)):
    try:
        file_location = f"/app/data/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())
        return {"message": f"File '{file.filename}' created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/create-folder")
async def create_folder(request: FolderCreateRequest):
    try:
        folder_location = f"/app/data/{request.foldername}"
        os.makedirs(folder_location, exist_ok=True)
        return {"message": f"Folder '{request.foldername}' created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/check-object/{object_name}")
async def check_object(object_name: str):
    object_location = f"/app/data/{object_name}"
    if os.path.exists(object_location):
        if os.path.isfile(object_location):
            return {"exists": True, "type": "file"}
        elif os.path.isdir(object_location):
            return {"exists": True, "type": "folder"}
    else:
        return {"exists": False, "type": None}

@router.get("/list-contents/{folder_name}")
async def list_contents(folder_name: str):
    folder_location = f"/app/data/{folder_name}"
    if os.path.exists(folder_location) and os.path.isdir(folder_location):
        contents = os.listdir(folder_location)
        return {"contents": contents}
    else:
        raise HTTPException(status_code=404, detail=f"Folder '{folder_name}' does not exist.")

