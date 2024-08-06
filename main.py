'''Crie um programa em que o usuário possa cadastrar uma lista de tarefas a fazer no dia. 
   Após terminar, envie o link do repositório no GitHub.'''

tarefasDiarias =['Acordar','Levantar da cama','Tomar Banho','Fazer barba','Ler','Tomar café',
'Ir trabalhar','Realizar um ótimo trabalho', 'Pausa para o almoço','Descanso do almoço'
,'Voltar ao trabalho','Encerrar o expediente','Ir para aula ' ,'etc']

#print(f'Quantida de tarefas do dia são :'(len(tarefasDiarias)))

for i in range(len(tarefasDiarias)):
    print(f'{i+1}º Listas de tarefas : {tarefasDiarias[i]}')
