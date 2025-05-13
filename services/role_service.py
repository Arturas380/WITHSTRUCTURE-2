from models.project import Role
from database import SessionLocal

def create_role(title):
    session = SessionLocal()
    role = Role(title=title)
    session.add(role)
    session.commit()
    session.close()

def list_roles():
    session = SessionLocal()
    roles = session.query(Role).all()
    session.close()
    return roles

def update_role(role_id, new_title):
    session = SessionLocal()
    role = session.query(Role).get(role_id)
    if not role:
        session.close()
        return None

    role.title = new_title
    session.commit()
    session.refresh(role)
    session.close()
    return role


def delete_role(role_id):
    session = SessionLocal()
    role = session.query(Role).get(role_id)
    if role:
        session.delete(role)
        session.commit()
    session.close()