
from database import Base, engine
from views.employee_view import (
    prompt_new_employee,
    prompt_edit_employee,
    prompt_delete_employee,
    list_employees
)
from views.company_view import (
    prompt_new_company,
    prompt_list_companies,
    prompt_delete_company
)
from views.role_view import (
    prompt_new_role,
    prompt_list_roles,
    prompt_delete_role
)

def main():
    Base.metadata.create_all(bind=engine)

    while True:
        print("\n--- Darbuotojų valdymas ---")
        print("1. Pridėti naują darbuotoją")
        print("2. Peržiūrėti visus darbuotojus")
        print("3. Redaguoti darbuotoją")
        print("4. Ištrinti darbuotoją")
        print("5. Valdyti įmones")
        print("6. Valdyti pareigas")
        print("7. Išeiti")
        choice = input("Pasirinkite veiksmą: ")

        if choice == "1":
            prompt_new_employee()
        elif choice == "2":
            list_employees()
        elif choice == "3":
            prompt_edit_employee()
        elif choice == "4":
            prompt_delete_employee()
        elif choice == "5":
            print("1. Pridėti įmonę")
            print("2. Peržiūrėti įmones")
            print("3. Ištrinti įmonę")
            sub = input("Pasirinkite veiksmą: ")
            if sub == "1": prompt_new_company()
            elif sub == "2": prompt_list_companies()
            elif sub == "3": prompt_delete_company()
        elif choice == "6":
            print("1. Pridėti pareigas")
            print("2. Peržiūrėti pareigas")
            print("3. Ištrinti pareigas")
            sub = input("Pasirinkite veiksmą: ")
            if sub == "1": prompt_new_role()
            elif sub == "2": prompt_list_roles()
            elif sub == "3": prompt_delete_role()
        elif choice == "7":
            print("Programa baigta.")
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")
