# gerenciador de tarefas pessoais com tarefas, contatos e horários das tarefas
# opções disponíveis no menu

from contatos import adicionar_contato, remover_contato, visualizar_contatos
from tarefas import adicionar_tarefa, remover_tarefa, visualizar_tarefas
from time import sleep
contatos = list()
tarefas = list()

while True:
    print('-'*15 + ' GERENCIADOR DE TAREFAS PESSOAIS ' + '-'*15)
    print('[0] ver lista de tarefas')
    print('[1] ver lista de contatos')
    print('[2] adicionar tarefa')
    print('[3] remover tarefa')
    print('[4] adicionar contato')
    print('[5] remover contato')
    print('[6] sair')
    opcao = int(input('Digite o número correspondete à opção que deseja realizar: '))

    if opcao == 0:
        visualizar_tarefas(tarefas)
        sleep(1)
    elif opcao == 1:
        visualizar_contatos(contatos)
        sleep(1)
    elif opcao == 2:
        print('ADICIONAR TAREFA:')
        if adicionar_tarefa(tarefas, contatos):
            print('Tarefa adicionada com sucesso!')
        else:
            print('Ocorreu um erro.')
        sleep(1)
    elif opcao == 3:
        print('REMOVER TAREFA:')
        visualizar_tarefas(tarefas)
        codigo = int(input('Informe o código da tarefa a ser removida: '))
        if remover_tarefa(tarefas, codigo):
            print('Tarefa removida com sucesso!')
        else:
            print('Ocorreu um erro.')
        sleep(1)
    elif opcao == 4:
        print('ADICIONAR CONTATO:')
        nome = str(input('Informe o nome do contato: ')).strip().upper()
        if adicionar_contato(contatos, nome):
            print('Contato adicionado com sucesso!')
        else:
            print('Ocorreu um erro.')
        sleep(1)
    elif opcao == 5:
        print('REMOVER CONTATO:')
        visualizar_contatos(contatos)
        nome = str(input('Informe o nome do contato: ')).strip().upper()
        if remover_contato(contatos, nome):
            print('Contato removido com sucesso!')
        else:
            print('Ocorreu um erro.')
        sleep(1)
    elif opcao == 6:
        break
    else:
        print('Opção indisponível! Tente novamente.')
        sleep(1)
