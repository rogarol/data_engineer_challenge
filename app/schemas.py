# app/schemas.py
from pydantic import BaseModel,PositiveInt
from typing import Optional

class DepartmentBase(BaseModel):
    id: PositiveInt
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: PositiveInt

    class Config:
        orm_mode = True

class JobBase(BaseModel):
    id: PositiveInt
    name: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int

    class Config:
        orm_mode = True

class EmployeeBase(BaseModel):
    id: PositiveInt
    name: str
    department_id: PositiveInt
    job_id: PositiveInt

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: PositiveInt

    class Config:
        orm_mode = True
