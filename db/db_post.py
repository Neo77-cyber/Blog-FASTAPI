from routers.schemas import Postbase
from sqlalchemy.orm.session import Session
from db.models import DbPost
import datetime
from fastapi import HTTPException
from fastapi import status


def create_post(db: Session, request: Postbase):
    new_post = DbPost(
    image_url = request.image_url,
    title = request.title,
    details = request.details,
    creator = request.creator,
    timestamp = datetime.datetime.now())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_posts(db:Session):
    return db.query(DbPost).all()

def get_post(id: int, db:Session):
    post= db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=400, detail=(f'Blog post with {id} not found'))
    return post
    
def update_post(db:Session, id: int,  request: Postbase):
    post = db.query(DbPost).filter(DbPost.id == id)
    if not post:
        raise HTTPException(status_code=400, detail=('Blog Post not found'))
    post.update({DbPost.image_url: request.image_url,
                        DbPost.title: request.title,
                        DbPost.details: request.details,
                        DbPost.creator: request.creator
   } 
    )
    db.commit()
    return 'Post updated'
    

def delete_post(id: int, db: Session):
  post = db.query(DbPost).filter(DbPost.id == id).first()
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog post with {id} not found')
  db.delete(post)
  db.commit()
  return 'Post Deleted'


    
    