from validate_docbr import CPF


def name_is_invalid(name):
    return not name.isalpha()


def cpf_is_invalid(cpf):
    validator = CPF()
    return not validator.validate(cpf)


def rg_is_invalid(rg):
    return len(rg) != 9
