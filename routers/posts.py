from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from routers.schemas import PostBaseDsplay
from db.database import get_db
from db import db_post
from fastapi import UploadFile, File
import shutil
import random






router = APIRouter(
  prefix='/blog',
  tags=['blog']
)

@router.post('')
def create_post(request: PostBaseDsplay, db: Session = Depends(get_db)):
  return db_post.create_post(db,request)

@router.get('/all')
def get_posts(db:Session = Depends(get_db)):
  return db_post.get_all_posts(db)

@router.get('{id}')
def get_post(id: int, db:Session = Depends(get_db)):
  return db_post.get_post(id, db)

@router.put('/update{id}')
def update_post(id: int, request: PostBaseDsplay, db: Session = Depends(get_db)):
  return db_post.update_post(db,id,request)

@router.delete('/{id}')
def delete_post(id: int, db: Session = Depends(get_db)):
  return db_post.delete_post(id, db)


@router.post('/image')
def upload_image(image: UploadFile = File(...)):


  path = image.filename 

  with open(path, "w+b") as buffer:
    shutil.copyfileobj(image.file, buffer)

  return {'filename': path}

