class DoublyNode:
    def __init__(self, value):
        self.value = value  # Valor do nó
        self.prev = None  # Referência ao nó anterior
        self.next = None  # Referência ao próximo nó


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Primeiro nó da lista
        self.tail = None  # Último nó da lista

    def insert(self, value):
        new_node = DoublyNode(value)  # Cria um novo nó
        if not self.head:  # Se a lista estiver vazia
            self.head = new_node  # O novo nó é o head e tail
            self.tail = new_node
        else:  # Se a lista não estiver vazia
            new_node.prev = self.tail  # Insere o novo nó no final da lista
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, value):
        current = self.head  # Começa pelo primeiro nó
        while current:  # Enquanto houver nós na lista
            if current.value == value:  # Se o valor do nó atual for o valor procurado
                if current.prev:  # Se não for o primeiro nó
                    current.prev.next = current.next  # Atualiza as referências dos nós vizinhos
                else:
                    self.head = current.next  # Se for o primeiro nó, atualiza o head
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev  # Se for o último nó, atualiza o tail
                return
            current = current.next

    def search(self, value):
        current = self.head  # Começa pelo primeiro nó
        position = 0  # Posição inicial
        while current:  # Enquanto houver nós na lista
            if current.value == value:  # Se o valor do nó atual for o valor procurado
                return position  # Retorna a posição do nó
            position += 1  # Incrementa a posição
            current = current.next  # Vai para o próximo nó
        return -1  # Se não encontrar o valor, retorna -1

    def insert_at(self, index, value):
        # Verifica se o índice fornecido é válido
        if index < 0:
            return "Índice inválido!"

        # Cria um novo nó com o valor fornecido
        new_node = DoublyNode(value)

        # Se o índice for zero, insere o novo nó no início da lista
        if index == 0:
            # Se a lista estiver vazia, o novo nó se torna a cabeça e a cauda da lista
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                # Se a lista não estiver vazia, insere o novo nó antes da cabeça atual e se torna a nova cabeça
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        else:
            # Se o índice não for zero, percorre a lista até encontrar a posição correta para inserir o novo nó
            current = self.head
            position = 0
            previous_node = None

            while position < index and current is not None:
                position += 1
                previous_node = current
                current = current.next

            """ Se a posição correta for encontrada e existir um nó anterior,
            insere o novo nó após o nó anterior e antes do nó atual """
            if position == index and previous_node is not None:
                previous_node.next = new_node
                new_node.prev = previous_node
                new_node.next = current

                """" Se o novo nó for inserido antes de um nó existente, atualiza o ponteiro 'prev'
                do nó existente para apontar para o novo nó"""
                if current is not None:
                    current.prev = new_node

                # Se o novo nó for o último na lista, ele se torna a nova cauda da lista
                if new_node.next is None:
                    self.tail = new_node

    def remove_at(self, index):
        # Verifica se o índice fornecido é válido e se a lista não está vazia
        if index < 0 or not self.head:
            return "Índice inválido!"

        # Se o índice for zero, remove o nó da cabeça
        if index == 0:
            # Se a cabeça for o único nó na lista, a cabeça e a cauda da lista são definidas como None
            if not self.head.next:
                self.head = None
                self.tail = None
            else:
                # Se houver mais nós na lista, o segundo nó se torna a nova cabeça e os ponteiros são atualizados
                next_node = self.head.next
                next_node.prev = None
                self.head.next = None
                self.head = next_node

        else:
            # Se o índice não for zero, percorre a lista até encontrar a posição correta para remover o nó
            current = self.head
            position = 0
            previous_node = None

            while position < index and current is not None:
                position += 1
                previous_node = current
                current = current.next

            """ Se a posição correta for encontrada e existir um nó anterior,
            remove o nó atual e atualiza os ponteiros dos nós adjacentes """
            if position == index and previous_node is not None:
               next_node = previous_node.next.next

               if next_node is not None:
                   next_node.prev = previous_node

               previous_node.next = next_node

               # Se o nó removido for o último na lista, o nó anterior se torna a nova cauda da lista
               if next_node is None:
                   tail = previous_node

