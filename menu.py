import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from ls import SequentialList
from lse import LinkedList
from lde import DoublyLinkedList


def display_sequential_list():
    sl = SequentialList(10)  # Define um limite de 10 elementos
    
    janela = ThemedTk(theme="ubuntu")
    janela.title("Lista Sequencial")
    janela.geometry("800x400")        
    
    tela = ttk.Frame(janela)
    tela.pack()

    label_valor = ttk.Label(janela, text="Valor:")
    label_valor.pack(side="left")
    
    entrada_valor = ttk.Entry(janela)
    entrada_valor.pack(side="left")

    # Adiciona um rótulo e uma caixa de entrada para a posição
    label_pos = ttk.Label(janela, text="Posição:")
    label_pos.pack(side="left")
    
    entrada_pos = ttk.Entry(janela)
    entrada_pos.pack(side="left")

    label_mensageiro = ttk.Label(janela)
    label_mensageiro.pack()

    # Adiciona um rótulo para exibir o número de elementos
    label_contador = ttk.Label(janela)
    label_contador.pack()

    def insert_value():
        value = entrada_valor.get()
        if value == "":
            label_mensageiro.config(text="Erro! A entrada está vazia!")
        elif len(sl.list) < sl.limit:
            sl.insert(value)
            display_elements()
        else:
            label_mensageiro.config(text=f"Erro! A lista atingiu seu limite de {sl.limit} elementos!")

    botao_insert = ttk.Button(janela, text="Inserir", command=insert_value)
    botao_insert.pack()


    def insert_at_position():
        value = entrada_valor.get()
        position = entrada_pos.get()
        if value =="":
            label_mensageiro.config(text="Erro! A entrada de valor está vazia!")
        elif (int(position) == 1 and len(sl.list) == 0) or (int(position)-1 == len(sl.list) and len(sl.list) < 10 and len(sl.list) > 0):
            label_mensageiro.config(text="Insira um valor válido")
            sl.insert(value)
            display_elements()
        elif position == "" or not position.isdigit() or int(position) < 1:
            label_mensageiro.config(text="Erro! Por favor, informe uma posição válida!")
        elif position.isdigit() and int(position) <= len(sl.list) and len(sl.list) < sl.limit:
            sl.insert_at_position(value, int(position) - 1)
            display_elements()
        else:
            label_mensageiro.config(text=f"Erro! Não é possível inserir na posição {position}.")

    # Adiciona um botão para inserir por posição
    botao_insert_position = ttk.Button(janela, text="Inserir por Posição", command=insert_at_position)
    botao_insert_position.pack()

    def remove_value():
        value = entrada_valor.get()
        if len(sl.list) > 0:
            sl.remove(value)
            display_elements()
        else:
            label_mensageiro.config(text="Erro! A lista está vazia!")

    botao_remove = ttk.Button(janela, text="Remover por valor", command=remove_value)
    botao_remove.pack()

    def remove_by_position():
        position = entrada_pos.get()
        if position == "" or not position.isdigit() or int(position) == 0:
            label_mensageiro.config(text="Erro! Por favor, informe uma posição válida!")
        elif position.isdigit() and int(position) <= len(sl.list):
            sl.remove_by_index(int(position) - 1)
            display_elements()
        else:
            label_mensageiro.config(text=f"Erro! Não existe elemento na posição {position}!")

    # Adiciona um botão para remover por posição
    botao_remove_position = ttk.Button(janela, text="Remover por Posição", command=remove_by_position)
    botao_remove_position.pack()

    def search_value():
        value = entrada_valor.get()
        position = sl.search(value)
        if position != -1:
            label_mensageiro.config(text=f"{position + 1}ª posição: {value}.")
        else:
            label_mensageiro.config(text=f"Valor {value} não encontrado!")

    botao_search = ttk.Button(janela, text="Buscar", command=search_value)
    botao_search.pack()

    def search_by_position():
        position = entrada_pos.get()
        if position == "" or not position.isdigit() or int(position) == 0:
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif position.isdigit():
            position = int(position) - 1
        if position < len(sl.list):
            label_mensageiro.config(text=f"{position + 1}ª posição: {sl.list[position]}.")
        else:
            label_mensageiro.config(text=f"Posição {position + 1} não encontrada!")

    botao_search_position = ttk.Button(janela, text="Buscar por Posição", command=search_by_position)
    botao_search_position.pack()
        
    def display_elements():
        for widget in tela.winfo_children():
            widget.destroy()
        
        for i in range(len(sl.list)):
            square = tk.Canvas(tela, width=60, height=60)
            square.create_rectangle(10, 10, 60, 60, fill="dark orange")
            square.create_text(30, 30, text=str(sl.list[i]), fill="white")
            square.pack(side="left")
            
            if i != len(sl.list) - 1: # Adiciona a vírgula apenas se não for o último elemento.
                comma_label = ttk.Label(tela, text="")
                comma_label.pack(side="left")

        # Atualiza o rótulo do contador com o número de elementos
        label_contador.config(text=f"Número de elementos: {len(sl.list)}/10.")

    janela.mainloop()


