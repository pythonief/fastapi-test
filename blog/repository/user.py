from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from blog import hashing, models


def create(db: Session, request):
    request.password = hashing.Hash().bcrypt(request.password)
    new_user = models.User(**request.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_one(db: Session, id):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')
    return user
