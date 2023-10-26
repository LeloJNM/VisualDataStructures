import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from tkinter import Text
from ttkthemes import ThemedTk
from sl import SequentialList 
from ll import LinkedList
from dll import DoublyLinkedList
from Pilha import Stack
from Fila import Queue
from ABP import ArvoreBinariaPesquisa
from ABP import NoGrafico

# Define a função display_sequential_list
def display_sequential_list():
    sl = SequentialList(10)  # Cria uma lista sequencial com limite de 10 elementos

    janela = ThemedTk(theme="ubuntu")  # Cria uma janela com o tema "ubuntu"
    janela.title("Lista Sequencial")  # Define o título da janela
    janela.geometry("800x800")  # Define o tamanho da janela

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

    squares = [tk.Canvas(tela, width=60, height=60) for _ in range(10)]  # Cria uma lista de quadrados vazios
    for square in squares:
        square.create_rectangle(10, 10, 60, 60)  # Desenha um quadrado vazio em cada canvas
        square.pack(side="left")  # Adiciona cada quadrado à tela

        # Função para inserir um valor na lista
    
        # Função para inserir um valor na lista
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
    botao_insert = ttk.Button(janela, text="Inserir no Final", command=insert_value)
    botao_insert.pack()

    # Função para inserir um valor em uma posição específica na lista
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
                int(position) - 1 <= len(sl.list) and 10 > len(sl.list)):
            # Insere o valor na lista e exibe os elementos se a posição for válida
            sl.insert_at_position(value, int(position) - 1)
            display_elements()

        elif position == "" or not position.isdigit() or int(position) < 1:
            # Exibe uma mensagem de erro se a posição não for válida
            label_mensageiro.config(text="Erro! Por favor, informe uma posição válida!")

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
    botao_search = ttk.Button(janela, text="Buscar por valor", command=search_value)
    botao_search.pack()

    # Função para buscar um valor em uma posição específica na lista
    def search_by_position():
        # Obtém a posição da entrada
        position = entrada_pos.get()
        if position == "" or not position.isdigit() or 10 < int(position) or int(position) <= 0:
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

        # Cria novos quadrados para cada elemento na lista
        for i in range(len(sl.list)):
            square = tk.Canvas(tela, width=60, height=60)
            square.create_rectangle(10, 10, 60, 60, fill="dark orange")
            square.create_text(30, 30, text=str(sl.list[i]), fill="white")
            square.pack(side="left")

        # Cria quadrados vazios para os espaços restantes na lista
        for _ in range(len(sl.list), 10):
            square = tk.Canvas(tela, width=60, height=60)
            square.create_rectangle(10, 10, 60, 60)
            square.pack(side="left")

        # Atualiza o rótulo do contador com o número de elementos
        label_contador.config(text=f"Número de elementos: {len(sl.list)}/10.")

    janela.mainloop()






# aqui

def display_linked_list():
    # Cria uma nova lista encadeada
    ll = LinkedList()

    # Configura a janela da interface gráfica
    janela = ThemedTk(theme="ubuntu")
    janela.title("Lista Simplesmente Encadeada")
    janela.geometry("800x800")

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

    # Cria um botão para inserir um valor na última posição lista encadeada
    botao_insert = ttk.Button(janela, text="Inserir na Última Posição", command=insert_value)
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

    botao_remove = ttk.Button(janela, text="Remover por valor", command=remove_value)
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

    botao_search = ttk.Button(janela, text="Buscar por valor", command=search_value)
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
    janela.geometry("800x800")

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

    botao_insert = ttk.Button(janela, text="Inserir na Última Posição", command=insert_value)
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
    botao_remove = ttk.Button(janela, text="Remover por valor", command=remove_value)
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
    botao_search = ttk.Button(janela, text="Buscar por valor", command=search_value)
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

