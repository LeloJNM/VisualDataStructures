import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from ls import SequentialList
from lse import LinkedList
from lde import DoublyLinkedList


# Define a função display_sequential_list
def display_sequential_list():
    sl = SequentialList(10)  # Cria uma lista sequencial com limite de 10 elementos

    janela = ThemedTk(theme="ubuntu")  # Cria uma janela com o tema "ubuntu"
    janela.title("Lista Sequencial")  # Define o título da janela
    janela.geometry("800x400")  # Define o tamanho da janela

    tela = ttk.Frame(janela)  # Cria um frame na janela
    tela.pack()  # Adiciona o frame à janela

    label_valor = ttk.Label(janela, text="Valor:")  # Cria um rótulo para o valor
    label_valor.pack(side="left")  # Adiciona o rótulo à janela

    entrada_valor = ttk.Entry(janela)  # Cria uma caixa de entrada para o valor
    entrada_valor.pack(side="left")  # Adiciona a caixa de entrada à janela

    label_pos = ttk.Label(janela, text="Posição:")  # Cria um rótulo para a posição
    label_pos.pack(side="left")  # Adiciona o rótulo à janela

    entrada_pos = ttk.Entry(janela)  # Cria uma caixa de entrada para a posição
    entrada_pos.pack(side="left")  # Adiciona a caixa de entrada à janela

    label_mensageiro = ttk.Label(janela)  # Cria um rótulo para exibir mensagens
    label_mensageiro.pack()  # Adiciona o rótulo à janela

    label_contador = ttk.Label(janela)  # Cria um rótulo para exibir o número de elementos
    label_contador.pack()  # Adiciona o rótulo à janela

    # Função para inserir um valor na lista
    def insert_value():
        # Obtém o valor da entrada
        value = entrada_valor.get()
        # Verifica se a entrada está vazia
        if value == "":
            # Exibe uma mensagem de erro se a entrada estiver vazia
            label_mensageiro.config(text="Erro! A entrada está vazia!")
        # Verifica se a lista ainda não atingiu seu limite
        elif len(sl.list) < sl.limit:
            # Insere o valor na lista e exibe os elementos
            sl.insert(value)
            display_elements()
        else:
            # Exibe uma mensagem de erro se a lista atingiu seu limite
            label_mensageiro.config(text=f"Erro! A lista atingiu seu limite de {sl.limit} elementos!")

    # Cria um botão para inserir um valor e associa a função insert_value a ele
    botao_insert = ttk.Button(janela, text="Inserir", command=insert_value)
    botao_insert.pack()

    # Função para inserir um valor em uma posição específica na lista
    def insert_at_position():
        # Obtém o valor e a posição da entrada
        value = entrada_valor.get()
        position = entrada_pos.get()
        # Verifica se a entrada de valor está vazia
        if value == "":
            # Exibe uma mensagem de erro se a entrada de valor estiver vazia
            label_mensageiro.config(text="Erro! A entrada de valor está vazia!")

        elif (int(position) == 1 and len(sl.list) == 0) or (
                int(position) - 1 == len(sl.list) and 10 > len(sl.list) > 0):
            # Insere o valor na lista e exibe os elementos se a posição for válida
            label_mensageiro.config(text="Insira um valor válido")
            sl.insert(value)
            display_elements()

        elif position == "" or not position.isdigit() or int(position) < 1:
            # Exibe uma mensagem de erro se a posição não for válida
            label_mensageiro.config(text="Erro! Por favor, informe uma posição válida!")

        elif position.isdigit() and int(position) <= len(sl.list) < sl.limit:
            """ Insere o valor em uma posição específica na lista e
            exibe os elementos se a posição for válida e a lista ainda não atingiu seu limite """
            sl.insert_at_position(value, int(position) - 1)
            display_elements()
        else:
            # Exibe uma mensagem de erro se não for possível inserir na posição especificada
            label_mensageiro.config(text=f"Erro! Não é possível inserir na posição {position}.")

    # Cria um botão para inserir um valor em uma posição específica e associa a função insert_at_position a ele
    botao_insert_position = ttk.Button(janela, text="Inserir por Posição", command=insert_at_position)
    botao_insert_position.pack()

    # Função para remover um valor da lista
    def remove_value():
        # Obtém o valor da entrada
        value = entrada_valor.get()
        # Verifica se a lista não está vazia
        if len(sl.list) > 0:
            # Remove o valor da lista e exibe os elementos
            sl.remove(value)
            display_elements()
        else:
            # Exibe uma mensagem de erro se a lista estiver vazia
            label_mensageiro.config(text="Erro! A lista está vazia!")

    # Cria um botão para remover um valor e associa a função remove_value a ele
    botao_remove = ttk.Button(janela, text="Remover por valor", command=remove_value)
    botao_remove.pack()

    # Função para remover um valor de uma posição específica na lista
    def remove_by_position():
        # Obtém a posição da entrada
        position = entrada_pos.get()
        # Verifica se a posição é válida
        if position == "" or not position.isdigit() or int(position) == 0:
            # Exibe uma mensagem de erro se a posição não for válida
            label_mensageiro.config(text="Erro! Por favor, informe uma posição válida!")
        elif position.isdigit() and int(position) <= len(sl.list):
            # Remove o valor da posição especificada na lista e exibe os elementos
            sl.remove_by_index(int(position) - 1)
            display_elements()
        else:
            # Exibe uma mensagem de erro se não houver elemento na posição especificada
            label_mensageiro.config(text=f"Erro! Não existe elemento na posição {position}.")

    # Cria um botão para remover um valor de uma posição específica e associa a função remove_by_position a ele
    botao_remove_position = ttk.Button(janela, text="Remover por Posição", command=remove_by_position)
    botao_remove_position.pack()

    # Função para buscar um valor na lista
    def search_value():
        # Obtém o valor da entrada
        value = entrada_valor.get()
        # Busca o valor na lista
        position = sl.search(value)
        if position != -1:
            # Exibe a posição do valor se ele for encontrado
            label_mensageiro.config(text=f"{position + 1}ª posição: {value}.")
        else:
            # Exibe uma mensagem se o valor não for encontrado
            label_mensageiro.config(text=f"Valor {value} não encontrado!")

    # Cria um botão para buscar um valor e associa a função search_value a ele
    botao_search = ttk.Button(janela, text="Buscar", command=search_value)
    botao_search.pack()

    # Função para buscar um valor em uma posição específica na lista
    def search_by_position():
        # Obtém a posição da entrada
        position = entrada_pos.get()
        if position == "" or not position.isdigit() or int(position) == 0:
            # Exibe uma mensagem de erro se a posição não for válida
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif position.isdigit():
            position = int(position) - 1
        if position < len(sl.list):
            # Exibe o valor na posição especificada se ela existir na lista
            label_mensageiro.config(text=f"{position + 1}ª posição: {sl.list[position]}.")
        else:
            # Exibe uma mensagem se a posição não for encontrada na lista
            label_mensageiro.config(text=f"Posição {position + 1} não encontrada!")

    # Cria um botão para buscar um valor em uma posição específica e associa a função search_by_position a ele
    botao_search_position = ttk.Button(janela, text="Buscar por Posição", command=search_by_position)
    botao_search_position.pack()

    # Função para exibir os elementos da lista
    def display_elements():
        # Remove todos os widgets da tela
        for widget in tela.winfo_children():
            widget.destroy()

        # Percorre todos os elementos da lista e exibe cada um deles em um quadrado na tela
        for i in range(len(sl.list)):
            square = tk.Canvas(tela, width=60, height=60)
            square.create_rectangle(10, 10, 60, 60, fill="dark orange")
            square.create_text(30, 30, text=str(sl.list[i]), fill="white")
            square.pack(side="left")

            if i != len(sl.list) - 1:  # Adiciona a vírgula apenas se não for o último elemento.
                comma_label = ttk.Label(tela, text="")
                comma_label.pack(side="left")

        # Atualiza o rótulo do contador com o número de elementos
        label_contador.config(text=f"Número de elementos: {len(sl.list)}/10.")

    janela.mainloop()


