from sqlalchemy import Column, Integer, String, Date, Float, Table, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

employee_roles = Table(
    'employee_roles',
    Base.metadata,
    Column('employee_id', Integer, ForeignKey('employees.id')),
    Column('role_id', Integer, ForeignKey('roles.id'))
)

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    birth_date = Column(Date)
    salary = Column(Float)
    start_date = Column(DateTime, default=datetime.utcnow)
    company_id = Column(Integer, ForeignKey('companies.id'))

    company = relationship("Company", back_populates="employees")
    roles = relationship("Role", secondary=employee_roles, back_populates="employees")