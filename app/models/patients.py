from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PatientDB(Base):
  __tablename__ = "patients"
  patients_id = Column(Integer, primary_key=True, index=True)
  fullname = Column(String(50))
  birthday = Column(Date)
  address = Column(String(100))
  phone = Column(String(13))
  email = Column(String(50))