def display_linked_list():
    # Cria uma nova lista encadeada
    ll = LinkedList()

    # Configura a janela da interface gráfica
    janela = ThemedTk(theme="ubuntu")
    janela.title("Lista Simplesmente Encadeada")
    janela.geometry("800x300")

    # Cria um frame na janela
    tela = ttk.Frame(janela)
    tela.pack()

    # Cria um rótulo e uma caixa de entrada para o valor
    label_valor = ttk.Label(janela, text="Valor:")
    label_valor.pack(side="left")

    entrada_valor = ttk.Entry(janela)
    entrada_valor.pack(side="left")

    # Adiciona um rótulo e uma caixa de entrada para a posição
    label_pos = ttk.Label(janela, text="Posição:")
    label_pos.pack(side="left")

    entrada_pos = ttk.Entry(janela)
    entrada_pos.pack(side="left")

    # Cria um rótulo para exibir mensagens para o usuário
    label_mensageiro = ttk.Label(janela)
    label_mensageiro.pack()

    # Função para inserir um valor na lista encadeada
    def insert_value():
        value = entrada_valor.get()
        if value == "" or not value.isdigit():
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            ll.insert(int(value))
            display_nodes()

    # Cria um botão para inserir um valor na lista encadeada
    botao_insert = ttk.Button(janela, text="Inserir", command=insert_value)
    botao_insert.pack()

    # Função para inserir um valor em uma posição específica na lista encadeada
    def insert_at_position():
        value = entrada_valor.get()
        position = entrada_pos.get()
        if value == "" or not value.isdigit() or position == "" or not position.isdigit() or int(position) == 0:
            label_mensageiro.config(text="Erro! Por favor, informe um valor e uma posição válidos!")
        elif value.isdigit() and position.isdigit():
            ll.insert_at_position(int(value), int(position) - 1)  # Subtrai 1 da posição
            display_nodes()

    # Cria um botão para inserir um valor em uma posição específica na lista encadeada
    botao_insert_position = ttk.Button(janela, text="Inserir por Posição", command=insert_at_position)
    botao_insert_position.pack()

    def remove_value():
        value = entrada_valor.get()
        if value == "" or not value.isdigit():
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            ll.remove(int(value))
            display_nodes()

    botao_remove = ttk.Button(janela, text="Remover", command=remove_value)
    botao_remove.pack()

    def remove_at_position():
        position = entrada_pos.get()
        if position == "" or not position.isdigit() or int(position) == 0:
            label_mensageiro.config(text="Erro! Por favor, informe uma posição válida!")
        elif position.isdigit():
            ll.remove_at_position(int(position) - 1)  # Subtrai 1 da posição
            display_nodes()

    botao_remove_position = ttk.Button(janela, text="Remover por Posição", command=remove_at_position)
    botao_remove_position.pack()

    def search_value():
        position = None
        value = entrada_valor.get()
        if value == "" or not value.isdigit():
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            position = ll.search(int(value))
        if position != -1:
            label_mensageiro.config(text=f"Valor {value} encontrado na posição {position + 1}.")
        else:
            label_mensageiro.config(text=f"Valor {value} não encontrado!")

    botao_search = ttk.Button(janela, text="Buscar", command=search_value)
    botao_search.pack()

    def search_by_position():
        current = None
        current_position = None
        position = entrada_pos.get()
        if position == "" or not position.isdigit() or int(position) == 0:
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif position.isdigit():
            position = int(position) - 1
            current = ll.head
            current_position = 0
        while current:
            if current_position == position:
                label_mensageiro.config(text=f"{position + 1}ª posição: {current.value}.")
                return
            current_position += 1
            current = current.next
        label_mensageiro.config(text=f"Posição {position + 1} não encontrada!")

    botao_search_position = ttk.Button(janela, text="Buscar por Posição", command=search_by_position)
    botao_search_position.pack()

    def display_nodes():

        for widget in tela.winfo_children():
            widget.destroy()

        # Cria um quadrado para "HEAD"
        head_square = tk.Canvas(tela, width=60, height=60)
        head_square.create_rectangle(10, 10, 60, 60, fill="light blue")
        head_square.create_text(30, 30, text="HEAD", fill="white")
        head_square.pack(side="left")

        # Adiciona uma seta após "HEAD"
        head_arrow = ttk.Label(tela, text="➡", font=("Segoe UI Symbol", 30))
        head_arrow.pack(side="left", padx=(0, 0))

        current = ll.head
        while current:
            square = tk.Canvas(tela, width=60, height=60)
            square.create_rectangle(10, 10, 60, 60, fill="blue")
            square.create_text(30, 30, text=str(current.value), fill="white")
            square.pack(side="left")

            if current.next is not None:  # Adiciona a seta apenas se houver um próximo nó.
                arrow_label = ttk.Label(tela, text="➡", font=("Segoe UI Symbol", 30))
                arrow_label.pack(side="left", padx=(0, 0))

            current = current.next

    janela.mainloop()


