from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    #We especify the relationship between the hired employee an the department
    employees = relationship("Employee", back_populates="department")

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    #We especify the relationship between the hired employee an the job
    employees = relationship("Employee", back_populates="job")

class Employee(Base):
    __tablename__ = "hired_employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    #We especify the relationship between the hired employee, department and job
    department = relationship("Department", back_populates="employees")
    job = relationship("Job", back_populates="employees")