def display_linked_list():
    ll = LinkedList()
    janela = ThemedTk(theme="ubuntu") 
    janela.title("Lista Simplesmente Encadeada")
    janela.geometry("800x300")    
    
    tela = ttk.Frame(janela)
    tela.pack()


    label_valor = ttk.Label(janela, text="Valor:")
    label_valor.pack(side="left")
    
    entrada_valor = ttk.Entry(janela)
    entrada_valor.pack(side="left")

    # Adiciona um rótulo e uma caixa de entrada para a posição
    label_pos = ttk.Label(janela, text="Posição:")
    label_pos.pack(side="left")
    
    entrada_pos = ttk.Entry(janela)
    entrada_pos.pack(side="left")

    label_mensageiro = ttk.Label(janela)
    label_mensageiro.pack()

    def insert_value():
        value = entrada_valor.get()
        if value == "" or not value.isdigit():
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            ll.insert(int(value))
            display_nodes()

    botao_insert = ttk.Button(janela, text="Inserir", command=insert_value)
    botao_insert.pack()

    def insert_at_position():
        value = entrada_valor.get()
        position = entrada_pos.get()
        if value == "" or not value.isdigit() or position == "" or not position.isdigit() or int(position) == 0:
            label_mensageiro.config(text="Erro! Por favor, informe um valor e uma posição válidos!")
        elif value.isdigit() and position.isdigit():
            ll.insert_at_position(int(value), int(position) - 1) # Subtrai 1 da posição
            display_nodes()

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
            ll.remove_at_position(int(position) - 1) # Subtrai 1 da posição
            display_nodes()

    botao_remove_position = ttk.Button(janela, text="Remover por Posição", command=remove_at_position)
    botao_remove_position.pack()

    def search_value():
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
        head_arrow = ttk.Label(tela, text="➡️", font=("Helvetica", 30))
        head_arrow.pack(side="left")

        current = ll.head
        while current:
            square = tk.Canvas(tela, width=60, height=60)
            square.create_rectangle(10, 10, 60, 60, fill="blue")
            square.create_text(30, 30, text=str(current.value), fill="white")
            square.pack(side="left")
            
            if current.next is not None: # Adiciona a seta apenas se houver um próximo nó.
                arrow_label = ttk.Label(tela, text="➡️", font=("Helvetica", 30))
                arrow_label.pack(side="left")
                
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

    def remove_value():
        value = entry_value.get()
        if value == "" or not value.isdigit():
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            dll.remove(int(value))
            display_nodes()

    botao_remove = ttk.Button(janela, text="Remover", command=remove_value)
    botao_remove.pack()
    
    def remove_at_position():
        position = entry_position.get()
        if not position.isdigit() or int(position) < 1:
            label_mensageiro.config(text="Erro! Por favor, informe uma posição válida!")
        else:
            dll.remove_at(int(position) - 1)
            display_nodes()

    botao_remove_position = ttk.Button(janela, text="Remover por Posição", command=remove_at_position)
    botao_remove_position.pack()
    
    def search_value():
        value = entry_value.get()
        if value == "" or not value.isdigit():
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif value.isdigit():
            position = dll.search(int(value))
        if position != -1:
            label_mensageiro.config(text=f"Valor {value} encontrado na posição {position + 1}.")
        else:
            label_mensageiro.config(text=f"Valor {value} não encontrado!")

    botao_search = ttk.Button(janela, text="Buscar", command=search_value)
    botao_search.pack()

    def search_by_position():
        position = entry_position.get()
        if position == "" or not position.isdigit() or int(position) == 0:
            label_mensageiro.config(text="Erro! Por favor, informe um valor válido!")
        elif position.isdigit():
            position = int(position) - 1
            current = dll.head
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
        head_square.create_rectangle(10, 10, 60, 60, fill="blue")
        head_square.create_text(30, 30, text="HEAD", fill="white")
        head_square.pack(side="left")

    # Adiciona uma seta após "HEAD"
        head_arrow = ttk.Label(tela, text="➡️", font=("Arial", 30))
        head_arrow.pack(side="left")

        current = dll.head
        while current:
            square = tk.Canvas(tela, width=60, height=60)
            square.create_rectangle(10, 10, 60, 60, fill="green")
            square.create_text(30, 30, text=str(current.value), fill="white")
            square.pack(side="left")
            
            if current.next is not None: # Adiciona a seta para o próximo nó.
                arrow_label = ttk.Label(tela, text="↔️", font=("Helvetica", 50))
                arrow_label.pack(side="left")

            current = current.next
                    
        head_arrow = ttk.Label(tela, text="⬅️", font=("Arial", 30))
        head_arrow.pack(side="left")

        tail_square = tk.Canvas(tela, width=60, height=60)
        tail_square.create_rectangle(10, 10, 60, 60, fill="light blue")
        tail_square.create_text(30, 30, text="TAIL", fill="white")
        tail_square.pack(side="left")


        janela.mainloop()

def main():
    
    janela = ThemedTk(theme="ubuntu")
    janela.title("Simulador de Listas")
    janela.geometry("730x300")    
    
    label = ttk.Label(janela, text='\nBem-vindo ao Simulador de Listas!',font=("Arial", 28), width=30, padding={"sticky": "nswe"},foreground="dark orange")
    label.pack()

    botaoLS = ttk.Button(janela, text="Lista Sequencial", command=display_sequential_list, width=40, padding={"sticky": "nswe"})
    botaoLS.pack()

    botaoLSE = ttk.Button(janela, text="Lista Simplesmente Encadeada", command=display_linked_list, width=40, padding={"sticky": "nswe"})
    botaoLSE.pack()

    botaoLDE = ttk.Button(janela, text="Lista Duplamente Encadeada", command=display_doubly_linked_list, width=40, padding={"sticky": "nswe"})
    botaoLDE.pack()

    janela.mainloop()



if __name__ == "__main__":
    main()