def display_doubly_linked_list():
    dll = DoublyLinkedList()

    janela = ThemedTk(theme="ubuntu")
    janela.title("Lista duplamente encadeada")
    janela.geometry("800x400")

    tela = ttk.Frame(janela)
    tela.pack()

    label_value = ttk.Label(janela, text="Valor:")
    label_value.pack(side="left")

    entry_value = ttk.Entry(janela)
    entry_value.pack(side="left")

    # Adiciona um rótulo e uma caixa de entrada para a posição
    label_position = ttk.Label(janela, text="Posição:")
    label_position.pack(side="left")

    entry_position = ttk.Entry(janela)
    entry_position.pack(side="left")

    label_mensageiro = ttk.Label(janela)
    label_mensageiro.pack()

    def insert_value():
        value = entry_value.get()
        if value == "" or not value.isdigit():
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            dll.insert(int(value))
            display_nodes()

    botao_insert = ttk.Button(janela, text="Inserir", command=insert_value)
    botao_insert.pack()

    def insert_at_position():
        value = entry_value.get()
        position = entry_position.get()
        if not value.isdigit() or not position.isdigit() or int(position) < 1:
            label_mensageiro.config(text="Erro! Por favor, informe um valor e uma posição válidos!")
        else:
            dll.insert_at(int(position) - 1, int(value))
            display_nodes()

    botao_insert_position = ttk.Button(janela, text="Inserir por Posição", command=insert_at_position)
    botao_insert_position.pack()

    # Função para remover um valor da lista duplamente encadeada
    def remove_value():
        value = entry_value.get()
        if value == "" or not value.isdigit():
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            dll.remove(int(value))  # Remove o valor da lista
            display_nodes()  # Atualiza a exibição dos nós

    # Cria um botão para remover um valor da lista duplamente encadeada
    botao_remove = ttk.Button(janela, text="Remover", command=remove_value)
    botao_remove.pack()

    # Função para remover um valor de uma posição específica na lista duplamente encadeada
    def remove_at_position():
        position = entry_position.get()
        if not position.isdigit() or int(position) < 1:
            label_mensageiro.config(text="Erro! Por favor, informe uma posição válida!")
        else:
            dll.remove_at(int(position) - 1)  # Remove o valor na posição especificada (subtrai 1 da posição)
            display_nodes()  # Atualiza a exibição dos nós

    # Cria um botão para remover um valor de uma posição específica na lista duplamente encadeada
    botao_remove_position = ttk.Button(janela, text="Remover por Posição", command=remove_at_position)
    botao_remove_position.pack()

    # Função para buscar um valor na lista duplamente encadeada
    def search_value():
        position = None
        value = entry_value.get()
        if value == "" or not value.isdigit():
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            position = dll.search(int(value))  # Busca o valor na lista
        if position != -1:
            label_mensageiro.config(text=f"Valor {value} encontrado na posição {position + 1}.")  # Valor encontrado
        else:
            label_mensageiro.config(text=f"Valor {value} não encontrado!")  # Valor não encontrado

    # Cria um botão para buscar um valor na lista duplamente encadeada
    botao_search = ttk.Button(janela, text="Buscar", command=search_value)
    botao_search.pack()

    # Função para buscar um valor por posição na lista duplamente encadeada
    def search_by_position():
        current = None
        current_position = None
        position = entry_position.get()
        if position == "" or not position.isdigit() or int(position) == 0:
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif position.isdigit():
            position = int(position) - 1  # Subtrai 1 da posição
            current = dll.head  # Começa a busca a partir do início da lista
            current_position = 0
        while current:
            if current_position == position:
                label_mensageiro.config(text=f"{position + 1}ª posição: {current.value}.")  # Valor encontrado
                return
            current_position += 1
            current = current.next  # Move para o próximo nó na lista
        label_mensageiro.config(text=f"Posição {position + 1} não encontrada!")  # Posição não encontrada

    # Cria um botão para buscar um valor por posição na lista duplamente encadeada
    botao_search_position = ttk.Button(janela, text="Buscar por Posição", command=search_by_position)
    botao_search_position.pack()

    # Função para exibir os nós da lista duplamente encadeada
    def display_nodes():
        # Remove todos os widgets existentes na tela
        for widget in tela.winfo_children():
            widget.destroy()

        # Cria um quadrado para "HEAD"
        head_square = tk.Canvas(tela, width=60, height=60)
        head_square.create_rectangle(10, 10, 60, 60, fill="blue")
        head_square.create_text(30, 30, text="HEAD", fill="white")
        head_square.pack(side="left", padx=(0, 0))

        # Adiciona uma seta após "HEAD"
        head_arrow = ttk.Label(tela, text="➡", font=("Segoe UI Symbol", 30))
        head_arrow.pack(side="left", padx=(0, 0))

        # Percorre a lista duplamente encadeada e exibe cada nó
        current = dll.head
        while current:
            square = tk.Canvas(tela, width=60, height=60)
            square.create_rectangle(10, 10, 60, 60, fill="green")
            square.create_text(30, 30, text=str(current.value), fill="white")
            square.pack(side="left", padx=(0, 0))

            # Adiciona a seta para o próximo nó se ele existir
            if current.next is not None:
                arrow_frame = ttk.Frame(tela)
                arrow_label_right = ttk.Label(arrow_frame, text="→", font=("Segoe UI Symbol", 30))
                arrow_label_right.pack(side="top", padx=(0, 0), pady=(0, 0))
                arrow_label_left = ttk.Label(arrow_frame, text="←", font=("Segoe UI Symbol", 30))
                arrow_label_left.pack(side="top", padx=(0, 0), pady=(0, 0))
                arrow_frame.pack(side="left", padx=(0, 0))

            # Move para o próximo nó na lista
            current = current.next

        # Adiciona uma seta antes de "TAIL"
        tail_arrow = ttk.Label(tela, text="⬅", font=("Segoe UI Symbol", 30))
        tail_arrow.pack(side="left", padx=(0, 0))

        # Cria um quadrado para "TAIL"
        tail_square = tk.Canvas(tela, width=60, height=60)
        tail_square.create_rectangle(10, 10, 60, 60, fill="blue")
        tail_square.create_text(30, 30, text="TAIL", fill="white")
        tail_square.pack(side="left", padx=(0, 0))

        # Inicia o loop principal da janela
        janela.mainloop()


