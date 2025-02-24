from sqlalchemy import select
from app.models.patients import PatientDB
from app.schemas.patients_schema import PatientRead

class PatientQueryHandler:
    def __init__(self, db_session):
        self.db_session = db_session

    async def get_patient(self, patients_id: int):
        result = await self.db_session.execute(
            select(PatientDB).where(PatientDB.patients_id == patients_id)
        )
        patient = result.scalars().first()
        return PatientRead.model_validate(patient, from_attributes=True) if patient else None 

    async def list_patients(self):
        result = await self.db_session.execute(select(PatientDB))
        return [PatientRead.model_validate(p, from_attributes=True) for p in result.scalars()]
