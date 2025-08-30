pessoas = []
contador = 0

def cadastrar_pessoa():
    global contador
    print("\n--- Cadastro de Pessoa ---")
    nome = input("Nome: ")
    while nome.strip() == "":
        nome = input("Nome não pode ser vazio.")

    cpf = input("CPF (apenas números): ")
    while not cpf.isdigit() or len(cpf) != 11:
        cpf = input("CPF inválido. Deve conter 11 dígitos.")

    idade = int(input("Idade: "))
    while idade <= 0 or idade >= 121:
        idade = input("idade invalida diga sua idade real: ")

    email = input("E-mail: ")
    while not "." in email and not "@" in email:
        email = input("email invalido digite novamente: ")

    cep = input("CEP: ")
    while len(cep) != 8:
        cep = input("cep invalido escreva novamente: ")

    pessoa = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "email": email,
        "cep": cep
    }
    pessoas.append(pessoa)
    contador = contador + 1
    print("Pessoa cadastrada com sucesso!")
    return

def listar_pessoas():
    print("\n--- Lista de Pessoas ---")
    for i, pessoa in enumerate(pessoas):
        print(f"{i+1} , {pessoa}")

def editar_pessoa():
    listar_pessoas()
    global contador
    opção1 = int(input("diga quem quer editar com o numero da lista: "))
    while opção1 <1 or opção1 > contador:
        opção1 = int(input("pessoa invalida digite o numero novamente: "))
    opção1 = opção1 - 1
    opção2 = input("escreva com uma palavra oque quer editar: ")
    if opção2 == "nome":
        nome = input("escreva o nome que quer editar: ")
        while nome.strip() == "":
            nome = input("Nome não pode ser vazio.")
        pessoas[opção1]["nome"] = nome
        print("nome editado com sucesso")
        return
    elif opção2 == "cpf":
         cpf = input("escreva o cpf que quer editar: ")
         while not cpf.isdigit() or len(cpf) != 11:
            cpf = input("CPF inválido. Deve conter 11 dígitos.")
         pessoas[opção1]["cpf"] = cpf
         print("cpf editado com sucesso")
         return
    elif opção2 == "idade":
        idade = input("digite qual idade que quer editar: ")
        while idade <= 0 or idade >= 121:
            idade = input("idade invalida diga sua idade real: ")
        pessoas[opção1]["idade"] = idade
        print("idade editada com sucesso")
        return
    elif opção2 == "email" or opção2 == "e-mail":
        email = input("digite o email que quer editar: ")
        while not "." in email and not "@" in email:
            email = input("email invalido digite novamente: ")
        pessoas[opção1]["email"] = email
        print("email editado com sucesso")
        return
    elif opção2 == "cep":
        cep = input("digite on cep qu quer editar: ")
        while len(cep) != 8:
            cep = input("cep invalido escreva novamente: ")
        pessoas[opção1]["cep"] = cep
        print("cep editado com suicesso")
        return
    else:
        print("COMANDO INVALIDO")
        return

def excluir_pessoa():
    listar_pessoas()
    global contador
    opção1 = int(input("diga quem quer excluir com o numero da lista: "))
    while opção1 <1 or opção1 > contador:
        opção1 = int(input("pessoa invalida digite o numero novamente: "))
    opção1 = opção1 - 1
    pessoas.pop(opção1)
    print("pessoa excluida com sucesso")
    contador = contador - 1
    return


def menu():
    while True:
        global contador
        print("\n====== MENU PRINCIPAL ======")
        print("1. Cadastrar Pessoa")
        print("2. Listar Pessoas")
        print("3. Editar Pessoa")
        print("4. Excluir Pessoa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            listar_pessoas()
        elif opcao == '3':
            if contador == 0:
                print("comando não pode ser executado por não ter pessoas cadastradas")
            else:
                editar_pessoa()
        elif opcao == '4':
            if contador == 0:
                print("comando não pode ser executado por não ter pessoas cadastradas")
            else:
                excluir_pessoa()
        elif opcao == '5':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
