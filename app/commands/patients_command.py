from sqlalchemy import insert
from app.models.patients import PatientDB
from app.schemas.patients_schema import PatientCreate

class PatientCommandHandler:
  def __init__(self, db_session):
    self.db_session = db_session

    async def create_patient(self, patient: PatientCreate):
      qInsert = insert(PatientDB).values(patient.model_dump())
      await self.db_session.execute(qInsert)
      await self.db_session.commit()
      return{"message": "Paciente agregado exitosamente."}