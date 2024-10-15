def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Editar tarefa")
        print("4. Remover tarefa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa()
            break
        elif opcao == '2':
            listar_tarefas()
            break
        elif opcao == '3':
            editar_tarefa()
            break
        elif opcao == '4':
            remover_tarefa()
            break
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def adicionar_tarefa():
    print("adicionar tarefa")

def listar_tarefas():
    print("listar tarefas")

def editar_tarefa():
    print("editar tarefa")

def remover_tarefa():
    print("remover tarefa")

if __name__ == "__main__":
    main()
