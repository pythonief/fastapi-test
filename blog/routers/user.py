from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from blog import schemas
from blog.database import get_db

from ..repository import user

router = APIRouter(
    tags=['Users'],
    prefix='/user',
)


@router.post('', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(db, request)


@router.get('/{id}', response_model=schemas.ShowUserBlogs)
def get_user(id, db: Session = Depends(get_db)):
    return user.get_one(db, id)
