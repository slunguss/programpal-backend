from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()
fake_db = []

class ProgramCreate(BaseModel):
    name: str
    days_per_week: int

class Program(BaseModel):
    id:str
    name:str
    days_per_week: int

@app.get("/")
def root():
    return {"message": "ProgramPal API is running"}


@app.post("/programs")
def create_program(program: ProgramCreate):
    new_program = Program(
        id=str(uuid.uuid4()),
        name=program.name,
        days_per_week=program.days_per_week)
    fake_db.append(new_program)
    return new_program