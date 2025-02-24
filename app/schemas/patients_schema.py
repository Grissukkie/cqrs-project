from datetime import date
from pydantic import BaseModel, ConfigDict

class PatientCreate(BaseModel):
  fullname: str
  birthday: date
  address: str
  phone: str
  email: str

class PatientRead(BaseModel):
  patients_id: int
  fullname: str
  birthday: date
  address: str
  phone: str
  email: str

model_config = ConfigDict(from_attributes=True)