def display_stack():
    stack = Stack()  # Corrigido aqui

    janela = ThemedTk(theme="ubuntu")
    janela.title("Pilha")
    janela.geometry("800x800")

    frame = ttk.Frame(janela)
    frame.pack()

    value_label = ttk.Label(janela, text="Valor:")
    value_label.pack(side="left")

    value_entry = ttk.Entry(janela)
    value_entry.pack(side="left")

    message_label = ttk.Label(janela)
    message_label.pack()

    count_label = ttk.Label(janela)
    count_label.pack()

    def push_value():
        value = value_entry.get()
        message = stack.push(value)
        message_label.config(text=message)
        display_elements()

    push_button = ttk.Button(janela, text="Empilhar", command=push_value)
    push_button.pack(side="left")
    push_button.place(x=45, y=100)
    
    def pop_value():
        message = stack.pop()
        message_label.config(text=message)
        display_elements()

    pop_button = ttk.Button(janela, text="Desempilhar", command=pop_value)
    pop_button.pack()
    pop_button.place(x=45, y=150)

    def peek_value():
        message = stack.peek()
        message_label.config(text=message)

    peek_button = ttk.Button(janela, text="Topo da pilha", command=peek_value)
    peek_button.pack(side="left")
    peek_button.place(x=45, y=200)

    def display_elements():
        for widget in frame.winfo_children():
            widget.destroy()

        for i in range(len(stack.stack)-1, -1, -1):  # Modificado aqui
            square = tk.Canvas(frame, width=60, height=60)
            square.create_rectangle(10, 10, 60, 60, fill="purple")
            square.create_text(30, 30, text=str(stack.stack[i]), fill="white")
            square.pack()  

            if i != 0:  # Modificado aqui
                comma_label = ttk.Label(frame, text="")
                comma_label.pack()

        count_label.config(text=f"Número de elementos: {len(stack.stack)}/10.")

    janela.mainloop()

def display_queue():
    queue = Queue()

    janela = ThemedTk(theme="ubuntu")
    janela.title("Fila")
    janela.geometry("800x800")

    frame = ttk.Frame(janela)
    frame.pack()

    value_label = ttk.Label(janela, text="Valor:")
    value_label.pack(side="left")

    value_entry = ttk.Entry(janela)
    value_entry.pack(side="left")

    message_label = ttk.Label(janela)
    message_label.pack()

    count_label = ttk.Label(janela)
    count_label.pack()

    def enqueue_front_value():
        value = value_entry.get()
        message = queue.enqueue_front(value)
        message_label.config(text=message)
        display_elements()

    enqueue_front_button = ttk.Button(janela, text="Adicionar no início", command=enqueue_front_value, x=100,y=100)
    enqueue_front_button.pack()

    def dequeue_back_value():
        message = queue.dequeue_back()
        message_label.config(text=message)
        display_elements()

    dequeue_back_button = ttk.Button(janela, text="Remover do final", command=dequeue_back_value)
    dequeue_back_button.pack()

    def first_value():
        message = queue.first()
        message_label.config(text=f"Primeiro elemento da fila: {message}.")

    first_button = ttk.Button(janela, text="Primeiro da fila", command=first_value)
    first_button.pack()

    def last_value():
        message = queue.last()
        message_label.config(text=f"Último elemento da fila: {message}.")

    last_button = ttk.Button(janela, text="Último da fila", command=last_value)
    last_button.pack()

    def display_elements():
        for widget in frame.winfo_children():
            widget.destroy()

        for i in range(len(queue.queue)):
            square = tk.Canvas(frame, width=60, height=60)
            square.create_rectangle(10, 10, 60, 60, fill="magenta")
            square.create_text(30, 30, text=str(queue.queue[i]), fill="white")
            square.pack(side='left')

            if i != len(queue.queue) - 1:
                comma_label = ttk.Label(frame, text="")
                comma_label.pack(side='left')

        count_label.config(text=f"Número de elementos: {len(queue.queue)}/10.")

    janela.mainloop()


