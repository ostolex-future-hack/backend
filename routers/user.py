from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from database import get_db
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from services import user as UserService
from dto import user as userDTO
from speech_to_text import speech_to_text

router = APIRouter()

@router.post('/', tags=["user"])
async def create(data: userDTO.User = None, db: Session = Depends(get_db)):
    return UserService.create_user(data, db)


@router.post('/user_lang', tags=["user"])
async def update_user_lang(id: int = None, data: userDTO.User = None, db: Session = Depends(get_db)):
    return UserService.update_user_language_lvl(id, data, db)


@router.get('/{id}', tags=["user"])
async def get(id: int = None, db: Session = Depends(get_db)):
    return UserService.get_user(id, db)


@router.put('/{id}', tags=["user"])
async def update(id: int = None, data: userDTO.User = None, db: Session = Depends(get_db)):
    return UserService.update(data, db, id)


@router.delete('/{id}', tags=["user"])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return UserService.remove(db, id)


@router.post('/goal', tags=["goal"])
async def create_goal(data: userDTO.Goal = None, db: Session = Depends(get_db)):
    return UserService.create_goal_s(data, db)


@router.get('/goal/{name}', tags=["goal"])
async def get_goal(id: int, db: Session = Depends(get_db)):
    return UserService.get_goal_s(db, id)


@router.post('/utg', tags=['user_to_goal'])
async def create_utg(data: userDTO.users_to_goals = None, db: Session = Depends(get_db)):
    return UserService.add_goals_to_user(data, db)


@router.get('/utg/{user_id}', tags=["user_to_goal"])
async def get_utg(user_id: int, db: Session = Depends(get_db)):
    return UserService.get_users_to_goal_s(user_id, db)


@router.post('/language', tags=["language_lvl"])
async def create_language(data: userDTO.Language = None, db: Session = Depends(get_db)):
    return UserService.create_language_lvl(data, db)


@router.get('/language/get', tags=["language_lvl"])
async def get_language(language: float, db: Session = Depends(get_db)):
    return UserService.get_language_lvl(db, language)


@router.post("/file/upload", tags=["file"])
async def upload_file(id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    # contents = await file.read()
    # with open("uploaded.mp3", "wb") as f:
    #     f.write(contents)
    speech_to_text("uploaded.mp3", id, db)
    # return {"filename": file.filename}



@router.get("/file/get", tags=["file"])
async def get_file(filename: str):
    file = filename
    return FileResponse(file, media_type="audio/mpeg")
