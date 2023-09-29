import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from ls import SequentialList
from lse import LinkedList
from lde import DoublyLinkedList


def display_sequential_list():
    sl = SequentialList(10)  # Define um limite de 10 elementos
    
    root = ThemedTk(theme="ubuntu")
    root.title("Lista Sequencial")
    root.geometry("800x400")        
    
    frame = ttk.Frame(root)
    frame.pack()

    label_value = ttk.Label(root, text="Valor:")
    label_value.pack(side="left")
    
    entry = ttk.Entry(root)
    entry.pack(side="left")

    # Adiciona um rótulo e uma caixa de entrada para a posição
    label_position = ttk.Label(root, text="Posição:")
    label_position.pack(side="left")
    
    entry_position = ttk.Entry(root)
    entry_position.pack(side="left")

    label = ttk.Label(root)
    label.pack()

    # Adiciona um rótulo para exibir o número de elementos
    count_label = ttk.Label(root)
    count_label.pack()

    def insert_value():
        value = entry.get()
        if value == "":
            label.config(text="Erro! A entrada está vazia!")
        elif len(sl.list) < sl.limit:
            sl.insert(value)
            display_elements()
        else:
            label.config(text=f"Erro! A lista atingiu seu limite de {sl.limit} elementos!")

    button_insert = ttk.Button(root, text="Inserir", command=insert_value)
    button_insert.pack()


    def insert_at_position():
        value = entry.get()
        position = entry_position.get()
        if value =="":
            label.config(text="Erro! A entrada de valor está vazia!")
        elif (int(position) == 1 and len(sl.list) == 0) or (int(position)-1 == len(sl.list) and len(sl.list) < 10 and len(sl.list) > 0):
            label.config(text="Insira um valor válido")
            sl.insert(value)
            display_elements()
        elif position == "" or not position.isdigit() or int(position) < 1:
            label.config(text="Erro! Por favor, informe uma posição válida!")
        elif position.isdigit() and int(position) <= len(sl.list) and len(sl.list) < sl.limit:
            sl.insert_at_position(value, int(position) - 1)
            display_elements()
        else:
            label.config(text=f"Erro! Não é possível inserir na posição {position}.")

    # Adiciona um botão para inserir por posição
    button_insert_position = ttk.Button(root, text="Inserir por Posição", command=insert_at_position)
    button_insert_position.pack()

    def remove_value():
        value = entry.get()
        if len(sl.list) > 0:
            sl.remove(value)
            display_elements()
        else:
            label.config(text="Erro! A lista está vazia!")

    button_remove = ttk.Button(root, text="Remover por valor", command=remove_value)
    button_remove.pack()

    def remove_by_position():
        position = entry_position.get()
        if position == "" or not position.isdigit() or int(position) == 0:
            label.config(text="Erro! Por favor, informe uma posição válida!")
        elif position.isdigit() and int(position) <= len(sl.list):
            sl.remove_by_index(int(position) - 1)
            display_elements()
        else:
            label.config(text=f"Erro! Não existe elemento na posição {position}!")

    # Adiciona um botão para remover por posição
    button_remove_position = ttk.Button(root, text="Remover por Posição", command=remove_by_position)
    button_remove_position.pack()

    def search_value():
        value = entry.get()
        position = sl.search(value)
        if position != -1:
            label.config(text=f"{position + 1}ª posição: {value}.")
        else:
            label.config(text=f"Valor {value} não encontrado!")

    button_search = ttk.Button(root, text="Buscar", command=search_value)
    button_search.pack()

    def search_by_position():
        position = entry_position.get()
        if position == "" or not position.isdigit() or int(position) == 0:
            label.config(text="Erro! Por favor, informe um valor válido!")
        elif position.isdigit():
            position = int(position) - 1
        if position < len(sl.list):
            label.config(text=f"{position + 1}ª posição: {sl.list[position]}.")
        else:
            label.config(text=f"Posição {position + 1} não encontrada!")

    button_search_position = ttk.Button(root, text="Buscar por Posição", command=search_by_position)
    button_search_position.pack()    
    def display_elements():
        for widget in frame.winfo_children():
            widget.destroy()
        
        for i in range(len(sl.list)):
            square = tk.Canvas(frame, width=60, height=60)
            square.create_rectangle(10, 10, 60, 60, fill="dark orange")
            square.create_text(30, 30, text=str(sl.list[i]), fill="white")
            square.pack(side="left")
            
            if i != len(sl.list) - 1: # Adiciona a vírgula apenas se não for o último elemento.
                comma_label = ttk.Label(frame, text="")
                comma_label.pack(side="left")

        # Atualiza o rótulo do contador com o número de elementos
        count_label.config(text=f"Número de elementos: {len(sl.list)}/10.")

    root.mainloop()


