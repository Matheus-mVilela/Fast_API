from fastapi import FastAPI, HTTPException
from models import User
from uuid import uuid4 as uuid


app = FastAPI()

db = []


@app.get("/")
def get_db():
    return db


@app.post("/user", response_model=User)
async def create_user(user: User):
    user.id = str(uuid())
    db.append(user.dict())
    return user


@app.get("/user/detail/{user_id}")
async def detail_user(user_id):
    for user in db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.put("/user/update/{user_id}")
async def update_user(user_id, user_updated: User):
    for index, user in enumerate(db):
        if user["id"] == user_id:
            db[index]["name"] = user_updated.name
            db[index]["description"] = user_updated.description
            db[index]["age"] = user_updated.age
            db[index]["number"] = user_updated.number
            breakpoint()
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/delete/{user_id}")
async def delete_user(user_id):
    for index, user in enumerate(db):
        if user["id"] == user_id:
            db.pop(index)
            return {"messege": "User deleted successful."}
    raise HTTPException(status_code=404, detail="User not found")