def display_bst():
    arvoreBP = ArvoreBinariaPesquisa()
    
    janela = ThemedTk(theme="ubuntu")
    janela.title("Árvore Binária de Pesquisa")
    janela.geometry("800x800")
    
    frame = ttk.Frame(janela)
    frame.pack()
    
    value_label = ttk.Label(janela, text="Valor:")
    value_label.pack()
    
    value_entry = ttk.Entry(janela)
    value_entry.pack()
    
    message_label = ttk.Label(janela)
    message_label.pack()
    
    count_label = ttk.Label(janela)
    count_label.pack()

    # Cria um canvas para desenhar a árvore
    canvas = Canvas(janela, width=800, height=800)
    canvas.pack()
    
    pre_ordem_label = ttk.Label(janela)
    pre_ordem_label.pack()
    pre_ordem_label.place(x=100, y=500)
    
    in_ordem_label = ttk.Label(janela)
    in_ordem_label.pack()
    in_ordem_label.place(x=100, y=600)

    pos_ordem_label = ttk.Label(janela)
    pos_ordem_label.pack()
    pos_ordem_label.place(x=100, y=700)
    
    
    def calcula_posicoes(no, profundidade=0, pos_x=400, espaco=200):
        if no is None:
            return {}
        
        posicoes = {}
        # Adiciona 100 (em vez de 50) à posição y do nó raiz
        posicoes[no] = (pos_x, profundidade * 50 + 100)

        # Calcula as posições dos nós filhos com uma profundidade maior e uma posição x ajustada
        posicoes.update(calcula_posicoes(no.esq, profundidade + 1, pos_x - espaco/2, espaco/2))  # 20 é o espaçamento horizontal entre os nós
        posicoes.update(calcula_posicoes(no.dir, profundidade + 1, pos_x + espaco/2, espaco/2))
        
        return posicoes


    def desenha_no(no_grafico):
        x, y = no_grafico.pos_x, no_grafico.pos_y
        r = no_grafico.raio

        # Desenha o círculo
        canvas.create_oval(x-r, y-r, x+r, y+r)

        # Desenha o valor do nó
        canvas.create_text(x, y, text=str(no_grafico.no.conteudo))
        
    def desenha_linha(no_grafico1, no_grafico2):
        x1, y1 = no_grafico1.pos_x, no_grafico1.pos_y + no_grafico1.raio
        x2, y2 = no_grafico2.pos_x, no_grafico2.pos_y - no_grafico2.raio

        canvas.create_line(x1, y1, x2, y2)

    def insere():
        valor = value_entry.get()
        if valor:
            if arvoreBP.insere(int(valor)):
                message_label.config(text=f"Valor {int(valor)} inserido com sucesso.")
                # Após inserir um novo nó, redesenhe a árvore
                desenha_arvore()
            else:
                message_label.config(text=f"Valor {int(valor)} já existe na árvore.")
        else:
            message_label.config(text="Por favor, insira um valor.")
        value_entry.delete(0, 'end')

    def desenha_arvore():
        # Limpa o canvas
        canvas.delete('all')
        
        # Calcula as posições dos nós gráficos
        posicoes = calcula_posicoes(arvoreBP.raiz)
        
        # Cria os nós gráficos e desenha os nós e as linhas de conexão
        for no, (pos_x, pos_y) in posicoes.items():
            no_grafico = NoGrafico(no, pos_x, pos_y)
            desenha_no(no_grafico)
            if no.esq is not None and no.esq in posicoes:
                desenha_linha(no_grafico, NoGrafico(no.esq, *posicoes[no.esq]))
            if no.dir is not None and no.dir in posicoes:
                desenha_linha(no_grafico, NoGrafico(no.dir, *posicoes[no.dir]))

        # Desenha uma seta acima do nó raiz
        if arvoreBP.raiz is not None and arvoreBP.raiz in posicoes:
            raiz_x, raiz_y = posicoes[arvoreBP.raiz]
            canvas.create_line(raiz_x, raiz_y - 50, raiz_x, raiz_y - 20)
            canvas.create_polygon(raiz_x - 5, raiz_y - 30, raiz_x + 5, raiz_y - 30, raiz_x, raiz_y - 20)

        # Adiciona um rótulo acima da seta para indicar que aquele é o nó raiz
        canvas.create_text(raiz_x, raiz_y - 70, text="Nó Raiz")

    def remove():
            valor = value_entry.get()
            vazia = arvoreBP.vazia()
            if valor:
                if arvoreBP.remove(int(valor)):
                    message_label.config(text=f"Valor {int(valor)} removido com sucesso.")
                    # Após remover um nó, redesenhe a árvore
                    desenha_arvore()
                elif vazia:
                    message_label.config(text="Árvore vazia.")
                else:
                    message_label.config(text=f"Valor {int(valor)} não encontrado na árvore.")
            else:
                message_label.config(text="Por favor, insira um valor.")
            value_entry.delete(0, 'end')
            
        
    def busca():
        valor = value_entry.get()
        if valor:
            no = arvoreBP.busca(int(valor))
            vazia = arvoreBP.vazia()
            if no is not None:
                message_label.config(text=f"Valor {int(valor)} encontrado na árvore.")
            elif vazia:
                message_label.config(text=f"Árvore vazia.")
            else:
                message_label.config(text=f"Não encontramos o valor {int(valor)} na árvore.")
        else:
            message_label.config(text="Por favor, insira um valor.")
        value_entry.delete(0, 'end')

    def atualiza_pre_ordem():
        pre_ordem_label.config(text="Pré-ordem: " + arvoreBP.pre_ordem())
        
    def atualiza_in_ordem():
        in_ordem_label.config(text="In-ordem: " + arvoreBP.in_ordem())

    def atualiza_pos_ordem():
        pos_ordem_label.config(text="Pós-ordem: " + arvoreBP.pos_ordem())


    insere_button = ttk.Button(janela, text="Inserir", command=insere)
    insere_button.pack()    
    insere_button.place(x=50, y=30)

    remove_button = ttk.Button(janela, text="Remover", command=remove)
    remove_button.pack()    
    remove_button.place(x=50, y=60)
    
    busca_button = ttk.Button(janela, text="Buscar", command=busca)
    busca_button.pack()    
    busca_button.place(x=50, y=90)    
    
    pre_ordem_button = ttk.Button(janela, text="Pré-ordem", command=atualiza_pre_ordem)
    pre_ordem_button.pack()    
    pre_ordem_button.place(x=50, y=120)
    
    in_ordem_button = ttk.Button(janela, text="In-ordem", command=atualiza_in_ordem)
    in_ordem_button.pack()    
    in_ordem_button.place(x=50, y=150)
    
    pos_ordem_button = ttk.Button(janela, text="Pós-ordem", command=atualiza_pos_ordem)
    pos_ordem_button.pack()    
    pos_ordem_button.place(x=50, y=180)

    janela.mainloop()        
    
