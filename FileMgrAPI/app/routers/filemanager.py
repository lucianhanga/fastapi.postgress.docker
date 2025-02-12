from fastapi import APIRouter, HTTPException, UploadFile, File, Path
from pydantic import BaseModel
import os
import logging
import urllib.parse

router = APIRouter()

class FolderCreateRequest(BaseModel):
    foldername: str

@router.post("/create-file/{file_path:path}")
async def create_file(file_path: str = Path(...), file: UploadFile = File(...)):
    try:
        decoded_path = urllib.parse.unquote(file_path)
        file_location = os.path.join("/app/data", decoded_path)
        with open(file_location, "wb") as f:
            f.write(await file.read())
        return {"message": f"File '{decoded_path}' created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/create-folder/{folder_path:path}")
async def create_folder(folder_path: str = Path(...)):
    try:
        decoded_path = urllib.parse.unquote(folder_path)
        folder_location = os.path.join("/app/data", decoded_path)
        os.makedirs(folder_location, exist_ok=True)
        return {"message": f"Folder '{decoded_path}' created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/check-object/{object_path:path}")
async def check_object(object_path: str = Path(...)):
    decoded_path = urllib.parse.unquote(object_path)
    object_location = os.path.join("/app/data", decoded_path)
    if os.path.exists(object_location):
        if os.path.isfile(object_location):
            return {"exists": True, "type": "file"}
        elif os.path.isdir(object_location):
            return {"exists": True, "type": "folder"}
    else:
        return {"exists": False, "type": None}

@router.get("/list-contents/{folder_path:path}")
async def list_contents(folder_path: str = Path(...)):
    decoded_path = urllib.parse.unquote(folder_path)
    folder_location = os.path.join("/app/data", decoded_path)
    if os.path.exists(folder_location) and os.path.isdir(folder_location):
        contents = os.listdir(folder_location)
        return {"contents": contents}
    else:
        raise HTTPException(status_code=404, detail=f"Folder '{decoded_path}' does not exist.")

@router.delete("/remove-file/{file_path:path}")
async def remove_file(file_path: str = Path(...)):
    decoded_path = urllib.parse.unquote(file_path)
    file_location = os.path.join("/app/data", decoded_path)
    logging.debug(f"Attempting to remove file: {file_location}")
    if os.path.exists(file_location) and os.path.isfile(file_location):
        os.remove(file_location)
        return {"message": f"File '{decoded_path}' removed successfully."}
    else:
        raise HTTPException(status_code=404, detail=f"File '{decoded_path}' does not exist.")

@router.delete("/remove-folder/{folder_path:path}")
async def remove_folder(folder_path: str = Path(...)):
    decoded_path = urllib.parse.unquote(folder_path)
    folder_location = os.path.join("/app/data", decoded_path)
    logging.debug(f"Attempting to remove folder: {folder_location}")
    if os.path.exists(folder_location) and os.path.isdir(folder_location):
        os.rmdir(folder_location)
        return {"message": f"Folder '{decoded_path}' removed successfully."}
    else:
        raise HTTPException(status_code=404, detail=f"Folder '{decoded_path}' does not exist or is not empty.")

