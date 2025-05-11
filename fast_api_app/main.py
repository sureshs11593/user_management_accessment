from fastapi import FastAPI, HTTPException
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_management.settings")
django.setup()

from users.models import UserProfile
from fast_api_app.schema import UserCreate, UserUpdate, UserOut
from django.shortcuts import get_object_or_404

app = FastAPI()

@app.get("/users/", response_model=list[UserOut])
def list_users():
    return list(UserProfile.objects.all())

@app.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: str):
    user = get_object_or_404(UserProfile, id=user_id)
    return user

@app.post("/users/", response_model=UserOut)
def create_user(user: UserCreate):
    obj = UserProfile.objects.create(**user.dict())
    return obj

@app.put("/users/{user_id}", response_model=UserOut)
def update_user(user_id: str, updated_user: UserUpdate):
    user = get_object_or_404(UserProfile, id=user_id)
    for field, value in updated_user.dict().items():
        setattr(user, field, value)
    user.save()
    return user

@app.delete("/users/{user_id}")
def soft_delete_user(user_id: str):
    user = get_object_or_404(UserProfile, id=user_id)
    user.is_active = False
    user.save()
    return {"message": "User soft deleted"}
