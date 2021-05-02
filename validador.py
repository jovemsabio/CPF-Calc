def validaCPF(CPF):
    """
    Valida o cpf informado

    Função para validar o número de CPF informado

    :param CPF: Número do CPF como string
    :return: True, quando o CPF for válido e False, caso contrário
    """

    cpf = list(CPF.replace('.', '').replace('-', ''))
    print(cpf)

    try:
        if len(cpf) != 11:
            raise Exception('CPF Inválido: deve conter 11 dígitos')
        elif not CPF.isalnum():
            raise Exception('CPF Inválido: deve conter apenas números')

        # dv -> dígito verificador
        dv = str()
        for j in range(1, 3):
            L = 0
            for i in range(0, 9):
                L += ((10 - i) * int(cpf[i]))
                Resto = L % 11
            if Resto < 2:
                dv += '0'
            else:
                dv += str(11 - Resto)
            cpf.pop(0)

        if not CPF.endswith(dv):
            raise Exception('CPF Inválido')

    except Exception as e:
        return False
    else:
        return True

