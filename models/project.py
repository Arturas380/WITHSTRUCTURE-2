from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.employee import employee_roles

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True)

    employees = relationship("Employee", secondary=employee_roles, back_populates="roles")