def display_linked_list():
    ll = LinkedList()
    root = ThemedTk(theme="ubuntu") 
    root.title("Lista Simplesmente Encadeada")
    root.geometry("800x300")    
    
    frame = ttk.Frame(root)
    frame.pack()


    label_value = ttk.Label(root, text="Valor:")
    label_value.pack(side="left")
    
    entry_value = ttk.Entry(root)
    entry_value.pack(side="left")

    # Adiciona um rótulo e uma caixa de entrada para a posição
    label_position = ttk.Label(root, text="Posição:")
    label_position.pack(side="left")
    
    entry_position = ttk.Entry(root)
    entry_position.pack(side="left")

    label = ttk.Label(root)
    label.pack()

    def insert_value():
        value = entry_value.get()
        if value == "" or not value.isdigit():
            label.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            ll.insert(int(value))
            display_nodes()

    button_insert = ttk.Button(root, text="Inserir", command=insert_value)
    button_insert.pack()

    def insert_at_position():
        value = entry_value.get()
        position = entry_position.get()
        if value == "" or not value.isdigit() or position == "" or not position.isdigit() or int(position) == 0:
            label.config(text="Erro! Por favor, informe um valor e uma posição válidos!")
        elif value.isdigit() and position.isdigit():
            ll.insert_at_position(int(value), int(position) - 1) # Subtrai 1 da posição
            display_nodes()

    button_insert_position = ttk.Button(root, text="Inserir por Posição", command=insert_at_position)
    button_insert_position.pack()

    def remove_value():
        value = entry_value.get()
        if value == "" or not value.isdigit():
            label.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            ll.remove(int(value))
            display_nodes()

    button_remove = ttk.Button(root, text="Remover", command=remove_value)
    button_remove.pack()

    def remove_at_position():
        position = entry_position.get()
        if position == "" or not position.isdigit() or int(position) == 0:
            label.config(text="Erro! Por favor, informe uma posição válida!")
        elif position.isdigit():
            ll.remove_at_position(int(position) - 1) # Subtrai 1 da posição
            display_nodes()

    button_remove_position = ttk.Button(root, text="Remover por Posição", command=remove_at_position)
    button_remove_position.pack()

    def search_value():
        value = entry_value.get()
        if value == "" or not value.isdigit():
            label.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            position = ll.search(int(value))
        if position != -1:
            label.config(text=f"Valor {value} encontrado na posição {position + 1}.")
        else:
            label.config(text=f"Valor {value} não encontrado!")

    button_search = ttk.Button(root, text="Buscar", command=search_value)
    button_search.pack()

    def search_by_position():
        position = entry_position.get()
        if position == "" or not position.isdigit() or int(position) == 0:
            label.config(text="Erro! Por favor, informe um valor válido!")
        elif position.isdigit():
            position = int(position) - 1
            current = ll.head
            current_position = 0
        while current:
            if current_position == position:
                label.config(text=f"{position + 1}ª posição: {current.value}.")
                return
            current_position += 1
            current = current.next
        label.config(text=f"Posição {position + 1} não encontrada!")

    button_search_position = ttk.Button(root, text="Buscar por Posição", command=search_by_position)
    button_search_position.pack()

    def display_nodes(): 
        for widget in frame.winfo_children():
            widget.destroy()
            
    # Cria um quadrado para "HEAD"
        head_square = tk.Canvas(frame, width=60, height=60)
        head_square.create_rectangle(10, 10, 60, 60, fill="light blue")
        head_square.create_text(30, 30, text="HEAD", fill="white")
        head_square.pack(side="left")

    # Adiciona uma seta após "HEAD"
        head_arrow = ttk.Label(frame, text="➡", font=("Segoe UI Symbol", 30))
        head_arrow.pack(side="left", padx=(0,0))

        current = ll.head
        while current:
            square = tk.Canvas(frame, width=60, height=60)
            square.create_rectangle(10, 10, 60, 60, fill="blue")
            square.create_text(30, 30, text=str(current.value), fill="white")
            square.pack(side="left")
            
            if current.next is not None: # Adiciona a seta apenas se houver um próximo nó.
                arrow_label = ttk.Label(frame, text="➡", font=("Segoe UI Symbol", 30))
                arrow_label.pack(side="left", padx=(0,0))
                
            current = current.next

    root.mainloop()

