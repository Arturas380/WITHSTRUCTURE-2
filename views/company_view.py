from services.company_service import create_company, list_companies, delete_company

def prompt_new_company():
    name = input("Įveskite naujos įmonės pavadinimą: ")
    create_company(name)
    print("Įmonė sukurta.")

def prompt_list_companies():
    companies = list_companies()
    if not companies:
        print("Nėra įmonių.")
    for c in companies:
        print(f"{c.id}: {c.name}")

def prompt_delete_company():
    company_id = int(input("Įveskite įmonės ID kurią norite ištrinti: "))
    delete_company(company_id)
    print("Įmonė ištrinta.")