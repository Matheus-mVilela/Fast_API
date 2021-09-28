from fastapi import FastAPI, Depends ,HTTPException
from sqlalchemy.orm import Session
from typing import List

import database, schemas, models

# Create DB.
database.Base.metadata.create_all(bind = database.engine)


app = FastAPI()

# Dependency
def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.Users).all()
    return users


@app.post("/create/user", response_model=schemas.User)
def create_user(user:schemas.User, db: Session = Depends(get_db)):
    new_user=models.Users(
        name=user.name,
        description=user.description,
        age=user.age,
        fone=user.fone
    )
    db.add(new_user)
    db.commit()

    return new_user


@app.get("/user/detail/{user_id}")
def detail_user(user_id, db: Session = Depends(get_db)):
    user=db.query(models.Users).filter(models.Users.id == user_id).first()
    if not user: 
        raise HTTPException(status_code=404, detail="User not found")

    return user


@app.put("/user/update/{user_id}")
def update_user(user_id, user:schemas.User , db: Session = Depends(get_db)):
    user_update=db.query(models.Users).filter(models.Users.id == user_id).first()
    
    if not user_update: 
        raise HTTPException(status_code=404, detail="User not found")
    
    user_update.name=user.name
    user_update.description=user.description
    user_update.age=user.age
    user_update.fone=user.fone
    
    db.commit()

    return user_update


@app.delete("/user/delete/{user_id}")
def delete_user(user_id, db: Session = Depends(get_db)):
    
    user=db.query(models.Users).filter(models.Users.id == user_id).first()
    if not user: 
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {'message': 'User is deleted!'}