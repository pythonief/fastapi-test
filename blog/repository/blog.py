from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

from blog import models


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request, db: Session):
    new_blog = models.Blog(**request.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(db: Session, id):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id of {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'done'}

def update(db: Session, request, id):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id of {id} not found')
    db.query(models.Blog).filter(models.Blog.id == id).update(request.dict())
    db.commit()
    return 'updated'

def show(db: Session, id):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    return blog