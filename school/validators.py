def name_is_invalid(name):
    return not name.isalpha()


def cpf_is_invalid(cpf):
    return len(cpf) != 11


def rg_is_invalid(rg):
    return len(rg) != 9
