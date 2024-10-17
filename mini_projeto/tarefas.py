from contatos import adicionar_contato, remover_contato, visualizar_contatos

# criar tarefa para adicionar na função adicionar tarefa
def criar_tarefa(contatos):
    tarefa = list()
    descricao = str(input('Qual tarefa deseja adicionar? ')).strip()
    horario = str(input('Qual o horário da tarefa? ')).strip().upper()
    add_contato = str(input('Deseja adicionar um contato à tarefa: [S/N] ')).strip().upper()[0]
    if add_contato == 'S':
        visualizar_contatos(contatos)
        contato = str(input('Qual contato deseja adicionar à tarefa? ')).strip().upper()
        tarefa.append(descricao)
        tarefa.append(horario)
        tarefa.append(contato)
    else:
        tarefa.append(descricao)
        tarefa.append(horario)
        tarefa.append('-')
    return tarefa
# adiciona tarefa criada na função criar_tarefa a lista de tarefas e retornar True se funcionar
def adicionar_tarefa(tarefas, contatos):
    tarefa = criar_tarefa(contatos)
    codigo = len(tarefas)
    tarefa.append(codigo)
    tarefas.append(tarefa)
    return True
# remover tarefa da lista de tarefas e retornar True se funcionar
def remover_tarefa(tarefas, codigo):
    for t in tarefas:
        if t[3] == codigo:
            tarefas.remove(t)
    return True
# visualizar a lista de tarefas
def visualizar_tarefas(tarefas):
    print('TAREFAS:')
    for t in tarefas:
        print(f'{t[3]} | {t[0]}, às {t[1]}, com {t[2]}')
