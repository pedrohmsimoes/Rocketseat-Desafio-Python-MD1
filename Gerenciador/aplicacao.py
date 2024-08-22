def criar_contato(contatos):
    
    nome = input("Adicione o nome do contato: ")
    email = input("Digite o email: ")
    try:
        telefone = int(input("Digite o número de telefone: "))
    except ValueError as erro:
        print(f"Erro: {erro}\nDigite apenas números")
        return
    contato = {"nome": nome, "email": email, "telefone": telefone, "favorito": False}
    contatos.append(contato)
    print(f"Contato com o nome {nome} foi criado com sucesso!")
    return

def lista_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos):
        status_favorito = "★" if contato["favorito"] else ""
        print(f"{indice + 1}. {contato['nome']} - {contato['telefone']} - {contato['email']} {status_favorito}")
    return

def editar_contato(contatos):
    lista_contatos(contatos)
    nome = input("\nDigite o nome do contato para poder editar: ")
    contato_encontrado = False

    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            contato_encontrado = True
            print("\nO que você deseja editar?")
            print("1. Email")
            print("2. Telefone")
            print("3. Editar Email e Telefone")
            escolha = input("Digite 1 para editar o Email, 2 para editar o Telefone ou 3 para editar ambos: ")

            if escolha == "1":
                novo_email = input("Digite o novo Email: ")
                contato["email"] = novo_email
                print(f"Email do contato {nome} foi atualizado para {novo_email}!")

            elif escolha == "2":
                novo_telefone = input("Digite o novo Telefone: ")
                contato["telefone"] = novo_telefone
                print(f"Telefone do contato {nome} foi atualizado para {novo_telefone}!")

            elif escolha == "3":
                novo_email = input("Digite o novo Email: ")
                contato["email"] = novo_email
                novo_telefone = input("Digite o novo Telefone: ")
                contato["telefone"] = novo_telefone
                print(f"O contato {nome} foi atualizado com o email {novo_email} e telefone {novo_telefone}.")

            else:
                print("Opção inválida! Tente novamente.")
            break

    if not contato_encontrado:
        print(f"Contato {nome} não encontrado.")

def contato_favorito(contatos):
    lista_contatos(contatos)
    nome = input("Qual é o nome do contato que deseja marcar como favorito ou desmarcar: ")
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            contato["favorito"] = not contato["favorito"]
            estado = "marcado" if contato["favorito"] else "desmarcado"
            print(f"O contato {nome} foi {estado} como favorito.")
            return
    print(f"Contato {nome} não encontrado.")
    return

def lista_contatos_favoritos(contatos):
    print("Lista de contatos Favoritos:")
    favoritos = [contato for contato in contatos if contato["favorito"]]
    if favoritos:
        for contato in favoritos:
            print(f'{contato["nome"]} - {contato["telefone"]} - {contato["email"]}')
    else:
        print("Nenhum contato favorito encontrado.")      
    return


def deletar_contato(contatos):
    # Antes de poder deletar podera visualizar a lista de contatos
    lista_contatos(contatos)
    nome = input("Digite o nome do contato que deseja deletar: ")
    contato_encontrado = False

    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            contatos.remove(contato)
            contato_encontrado = True
            print(f"Contato '{nome}' foi deletado com sucesso!")
            break
    
    if not contato_encontrado:
        print(f"Contato '{nome}' não encontrado.")
    return

contatos = []

while True:
    print("\nGerenciador de contatos")
    print("1. Fazer um cadastro de um contato")
    print("2. Visualizar a lista de contatos cadastrados")
    print("3. Editar um contato")
    print("4. Marcar ou desmarcar um contato como favorito")
    print("5. Visualizar uma lista de contatos favoritos")
    print("6. Apagar um contato")
    print("7. Finalizar Programa")

    escolha = input("Digite um número de 1 a 7: ")

    if escolha == "1":
        criar_contato(contatos)
    elif escolha == "2":
        lista_contatos(contatos)
    elif escolha == "3":
        # Você pode adicionar a função de editar contato aqui.

        editar_contato(contatos)
        pass
    elif escolha == "4":
        # Você pode adicionar a função de marcar/desmarcar favorito aqui.
        contato_favorito(contatos)
        pass
    elif escolha == "5":
        # Você pode adicionar a função de visualizar contatos favoritos aqui.
        lista_contatos_favoritos(contatos)
        pass
    elif escolha == "6":
        deletar_contato(contatos)
    elif escolha == "7":
        break
    else:
        print("Opção inválida! Tente novamente.")

print("Programa finalizado")