from services.role_service import create_role, list_roles, delete_role

def prompt_new_role():
    title = input("Įveskite naują pareigų pavadinimą: ")
    create_role(title)
    print("Pareigos sukurtos.")

def prompt_list_roles():
    roles = list_roles()
    if not roles:
        print("Nėra pareigų.")
    for r in roles:
        print(f"{r.id}: {r.title}")

def prompt_delete_role():
    role_id = int(input("Įveskite pareigų ID kurias norite ištrinti: "))
    delete_role(role_id)
    print("Pareigos ištrintos.")