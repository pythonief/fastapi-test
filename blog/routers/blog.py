from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session

from blog import schemas
from blog.database import get_db
from blog.repository import blog

router = APIRouter(
    tags=['Blogs'],
    prefix='/blogs',
)


@router.get('', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return blog.delete(db, id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(db, request, id)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db)):
    return blog.show(db, id)
