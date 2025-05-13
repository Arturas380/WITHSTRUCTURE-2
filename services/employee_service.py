from models.employee import Employee
from models.department import Company
from models.project import Role
from database import SessionLocal

def get_or_create_company(session, company_name):
    company = session.query(Company).filter_by(name=company_name).first()
    if not company:
        company = Company(name=company_name)
        session.add(company)
        session.commit()
        session.refresh(company)
    return company

def get_or_create_roles(session, role_titles):
    roles = []
    for title in role_titles:
        role = session.query(Role).filter_by(title=title).first()
        if not role:
            role = Role(title=title)
            session.add(role)
            session.commit()
            session.refresh(role)
        roles.append(role)
    return roles

def create_employee(data):
    session = SessionLocal()
    company = get_or_create_company(session, data.pop("company_name"))
    role_titles = data.pop("role_titles")

    employee = Employee(**data)
    employee.company = company
    employee.roles = get_or_create_roles(session, role_titles)

    session.add(employee)
    session.commit()
    session.refresh(employee)
    session.close()
    return employee

def update_employee(data):
    session = SessionLocal()
    employee = session.query(Employee).get(data["id"])
    if not employee:
        print("Darbuotojas nerastas.")
        return

    employee.first_name = data["first_name"]
    employee.last_name = data["last_name"]
    employee.birth_date = data["birth_date"]
    employee.salary = data["salary"]
    employee.company = get_or_create_company(session, data["company_name"])
    employee.roles = get_or_create_roles(session, data["role_titles"])

    session.commit()
    session.close()

def delete_employee(emp_id):
    session = SessionLocal()
    employee = session.query(Employee).get(emp_id)
    if employee:
        session.delete(employee)
        session.commit()
    session.close()