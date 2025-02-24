from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.commands.patients_command import PatientCommandHandler
from app.db.database import get_db, init_db
from app.queries.patients_query import PatientQueryHandler
from app.schemas.patients_schema import PatientCreate, PatientRead

app = FastAPI()

@app.on_event("startup")
async def startup_event():
   await init_db()

@app.get("/")
async def root():
  return {"message": "Bienvenido dal sistema del Centro Médico"}

@app.post("/patients")
async def create_patient(
  patient: PatientCreate,
  db: AsyncSession = Depends(get_db)
 ):
    handler = PatientCommandHandler(db)
    return await handler.create_patient(patient)

@app.get("/patients/{patients_id}", response_model=PatientRead)
async def get_patient(
    patients_id: int,
    db: AsyncSession = Depends(get_db)
  ):
    handler = PatientQueryHandler(db)
    return await handler.get_patient(patients_id)

@app.get("/patients", response_model=list[PatientRead])
async def list_patients(db: AsyncSession = Depends(get_db)):
  handler = PatientQueryHandler(db)
  return await handler.list_patients()