def main():
    # Cria uma nova janela com o tema "ubuntu"
    janela = ThemedTk(theme="ubuntu")
    janela.title("Simulador de Listas")  # Define o título da janela
    janela.geometry("730x300")  # Define o tamanho da janela

    # Cria um rótulo de boas-vindas na janela
    label = ttk.Label(janela, text='\nBem-vindo ao Simulador de Listas!', font=("Arial", 28), width=30,
                      padding={"sticky": "nswe"}, foreground="dark orange")
    label.pack()

    # Cria um botão para exibir a lista sequencial
    botaoLS = ttk.Button(janela, text="Lista Sequencial", command=display_sequential_list, width=40,
                         padding={"sticky": "nswe"})
    botaoLS.pack()

    # Cria um botão para exibir a lista simplesmente encadeada
    botaoLSE = ttk.Button(janela, text="Lista Simplesmente Encadeada", command=display_linked_list, width=40,
                          padding={"sticky": "nswe"})
    botaoLSE.pack()

    # Cria um botão para exibir a lista duplamente encadeada
    botaoLDE = ttk.Button(janela, text="Lista Duplamente Encadeada", command=display_doubly_linked_list, width=40,
                          padding={"sticky": "nswe"})
    botaoLDE.pack()

    # Inicia o loop principal da janela
    janela.mainloop()


# Verifica se este arquivo é o arquivo principal sendo executado
if __name__ == "__main__":
    main()  # Se for, executa a função main
