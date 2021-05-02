from validador import validaCPF

if __name__ == '__main__':
    while True:
        cpf = input('Informe o CPF (apenas números), \'q\' para sair: ')
        if cpf == 'q':
            break
        if validaCPF(cpf):
            print('CPF válido')
        else:
            print("CPF Invalido")