def display_doubly_linked_list():
    dll = DoublyLinkedList()

    root = ThemedTk(theme="ubuntu")
    root.title("Lista duplamente encadeada")
    root.geometry("800x400")    
    
    frame = ttk.Frame(root)
    frame.pack()

    
    label_value = ttk.Label(root, text="Valor:")
    label_value.pack(side="left")
    
    entry = ttk.Entry(root)
    entry.pack(side="left")

    # Adiciona um rótulo e uma caixa de entrada para a posição
    label_position = ttk.Label(root, text="Posição:")
    label_position.pack(side="left")
    
    entry_position = ttk.Entry(root)
    entry_position.pack(side="left")

    label = ttk.Label(root)
    label.pack()

    def insert_value():
        value = entry.get()
        if value == "" or not value.isdigit():
            label.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            dll.insert(int(value))
            display_nodes()

    button_insert = ttk.Button(root, text="Inserir", command=insert_value)
    button_insert.pack()

    def insert_at_position():
        value = entry.get()
        position = entry_position.get()
        if not value.isdigit() or not position.isdigit() or int(position) < 1:
            label.config(text="Erro! Por favor, informe um valor e uma posição válidos!")
        else:
            dll.insert_at(int(position) - 1, int(value))
            display_nodes()

    button_insert_position = ttk.Button(root, text="Inserir por Posição", command=insert_at_position)
    button_insert_position.pack()

    def remove_value():
        value = entry.get()
        if value == "" or not value.isdigit():
            label.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            dll.remove(int(value))
            display_nodes()

    button_remove = ttk.Button(root, text="Remover", command=remove_value)
    button_remove.pack()
    
    def remove_at_position():
        position = entry_position.get()
        if not position.isdigit() or int(position) < 1:
            label.config(text="Erro! Por favor, informe uma posição válida!")
        else:
            dll.remove_at(int(position) - 1)
            display_nodes()

    button_remove_position = ttk.Button(root, text="Remover por Posição", command=remove_at_position)
    button_remove_position.pack()
    
    def search_value():
        value = entry.get()
        if value == "" or not value.isdigit():
            label.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            position = dll.search(int(value))
        if position != -1:
            label.config(text=f"Valor {value} encontrado na posição {position + 1}.")
        else:
            label.config(text=f"Valor {value} não encontrado!")

    button_search = ttk.Button(root, text="Buscar", command=search_value)
    button_search.pack()

    def search_by_position():
        position = entry_position.get()
        if position == "" or not position.isdigit() or int(position) == 0:
            label.config(text="Erro! Por favor, informe um valor válido!")
        elif position.isdigit():
            position = int(position) - 1
            current = dll.head
            current_position = 0
        while current:
            if current_position == position:
                label.config(text=f"{position + 1}ª posição: {current.value}.")
                return
            current_position += 1
            current = current.next
        label.config(text=f"Posição {position + 1} não encontrada!")

    button_search_position = ttk.Button(root, text="Buscar por Posição", command=search_by_position)
    button_search_position.pack()

    def display_nodes():
        for widget in frame.winfo_children():
            widget.destroy()
    def display_nodes():
        for widget in frame.winfo_children():
            widget.destroy()
        # Cria um quadrado para "HEAD"
        head_square = tk.Canvas(frame, width=60, height=60)
        head_square.create_rectangle(10, 10, 60, 60, fill="blue")
        head_square.create_text(30, 30, text="HEAD", fill="white")
        head_square.pack(side="left", padx=(0,0))

        # Adiciona uma seta após "HEAD"
        head_arrow = ttk.Label(frame, text="➡", font=("Segoe UI Symbol", 30))
        head_arrow.pack(side="left", padx=(0,0))

        current = dll.head
        while current:
            square = tk.Canvas(frame, width=60, height=60)
            square.create_rectangle(10, 10, 60, 60, fill="green")
            square.create_text(30, 30, text=str(current.value), fill="white")
            square.pack(side="left", padx=(0,0))
            
            if current.next is not None: # Adiciona a seta para o próximo nó.
                arrow_frame = ttk.Frame(frame)
                arrow_label_right = ttk.Label(arrow_frame, text="→", font=("Segoe UI Symbol", 30))
                arrow_label_right.pack(side="top", padx=(0,0), pady=(0,0))
                arrow_label_left = ttk.Label(arrow_frame, text="←", font=("Segoe UI Symbol", 30))
                arrow_label_left.pack(side="top", padx=(0,0), pady=(0,0))
                arrow_frame.pack(side="left", padx=(0,0))

            current = current.next


        tail_arrow = ttk.Label(frame, text="⬅", font=("Segoe UI Symbol", 30))
        tail_arrow.pack(side="left", padx=(0,0))


        tail_square = tk.Canvas(frame, width=60, height=60)
        tail_square.create_rectangle(10, 10, 60, 60, fill="blue")
        tail_square.create_text(30, 30, text="TAIL", fill="white")
        tail_square.pack(side="left", padx=(0,0))

        root.mainloop()

def main():
    
    root = ThemedTk(theme="ubuntu")
    root.title("Simulador de Listas")
    root.geometry("730x300")    
    
    label = ttk.Label(root, text='\nBem-vindo ao Simulador de Listas!',font=("Arial", 28), width=30, padding={"sticky": "nswe"},foreground="dark orange")
    label.pack()

    button1 = ttk.Button(root, text="Lista Sequencial", command=display_sequential_list, width=40, padding={"sticky": "nswe"})
    button1.pack()

    button2 = ttk.Button(root, text="Lista Simplesmente Encadeada", command=display_linked_list, width=40, padding={"sticky": "nswe"})
    button2.pack()

    button3 = ttk.Button(root, text="Lista Duplamente Encadeada", command=display_doubly_linked_list, width=40, padding={"sticky": "nswe"})
    button3.pack()

    root.mainloop()



if __name__ == "__main__":
    main()