def main():
    # Cria uma nova janela com o tema "ubuntu"
    janela = ThemedTk(theme="ubuntu")
    janela.title("Simulador de Estruturas de Dados")  # Define o título da janela
    janela.geometry("1100x400")  # Define o tamanho da janela

    # Cria um rótulo de boas-vindas na janela
    label = ttk.Label(janela, text='\nBem-vindo ao Simulador de Estruturas de Dados!', font=("Arial", 28), width=40,
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

    # Cria um botão para exibir a Pilha
    botaoPilha = ttk.Button(janela, text="Pilha Sequencial", command=display_stack, width=40,
                          padding={"sticky": "nswe"})
    botaoPilha.pack()

    # Cria um botão para exibir a Fila
    botaoFila = ttk.Button(janela, text="Fila Sequencial", command=display_queue, width=40,
                          padding={"sticky": "nswe"})
    botaoFila.pack()
    
        # Cria um botão para exibir a Árvore
    botaoArvore = ttk.Button(janela, text="Árvore Binária de Pesquisa", command=display_bst, width=40,
                          padding={"sticky": "nswe"})
    botaoArvore.pack()

    # Inicia o loop principal da janela
    janela.mainloop()

# Verifica se este arquivo é o arquivo principal sendo executado
if __name__ == "__main__":
    main()  # Se for, executa a função main