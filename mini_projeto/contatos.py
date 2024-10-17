# adicionar um novo contato à lista de contatos e retornar True se funcionar
def adicionar_contato(contatos, nome):
    contatos.append(nome)
    return True
# remover um contato da lista de contatos e retornar True se funcionar
def remover_contato(contatos, nome):
    for c in contatos:
        if c == nome:
            contatos.remove(c)
    return True
# visualizar a lista com todos os contatos
def visualizar_contatos(contatos):
    print('CONTATOS:')
    for c in contatos:
        print(c)
