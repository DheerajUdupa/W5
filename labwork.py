def display_dico(dico: dict):
    for key in dico:
        print(f"{str(key)} --> {str(dico[key])}")

display_dico({"un": 1, "deux": 2, "trois": 3})