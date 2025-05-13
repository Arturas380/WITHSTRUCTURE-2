from models.department import Company
from database import SessionLocal

def create_company(name):
    session = SessionLocal()
    company = Company(name=name)
    session.add(company)
    session.commit()
    session.close()

def list_companies():
    session = SessionLocal()
    companies = session.query(Company).all()
    session.close()
    return companies

def update_company(company_id, new_name):
    session = SessionLocal()
    company = session.query(Company).get(company_id)
    if not company:
        session.close()
        return None

    company.name = new_name
    session.commit()
    session.refresh(company)
    session.close()
    return company


def delete_company(company_id):
    session = SessionLocal()
    company = session.query(Company).get(company_id)
    if company:
        session.delete(company)
        session.commit()
    session.close()