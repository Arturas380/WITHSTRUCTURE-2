from services.employee_service import create_employee, update_employee, delete_employee
from database import SessionLocal
from models.employee import Employee

def prompt_new_employee():
    data = {
        "first_name": input("Vardas: "),
        "last_name": input("Pavardė: "),
        "birth_date": input("Gimimo data (YYYY-MM-DD): "),
        "salary": float(input("Atlyginimas: ")),
        "company_name": input("Įmonės pavadinimas: "),
        "role_titles": input("Pareigos (atskirti kableliais): ").split(",")
    }
    data["role_titles"] = [title.strip() for title in data["role_titles"]]
    employee = create_employee(data)
    print(f"Darbuotojas sukurtas: {employee.id}")

def prompt_edit_employee():
    session = SessionLocal()
    emp_id = int(input("Įveskite darbuotojo ID kurį norite redaguoti: "))
    employee = session.query(Employee).get(emp_id)
    if not employee:
        print("Darbuotojas nerastas.")
        return

    print("Palikite tuščią lauką, jei nenorite keisti.")
    first_name = input(f"Naujas vardas ({employee.first_name}): ") or employee.first_name
    last_name = input(f"Nauja pavardė ({employee.last_name}): ") or employee.last_name
    birth_date = input(f"Nauja gimimo data ({employee.birth_date}): ") or str(employee.birth_date)
    salary = input(f"Naujas atlyginimas ({employee.salary}): ")
    salary = float(salary) if salary else employee.salary
    company_name = input(f"Naujas įmonės pavadinimas ({employee.company.name}): ") or employee.company.name
    role_titles = input(f"Naujos pareigos (dabartinės: {', '.join([r.title for r in employee.roles])}): ")
    role_titles = [r.strip() for r in role_titles.split(",")] if role_titles else [r.title for r in employee.roles]

    updated_data = {
        "id": emp_id,
        "first_name": first_name,
        "last_name": last_name,
        "birth_date": birth_date,
        "salary": salary,
        "company_name": company_name,
        "role_titles": role_titles,
    }

    update_employee(updated_data)
    print("Darbuotojas atnaujintas.")

def prompt_delete_employee():
    emp_id = int(input("Įveskite darbuotojo ID kurį norite ištrinti: "))
    delete_employee(emp_id)
    print("Darbuotojas ištrintas.")

from database import SessionLocal
from models.employee import Employee

def list_employees():
    session = SessionLocal()
    employees = session.query(Employee).all()
    if not employees:
        print("Darbuotojų nėra.")
    for emp in employees:
        roles = ', '.join([role.title for role in emp.roles])
        print(f"{emp.id}: {emp.first_name} {emp.last_name}, {emp.birth_date}, Atlyginimas: {emp.salary}, Įmonė: {emp.company.name}, Pareigos: {roles}")
    session.close()
